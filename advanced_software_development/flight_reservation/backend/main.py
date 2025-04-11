from fastapi import FastAPI, Depends, Response, Query, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy.exc import IntegrityError
import os
import json
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
# CORS 設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # すべてのオリジンを許可（開発用）
    allow_credentials=True,
    allow_methods=["*"],  # すべての HTTP メソッドを許可
    allow_headers=["*"],  # すべての HTTP ヘッダーを許可
)

# MySQL の接続情報を環境変数から取得（utf8mb4 を明示）
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:XXX@db/flight_db?charset=utf8mb4")

# SQLAlchemy の設定
engine = create_engine(DATABASE_URL, connect_args={"charset": "utf8mb4"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ベースモデル
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# フライト情報
class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    flight_name = Column(String(20), index=True)
    departure_place = Column(String(100), nullable=False)
    arrival_place = Column(String(100), nullable=False)
    time = Column(String(20), nullable=False)
    cap_business = Column(Integer)
    cap_economy = Column(Integer)

# 顧客情報
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

# 予約情報
class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    flight_id = Column(Integer, ForeignKey("flights.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    seat_class = Column(Integer, nullable=False)

    flight = relationship("Flight")
    customer = relationship("Customer")

# リクエストモデル
class ReservationRequest(BaseModel):
    customer_id: int
    password: str
    flight_name: str
    seat_class: int  # 0: エコノミー, 1: ビジネス
    year: int
    month: int
    day: int

# ユーザ情報登録用リクエストモデル
class CustomerRequest(BaseModel):
    customer_name: str
    password: str

# データベース作成
Base.metadata.create_all(bind=engine)

# DBセッション管理
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "テスト"}

@app.get("/flights")
def get_flights(db: Session = Depends(get_db)):
    flights = db.query(Flight).all()
    json_data = json.dumps([{
        "id": f.id,
        "flight_name": f.flight_name,
        "departure_place": f.departure_place,
        "arrival_place": f.arrival_place,
        "time": f.time,
        "cap_business": f.cap_business,
        "cap_economy": f.cap_economy
    } for f in flights], ensure_ascii=False)  # 日本語対応

    return Response(content=json_data, media_type="application/json; charset=UTF-8")


@app.get("/flights/manifest")
def get_flight_manifest(date: str = Query(...), flight_name: str = Query(...), db: Session = Depends(get_db)):
    """
    指定された日付と便名の搭乗者名簿を取得する
    """
    # 年月日の分割（YYYY-MM-DD 形式を想定）
    year, month, day = date.split("-")

    reservations = (
        db.query(Reservation)
        .join(Flight)
        .join(Customer)
        .filter(
            Reservation.year == int(year),
            Reservation.month == int(month),
            Reservation.day == int(day),
            Flight.flight_name == flight_name
        )
        .all()
    )

    json_data = json.dumps([
        {"id": r.customer.id, "customer_name": r.customer.customer_name}
        for r in reservations
    ], ensure_ascii=False)

    return Response(content=json_data, media_type="application/json; charset=UTF-8")

@app.get("/flight24024/page2")
def get_passengers_by_flight(
    year: int = Query(..., description="年 (例: 2025)"),
    month: int = Query(..., description="月 (例: 3)"),
    day: int = Query(..., description="日 (例: 1)"),
    flight_name: str = Query(..., description="便名 (例: RAC861)"),
    db: Session = Depends(get_db)
):
    """
    指定された日付と便名の搭乗者リストを取得
    """
    reservations = (
        db.query(Reservation)
        .join(Flight)
        .join(Customer)
        .filter(
            Reservation.year == year,
            Reservation.month == month,
            Reservation.day == day,
            Flight.flight_name == flight_name
        )
        .all()
    )

    if not reservations:
        return Response(content=json.dumps({"message": "該当する搭乗者が見つかりません"}, ensure_ascii=False), media_type="application/json; charset=UTF-8")

    json_data = json.dumps([
        {"id": r.customer.id, "customer_name": r.customer.customer_name}
        for r in reservations
    ], ensure_ascii=False)

    return Response(content=json_data, media_type="application/json; charset=UTF-8")


@app.get("/flight24024/page3")
def get_reservation_status(db: Session = Depends(get_db)):
    """
    2025年3月2日の那覇 → 南大東便の予約状況
    """

    year, month, day = 2025, 3, 2
    departure, arrival = "那覇", "南大東"

    flights = db.query(Flight).filter(
        Flight.departure_place == departure,
        Flight.arrival_place == arrival
    ).all()

    results = []
    for flight in flights:
        business_reserved = db.query(Reservation).filter(
            Reservation.year == year,
            Reservation.month == month,
            Reservation.day == day,
            Reservation.flight_id == flight.id,
            Reservation.seat_class == 1  # ビジネスクラス
        ).count()

        economy_reserved = db.query(Reservation).filter(
            Reservation.year == year,
            Reservation.month == month,
            Reservation.day == day,
            Reservation.flight_id == flight.id,
            Reservation.seat_class == 0  # エコノミークラス
        ).count()

        # 空席数の計算
        business_remaining = flight.cap_business - business_reserved
        economy_remaining = flight.cap_economy - economy_reserved

        # ○△×の判定関数
        def classify_status(remain, threshold1, threshold2):
            if remain >= threshold1:
                return "○"
            elif remain >= threshold2:
                return "△"
            else:
                return "×"

        results.append({
            "flight_name": flight.flight_name,
            "time": flight.time,
            "business_status": classify_status(business_remaining, 2, 1),  # 2以上○, 1△, 0×
            "economy_status": classify_status(economy_remaining, 5, 1)  # 5以上○, 1-4△, 0×
        })

    return {
        "date": f"{year}-{month:02d}-{day:02d}",
        "departure": departure,
        "arrival": arrival,
        "flights": results
    }


@app.get("/flight24024/page4")
def get_reservation_status_dynamic(
    date: str = Query(..., description="検索する日付（YYYY-MM-DD）"),
    departure: str = Query(..., description="出発地"),
    arrival: str = Query(..., description="到着地"),
    db: Session = Depends(get_db)
):
    """
    指定された日付と出発地・到着地での予約状況を取得する
    """

    # 年・月・日に分割
    try:
        year, month, day = map(int, date.split("-"))
    except ValueError:
        return {"error": "日付の形式は YYYY-MM-DD で入力してください"}

    # 指定された条件に一致するフライトを取得
    flights = db.query(Flight).filter(
        Flight.departure_place == departure,
        Flight.arrival_place == arrival
    ).all()

    results = []
    for flight in flights:
        business_reserved = db.query(Reservation).filter(
            Reservation.year == year,
            Reservation.month == month,
            Reservation.day == day,
            Reservation.flight_id == flight.id,
            Reservation.seat_class == 1  # ビジネスクラス
        ).count()

        economy_reserved = db.query(Reservation).filter(
            Reservation.year == year,
            Reservation.month == month,
            Reservation.day == day,
            Reservation.flight_id == flight.id,
            Reservation.seat_class == 0  # エコノミークラス
        ).count()

        # 空席数の計算
        business_remaining = flight.cap_business - business_reserved
        economy_remaining = flight.cap_economy - economy_reserved

        # ○△×の判定関数
        def classify_status(remain, threshold1, threshold2):
            if remain >= threshold1:
                return "○"
            elif remain >= threshold2:
                return "△"
            else:
                return "×"

        results.append({
            "flight_name": flight.flight_name,
            "time": flight.time,
            "business_status": classify_status(business_remaining, 2, 1),  # 2以上○, 1△, 0×
            "economy_status": classify_status(economy_remaining, 5, 1)  # 5以上○, 1-4△, 0×
        })

    return {
        "date": date,
        "departure": departure,
        "arrival": arrival,
        "flights": results
    }


@app.post("/flight24024/page5")
def create_reservation(
    date: str = Query(..., description="予約する日付（YYYY-MM-DD）"),
    flight_name: str = Query(..., description="予約する便名"),
    customer_id: int = Query(..., description="顧客ID"),
    seat_class: int = Query(..., description="座席クラス（0:エコノミー, 1:ビジネス）"),
    db: Session = Depends(get_db)
):
    """
    指定された便に予約を登録する
    """

    # 年・月・日を分割
    try:
        year, month, day = map(int, date.split("-"))
    except ValueError:
        raise HTTPException(status_code=400, detail="日付の形式は YYYY-MM-DD で入力してください")

    # フライトの取得
    flight = db.query(Flight).filter(Flight.flight_name == flight_name).first()
    if not flight:
        raise HTTPException(status_code=404, detail="指定された便が見つかりません")

    # 予約が空席かチェック
    business_reserved = db.query(Reservation).filter(
        Reservation.year == year,
        Reservation.month == month,
        Reservation.day == day,
        Reservation.flight_id == flight.id,
        Reservation.seat_class == 1
    ).count()

    economy_reserved = db.query(Reservation).filter(
        Reservation.year == year,
        Reservation.month == month,
        Reservation.day == day,
        Reservation.flight_id == flight.id,
        Reservation.seat_class == 0
    ).count()

    # 空席数の計算
    business_remaining = flight.cap_business - business_reserved
    economy_remaining = flight.cap_economy - economy_reserved

    if seat_class == 1 and business_remaining <= 0:
        raise HTTPException(status_code=400, detail="ビジネスクラスは満席です")
    if seat_class == 0 and economy_remaining <= 0:
        raise HTTPException(status_code=400, detail="エコノミークラスは満席です")

    # 予約の登録
    new_reservation = Reservation(
        year=year, month=month, day=day,
        flight_id=flight.id, customer_id=customer_id,
        seat_class=seat_class
    )

    try:
        db.add(new_reservation)
        db.commit()
        return {"message": "予約が完了しました"}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="予約の登録に失敗しました")


@app.post("/flight24024/page6")
def register_reservation_with_auth(
    request: ReservationRequest,
    db: Session = Depends(get_db)
):
    """
    認証付きの予約登録 API（日付を指定可能）
    """
    
    # 顧客情報の確認
    customer = db.query(Customer).filter(Customer.id == request.customer_id).first()
    if not customer or customer.password != request.password:
        raise HTTPException(status_code=401, detail="認証失敗: 顧客番号またはパスワードが間違っています")

    # フライト情報の取得
    flight = db.query(Flight).filter(Flight.flight_name == request.flight_name).first()
    if not flight:
        raise HTTPException(status_code=404, detail="指定された便が見つかりません")

    # 既存の予約があるか確認（重複予約防止）
    existing_reservation = db.query(Reservation).filter(
        Reservation.year == request.year,
        Reservation.month == request.month,
        Reservation.day == request.day,
        Reservation.flight_id == flight.id,
        Reservation.customer_id == request.customer_id
    ).first()

    if existing_reservation:
        raise HTTPException(status_code=400, detail="すでにこの便を予約しています")

    # 予約の登録
    try:
        reservation = Reservation(
            year=request.year,
            month=request.month,
            day=request.day,
            flight_id=flight.id,
            customer_id=request.customer_id,
            seat_class=request.seat_class
        )
        db.add(reservation)
        db.commit()
        return {"message": "予約が完了しました"}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="予約の登録に失敗しました")


@app.post("/flight24024/page7")
def register_customer(request: CustomerRequest, db: Session = Depends(get_db)):
    """
    新規顧客登録API
    """

    # 既存の顧客名をチェック
    existing_customer = db.query(Customer).filter(Customer.customer_name == request.customer_name).first()
    if existing_customer:
        raise HTTPException(status_code=400, detail="この顧客名は既に登録されています")

    # 現在の最大IDを取得
    max_id = db.query(Customer.id).order_by(Customer.id.desc()).first()
    new_id = max_id[0] + 1 if max_id else 1  # max_id が None の場合、最初の ID を 1 にする

    # 新規顧客を作成
    new_customer = Customer(id=new_id, customer_name=request.customer_name, password=request.password)

    try:
        db.add(new_customer)
        db.commit()
        return {"message": "顧客登録が完了しました", "customer_id": new_customer.id}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="顧客登録に失敗しました")


