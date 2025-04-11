const Home = () => {
  return (
    <div className="center">
      <h1>フライト予約システム</h1>
      <ul className="list-group">
        <li className="list-group-item"><a href="/flight24024/page1" className="btn btn-primary">搭乗者名簿 (固定日・固定便)</a></li>
        <li className="list-group-item"><a href="/flight24024/page2" className="btn btn-secondary">搭乗者名簿 (入力対応)</a></li>
        <li className="list-group-item"><a href="/flight24024/page3" className="btn btn-success">予約状況 (固定日・固定ルート)</a></li>
        <li className="list-group-item"><a href="/flight24024/page4" className="btn btn-danger">予約状況 (入力対応)</a></li>
        <li className="list-group-item"><a href="/flight24024/page5" className="btn btn-warning">新規予約登録</a></li>
        <li className="list-group-item"><a href="/flight24024/page6" className="btn btn-info">ログイン</a></li>
        <li className="list-group-item"><a href="/flight24024/page7" className="btn btn-dark">新規顧客登録</a></li>
        <li className="list-group-item"><a href="/flight24024/page8" className="btn btn-light">自由な機能</a></li>
      </ul>
    </div>
  );
};

export default Home;