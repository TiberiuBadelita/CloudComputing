import React from 'react';
import './App.css';
import HomePage from './HomePage';
import CreateCup from './CreateCup';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from './Navbar.js';
import CompetitionPage from './CompetitionPage';
import Teams from './Teams';


const App = () => {
  return (
    <BrowserRouter>
      <Navbar/>
      <Routes>
          <Route path="/" element={<HomePage />}/>
          <Route path="create-cup" element={<CreateCup />} />
          <Route path="teams" element={<Teams />} />
          <Route path="competition/:id" element={<CompetitionPage />} />
      </Routes>
    </BrowserRouter>
  );

}

export default App;