@app.post("/flight24024/page8/login")
def login(customer_id: int, password: str, db: Session = Depends(get_db)):
    """
    ユーザー認証 API
    """
    customer = db.query(Customer).filter(
        Customer.id == customer_id, Customer.password == password
    ).first()

    if not customer:
        raise HTTPException(status_code=401, detail="ログイン失敗: IDまたはパスワードが間違っています")

    return {"success": True, "message": "ログイン成功"}

# **2️⃣ ユーザーの予約一覧取得**
@app.get("/flight24024/page8/reservations")
def get_user_reservations(customer_id: int, db: Session = Depends(get_db)):
    """
    指定されたユーザーの予約一覧を取得
    """
    reservations = (
        db.query(Reservation, Flight)
        .join(Flight, Reservation.flight_id == Flight.id)
        .filter(Reservation.customer_id == customer_id)
        .all()
    )

    return [
        {
            "flight_name": res.Flight.flight_name,
            "year": res.Reservation.year,
            "month": res.Reservation.month,
            "day": res.Reservation.day,
            "time": res.Flight.time,
            "seat_class": res.Reservation.seat_class
        }
        for res in reservations
    ]

# **3️⃣ 全フライトのスケジュール一覧取得**
@app.get("/flight24024/page8/flights")
def get_all_flights(db: Session = Depends(get_db)):
    """
    全フライトのスケジュール一覧を取得
    """
    flights = db.query(Flight).all()

    return [
        {
            "flight_name": f.flight_name,
            "departure_place": f.departure_place,
            "arrival_place": f.arrival_place,
            "time": f.time
        }
        for f in flights
    ]

