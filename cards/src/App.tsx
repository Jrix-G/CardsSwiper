import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Pages/Home.tsx';
import CardCreate from './Pages/CardCreate.tsx';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/cardCreate" element={<CardCreate />} />
      </Routes>
    </Router>
  );
}

export default App;
