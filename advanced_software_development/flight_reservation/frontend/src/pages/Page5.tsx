import { useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

function Page5() {
  const [date, setDate] = useState("");
  const [flightName, setFlightName] = useState("");
  const [customerId, setCustomerId] = useState("");
  const [seatClass, setSeatClass] = useState("0"); // 0: エコノミー, 1: ビジネス
  const [message, setMessage] = useState("");

  const handleReservation = async () => {
    try {
      const response = await axios.post("http://localhost:8000/flight24024/page5", null, {
        params: { date, flight_name: flightName, customer_id: Number(customerId), seat_class: Number(seatClass) }
      });
      setMessage(response.data.message);
    } catch (error) {
      setMessage((error as any).response?.data.detail || "予約に失敗しました");
    }
  };

  return (
    <div className="container mt-4">
      <h2>新規予約</h2>
      <div className="mb-3">
        <label className="form-label">日付 (YYYY-MM-DD)</label>
        <input type="date" className="form-control" value={date} onChange={(e) => setDate(e.target.value)} />
      </div>
      <div className="mb-3">
        <label className="form-label">便名</label>
        <input type="text" className="form-control" value={flightName} onChange={(e) => setFlightName(e.target.value)} />
      </div>
      <div className="mb-3">
        <label className="form-label">顧客番号</label>
        <input type="number" className="form-control" value={customerId} onChange={(e) => setCustomerId(e.target.value)} />
      </div>
      <div className="mb-3">
        <label className="form-label">座席クラス</label>
        <select className="form-select" value={seatClass} onChange={(e) => setSeatClass(e.target.value)}>
          <option value="0">エコノミークラス</option>
          <option value="1">ビジネスクラス</option>
        </select>
      </div>
      <button className="btn btn-primary" onClick={handleReservation}>予約</button>

      {message && <div className="alert alert-info mt-3">{message}</div>}
    </div>
  );
}

export default Page5;