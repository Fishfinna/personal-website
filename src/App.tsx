import { Routes, Route } from "react-router-dom";

// styles
import "./App.scss";

// pages

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<p>home</p>} />
        <Route path="/about" element={<p>about</p>} />
        <Route path="/projects" element={<p>projects</p>} />
        <Route path="/contact" element={<p>contact</p>} />
        <Route path="*" element={<h1>404: Page not found</h1>} />
      </Routes>
    </div>
  );
}

export default App;
