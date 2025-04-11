import { useState } from "react";
import axios from "axios";

const Page7 = () => {
  const [customerName, setCustomerName] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleRegister = async () => {
    if (!customerName || !password) {
      setMessage("顧客名とパスワードを入力してください");
      return;
    }

    const requestData = {
      customer_name: customerName, // ここを FastAPI の Pydantic モデルと一致させる
      password: password,
    };

    console.log("送信データ:", requestData);

    try {
      const response = await axios.post(
        "http://localhost:8000/flight24024/page7",
        requestData,
        {
          headers: { "Content-Type": "application/json" },
        }
      );
      setMessage(`登録成功: 顧客ID ${response.data.customer_id}`);
    } catch (error) {
      console.error("登録エラー:", error);

      // API のレスポンスを適切に処理
      if (error.response && error.response.data) {
        if (typeof error.response.data === "object") {
          setMessage(error.response.data.detail || "登録に失敗しました");
        } else {
          setMessage(error.response.data);
        }
      } else {
        setMessage("ネットワークエラーが発生しました");
      }
    }
  };

  return (
    <div className="container mt-5">
      <h2>新規顧客登録</h2>
      <div className="mb-3">
        <label className="form-label">顧客名</label>
        <input
          type="text"
          className="form-control"
          value={customerName}
          onChange={(e) => setCustomerName(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <label className="form-label">パスワード</label>
        <input
          type="password"
          className="form-control"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <button className="btn btn-primary" onClick={handleRegister}>
        登録する
      </button>
      {message && <p className="mt-3">{message}</p>}
    </div>
  );
};

export default Page7;