import { useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

interface Passenger {
  id: number;
  name: string;
}

const PassengerList = () => {
  const [year, setYear] = useState("2025");
  const [month, setMonth] = useState("3");
  const [day, setDay] = useState("1");
  const [flightName, setFlightName] = useState("RAC861");
  const [passengers, setPassengers] = useState<Passenger[]>([]);
  const [error, setError] = useState("");

  const fetchPassengers = async () => {
    setError("");
    try {
      const response = await axios.get("http://localhost:8000/flight24024/page2", {
        params: { year, month, day, flight_name: flightName },
      });
      setPassengers(response.data);
    } catch (err) {
      setError("データの取得に失敗しました");
      setPassengers([]);
    }
  };

  return (
    <div className="container mt-5">
      <h2>搭乗者名簿の検索</h2>
      <div className="mb-3">
        <label className="form-label">年</label>
        <input
          type="number"
          className="form-control"
          value={year}
          onChange={(e) => setYear(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <label className="form-label">月</label>
        <input
          type="number"
          className="form-control"
          value={month}
          onChange={(e) => setMonth(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <label className="form-label">日</label>
        <input
          type="number"
          className="form-control"
          value={day}
          onChange={(e) => setDay(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <label className="form-label">便名</label>
        <input
          type="text"
          className="form-control"
          value={flightName}
          onChange={(e) => setFlightName(e.target.value)}
        />
      </div>
      <button className="btn btn-primary" onClick={fetchPassengers}>
        検索
      </button>

      {error && <div className="alert alert-danger mt-3">{error}</div>}

      <h3 className="mt-4">搭乗者リスト</h3>
      <ul className="list-group">
        {passengers.map((passenger) => (
          <li key={passenger.id} className="list-group-item">
            {passenger.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PassengerList;