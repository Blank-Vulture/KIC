import { useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

const Page6 = () => {
  // 入力フォームの状態管理
  const [customerId, setCustomerId] = useState("");
  const [password, setPassword] = useState("");
  const [flightName, setFlightName] = useState("");
  const [seatClass, setSeatClass] = useState("0"); // 0: エコノミー, 1: ビジネス
  const [date, setDate] = useState("");

  const [message, setMessage] = useState("");

  // 予約処理
  const handleReservation = async () => {
    if (!customerId || !password || !flightName || !date) {
      setMessage("全ての項目を入力してください");
      return;
    }
  
    const [year, month, day] = date.split("-").map(Number);
  
    const requestData = {
      customer_id: Number(customerId),
      password: password.toString(), // 明示的に文字列へ
      flight_name: flightName.toString(),
      seat_class: Number(seatClass),
      year: Number(year),
      month: Number(month),
      day: Number(day),
    };
  
    console.log("送信データ:", requestData);
  
    try {
      const response = await axios.post(
        "http://localhost:8000/flight24024/page6",
        requestData,
        {
          headers: { "Content-Type": "application/json" }, // Content-Type を明示的に指定
        }
      );
      setMessage(response.data.message);
    } catch (error) {
      console.error("予約エラー:", error);
  
      const errorMessage = (error as any).response?.data?.detail;
      setMessage(
        Array.isArray(errorMessage)
          ? errorMessage.map(e => e.msg).join(", ")
          : JSON.stringify(errorMessage || "予約に失敗しました")
      );
    }
  };

  return (
    <div className="container mt-5">
      <h2>認証付き予約登録</h2>
      <div className="mb-3">
        <label className="form-label">顧客番号</label>
        <input
          type="number"
          className="form-control"
          value={customerId}
          onChange={(e) => setCustomerId(e.target.value)}
          placeholder="顧客番号を入力"
        />
      </div>

      <div className="mb-3">
        <label className="form-label">パスワード</label>
        <input
          type="password"
          className="form-control"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="パスワードを入力"
        />
      </div>

      <div className="mb-3">
        <label className="form-label">便名</label>
        <input
          type="text"
          className="form-control"
          value={flightName}
          onChange={(e) => setFlightName(e.target.value)}
          placeholder="例: RAC861"
        />
      </div>

      <div className="mb-3">
        <label className="form-label">日付</label>
        <input
          type="date"
          className="form-control"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />
      </div>

      <div className="mb-3">
        <label className="form-label">座席クラス</label>
        <select
          className="form-select"
          value={seatClass}
          onChange={(e) => setSeatClass(e.target.value)}
        >
          <option value="0">エコノミークラス</option>
          <option value="1">ビジネスクラス</option>
        </select>
      </div>

      <button className="btn btn-primary" onClick={handleReservation}>
        予約する
      </button>

      {message && <div className="alert alert-info mt-3">{message}</div>}
    </div>
  );
};

export default Page6;