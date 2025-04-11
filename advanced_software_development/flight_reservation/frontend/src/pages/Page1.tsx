import { useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

interface Passenger {
  id: number;
  customer_name: string;
}

const Page1 = () => {
  const [passengers, setPassengers] = useState<Passenger[]>([]);

  useEffect(() => {
    fetch(`http://localhost:8000/flights/manifest?date=2025-03-01&flight_name=RAC861`)
      .then((res) => res.json())
      .then((data) => {
        if (Array.isArray(data)) {
          setPassengers(data);
        } else {
          console.error("Unexpected API Response Format:", data);
        }
      })
      .catch((err) => console.error("Error fetching data:", err));
  }, []);

  return (
    <div className="container mt-5 text-center">
      <h2>2025年3月1日 RAC861便 搭乗者名簿</h2>
      <table className="table table-bordered mt-3">
        <thead className="table-dark">
          <tr>
            <th>ID</th>
            <th>名前</th>
          </tr>
        </thead>
        <tbody>
          {passengers.map((p, index) => (
            <tr key={`${p.id}-${index}`}>
              <td>{p.id}</td>
              <td>{p.customer_name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Page1;