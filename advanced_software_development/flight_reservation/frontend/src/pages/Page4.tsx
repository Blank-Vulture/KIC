import { useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

function Page4() {
  const [date, setDate] = useState("");
  const [departure, setDeparture] = useState("");
  const [arrival, setArrival] = useState("");
  interface Flight {
    flight_name: string;
    time: string;
    business_status: string;
    economy_status: string;
  }

  const [flights, setFlights] = useState<Flight[]>([]);

  const fetchReservationStatus = async () => {
    try {
      const response = await axios.get("http://localhost:8000/flight24024/page4", {
        params: { date, departure, arrival }
      });
      setFlights(response.data.flights);
    } catch (error) {
      console.error("データ取得エラー:", error);
    }
  };

  return (
    <div className="container mt-4">
      <h2>予約状況検索</h2>
      <div className="mb-3">
        <label className="form-label">日付 (YYYY-MM-DD)</label>
        <input type="date" className="form-control" value={date} onChange={(e) => setDate(e.target.value)} />
      </div>
      <div className="mb-3">
        <label className="form-label">出発地</label>
        <input type="text" className="form-control" value={departure} onChange={(e) => setDeparture(e.target.value)} />
      </div>
      <div className="mb-3">
        <label className="form-label">到着地</label>
        <input type="text" className="form-control" value={arrival} onChange={(e) => setArrival(e.target.value)} />
      </div>
      <button className="btn btn-primary" onClick={fetchReservationStatus}>
        予約状況を検索
      </button>

      {flights.length > 0 && (
        <table className="table mt-4">
          <thead>
            <tr>
              <th>便名</th>
              <th>出発時刻</th>
              <th>ビジネスクラス</th>
              <th>エコノミークラス</th>
            </tr>
          </thead>
          <tbody>
            {flights.map((flight, index) => (
              <tr key={index}>
                <td>{flight.flight_name}</td>
                <td>{flight.time}</td>
                <td>{flight.business_status}</td>
                <td>{flight.economy_status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default Page4;