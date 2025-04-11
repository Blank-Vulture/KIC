import { useState } from "react";
import axios from "axios";
import { Table, Button, Form, Alert, Container } from "react-bootstrap";

const API_BASE = "http://localhost:8000/flight24024/page8";

const Page8 = () => {
  const [customerId, setCustomerId] = useState("");
  const [password, setPassword] = useState("");
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  interface Reservation {
    flight_name: string;
    year: number;
    month: number;
    day: number;
    time: string;
    seat_class: number;
  }
  
  const [reservations, setReservations] = useState<Reservation[]>([]);
  interface Flight {
    flight_name: string;
    departure_place: string;
    arrival_place: string;
    time: string;
  }

  const [flights, setFlights] = useState<Flight[]>([]);
  const [error, setError] = useState("");

  // **ログイン処理**
  const handleLogin = async () => {
    try {
      const response = await axios.post(`${API_BASE}/login`, null, {
        params: { customer_id: customerId, password: password },
      });

      if (response.data.success) {
        setIsLoggedIn(true);
        fetchReservations();
        fetchFlights();
      } else {
        setError("ログインに失敗しました");
      }
    } catch (err) {
      setError("ログインエラー: " + (err as any).response?.data?.detail || (err as any).message);
    }
  };

  // **予約一覧取得**
  const fetchReservations = async () => {
    try {
      const response = await axios.get(`${API_BASE}/reservations`, {
        params: { customer_id: customerId },
      });
      setReservations(response.data);
    } catch (err) {
      setError("予約情報の取得に失敗しました");
    }
  };

  // **フライト一覧取得**
  const fetchFlights = async () => {
    try {
      const response = await axios.get(`${API_BASE}/flights`);
      setFlights(response.data);
    } catch (err) {
      setError("フライト情報の取得に失敗しました");
    }
  };

  // **予約キャンセル**
  const handleCancelReservation = async (flightName: string) => {
    try {
      await axios.delete(`${API_BASE}/cancel_reservation`, {
        params: { customer_id: customerId, flight_name: flightName },
      });
      fetchReservations();
    } catch (err) {
      setError("予約キャンセルに失敗しました");
    }
  };

  // **アカウント削除**
  const handleDeleteAccount = async () => {
    try {
      await axios.delete(`${API_BASE}/delete_account`, {
        params: { customer_id: customerId, password: password },
      });
      setIsLoggedIn(false);
      setCustomerId("");
      setPassword("");
    } catch (err) {
      setError("アカウント削除に失敗しました");
    }
  };

  // **パスワード変更**
  const handleChangePassword = async (newPassword: string) => {
    try {
      await axios.put(`${API_BASE}/change_password`, null, {
        params: {
          customer_id: customerId,
          old_password: password,
          new_password: newPassword,
        },
      });
      setPassword(newPassword);
      alert("パスワードが変更されました");
    } catch (err) {
      setError("パスワード変更に失敗しました");
    }
  };

  return (
    <Container>
      <h1 className="mt-4">ダッシュボード</h1>

      {/* ログインフォーム */}
      {!isLoggedIn ? (
        <>
          {error && <Alert variant="danger">{error}</Alert>}
          <Form>
            <Form.Group className="mb-3">
              <Form.Label>顧客ID</Form.Label>
              <Form.Control
                type="text"
                value={customerId}
                onChange={(e) => setCustomerId(e.target.value)}
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>パスワード</Form.Label>
              <Form.Control
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </Form.Group>

            <Button variant="primary" onClick={handleLogin}>
              ログイン
            </Button>
          </Form>
        </>
      ) : (
        <>
          {/* ログイン後の情報 */}
          <h3>次のIDでログインしました: {customerId} </h3>
          <Button variant="danger" className="me-2" onClick={handleDeleteAccount}>
            アカウント削除
          </Button>
          <Button
            variant="warning"
            onClick={() => handleChangePassword(prompt("新しいパスワードを入力してください") || "")}
          >
            パスワード変更
          </Button>

          <hr />

          {/* 予約済みフライト一覧 */}
          <h3>予約済みのフライト</h3>
          {reservations.length > 0 ? (
            <Table striped bordered hover>
              <thead>
                <tr>
                  <th>便名</th>
                  <th>出発日</th>
                  <th>出発時刻</th>
                  <th>座席クラス</th>
                  <th>キャンセル</th>
                </tr>
              </thead>
              <tbody>
                {reservations.map((res, index) => (
                  <tr key={index}>
                    <td>{res.flight_name}</td>
                    <td>{`${res.year}-${res.month}-${res.day}`}</td>
                    <td>{res.time}</td>
                    <td>{res.seat_class === 1 ? "ビジネス" : "エコノミー"}</td>
                    <td>
                      <Button
                        variant="danger"
                        onClick={() => handleCancelReservation(res.flight_name)}
                      >
                        キャンセル
                      </Button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </Table>
          ) : (
            <p>現在予約されているフライトはありません。</p>
          )}

          <hr />

          {/* 全フライト情報 */}
          <h3>全フライト一覧</h3>
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>便名</th>
                <th>出発地</th>
                <th>到着地</th>
                <th>時間</th>
              </tr>
            </thead>
            <tbody>
              {flights.map((flight, index) => (
                <tr key={index}>
                  <td>{flight.flight_name}</td>
                  <td>{flight.departure_place}</td>
                  <td>{flight.arrival_place}</td>
                  <td>{flight.time}</td>
                </tr>
              ))}
            </tbody>
          </Table>
        </>
      )}
    </Container>
  );
};

export default Page8;