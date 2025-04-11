import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Page1 from "./pages/Page1";
import Page2 from "./pages/Page2";
import Page3 from "./pages/Page3";
import Page4 from "./pages/Page4";
import Page5 from "./pages/Page5";
import Page6 from "./pages/Page6";
import Page7 from "./pages/Page7";
import Page8 from "./pages/Page8";
import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css"; // スタイルを適用

const App = () => {
  return (
    <div className="app-container">
      <Router>
        <div className="content-wrapper">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/flight24024/page1" element={<Page1 />} />
            <Route path="/flight24024/page2" element={<Page2 />} />
            <Route path="/flight24024/page3" element={<Page3 />} />
            <Route path="/flight24024/page4" element={<Page4 />} />
            <Route path="/flight24024/page5" element={<Page5 />} />
            <Route path="/flight24024/page6" element={<Page6 />} />
            <Route path="/flight24024/page7" element={<Page7 />} />
            <Route path="/flight24024/page8" element={<Page8 />} />
          </Routes>
        </div>
      </Router>
    </div>
  );
};

export default App;