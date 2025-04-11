import { useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const Page3 = () => {
  const [data, setData] = useState<{
    date: string;
    departure: string;
    arrival: string;
    flights: { flight_name: string; time: string; business_status: string; economy_status: string }[];
  } | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:8000/flight24024/page3");
        if (!response.ok) throw new Error("データ取得に失敗しました");

        const result = await response.json();
        setData(result);
      } catch (error) {
        setError("サーバーとの通信に失敗しました");
      }
    };

    fetchData();
  }, []);

  return (
    <div className="container mt-4">
      <h2>予約状況</h2>
      {error && <div className="alert alert-danger">{error}</div>}
      {data && (
        <>
          <p>日付: {data.date}</p>
          <p>出発地: {data.departure}</p>
          <p>到着地: {data.arrival}</p>
          <table className="table table-bordered">
            <thead>
              <tr>
                <th>便名</th>
                <th>出発時刻</th>
                <th>ビジネスクラス</th>
                <th>エコノミークラス</th>
              </tr>
            </thead>
            <tbody>
              {data.flights.map((flight, index) => (
                <tr key={index}>
                  <td>{flight.flight_name}</td>
                  <td>{flight.time}</td>
                  <td>{flight.business_status}</td>
                  <td>{flight.economy_status}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <p>○△×の表示ルール</p>
          <ul>
            <li>ビジネスクラス: ○: 残り2席以上, △: 残り1席, ×: 満席</li>
            <li>エコノミークラス: ○: 残り5席以上, △: 残り1〜4席, ×: 満席</li>
          </ul>
        </>
      )}
    </div>
  );
};

export default Page3;