# **4️⃣ ユーザーアカウント削除**
@app.delete("/flight24024/page8/delete_account")
def delete_account(customer_id: int, password: str, db: Session = Depends(get_db)):
    """
    ユーザー自身によるアカウント削除
    """
    customer = db.query(Customer).filter(Customer.id == customer_id, Customer.password == password).first()

    if not customer:
        raise HTTPException(status_code=401, detail="認証失敗: IDまたはパスワードが間違っています")

    db.query(Reservation).filter(Reservation.customer_id == customer_id).delete()
    db.delete(customer)
    db.commit()

    return {"message": "アカウント削除が完了しました"}

# **5️⃣ パスワード変更**
@app.put("/flight24024/page8/change_password")
def change_password(customer_id: int, old_password: str, new_password: str, db: Session = Depends(get_db)):
    """
    パスワード変更処理
    """
    customer = db.query(Customer).filter(Customer.id == customer_id, Customer.password == old_password).first()

    if not customer:
        raise HTTPException(status_code=401, detail="認証失敗: IDまたはパスワードが間違っています")

    customer.password = new_password
    db.commit()

    return {"message": "パスワードが変更されました"}

# **6️⃣ 予約キャンセル**
@app.delete("/flight24024/page8/cancel_reservation")
def cancel_reservation(customer_id: int, flight_name: str, db: Session = Depends(get_db)):
    """
    予約をキャンセルする
    """
    flight = db.query(Flight).filter(Flight.flight_name == flight_name).first()
    if not flight:
        raise HTTPException(status_code=404, detail="指定された便が見つかりません")

    reservation = db.query(Reservation).filter(
        Reservation.customer_id == customer_id,
        Reservation.flight_id == flight.id
    ).first()

    if not reservation:
        raise HTTPException(status_code=404, detail="予約が見つかりません")

    db.delete(reservation)
    db.commit()

    return {"message": "予約がキャンセルされました"}