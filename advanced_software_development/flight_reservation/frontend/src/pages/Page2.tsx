import { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const Page2 = () => {
  const [date, setDate] = useState("");
  const [flightName, setFlightName] = useState("");
  const [passengers, setPassengers] = useState<{ id: number; customer_name: string }[]>([]);
  const [errorMessage, setErrorMessage] = useState("");

  const fetchPassengers = async () => {
    if (!date || !flightName) {
      setErrorMessage("日付と便名を入力してください。");
      return;
    }

    setErrorMessage(""); // エラーメッセージをクリア
    const [year, month, day] = date.split("-");

    try {
      const response = await fetch(
        `http://localhost:8000/flight24024/page2?year=${year}&month=${month}&day=${day}&flight_name=${flightName}`
      );

      if (!response.ok) {
        throw new Error("サーバーエラーが発生しました");
      }

      const data = await response.json();

      if (data.message) {
        setErrorMessage(data.message);
        setPassengers([]);
      } else if (Array.isArray(data)) {
        setPassengers(data);
      } else {
        console.error("Unexpected API Response Format:", data);
        setErrorMessage("データの取得に失敗しました");
        setPassengers([]);
      }
    } catch (error) {
      setErrorMessage("データの取得に失敗しました");
      setPassengers([]);
    }
  };

  return (
    <div className="container mt-4 text-center">
      <h2 className="mb-3">搭乗者名簿検索</h2>

      <div className="mb-3">
        <label className="form-label">搭乗日:</label>
        <input
          type="date"
          className="form-control text-center"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />
      </div>

      <div className="mb-3">
        <label className="form-label">便名:</label>
        <input
          type="text"
          className="form-control text-center"
          placeholder="例: RAC861"
          value={flightName}
          onChange={(e) => setFlightName(e.target.value)}
        />
      </div>

      <button className="btn btn-primary" onClick={fetchPassengers}>
        検索
      </button>

      {errorMessage && <div className="alert alert-danger mt-3">{errorMessage}</div>}

      {passengers.length > 0 && (
        <div className="mt-4">
          <h3>搭乗者リスト</h3>
          <ul className="list-group">
            {passengers.map((passenger, index) => (
              <li key={`${passenger.id}-${index}`} className="list-group-item">
                {passenger.customer_name}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default Page2;