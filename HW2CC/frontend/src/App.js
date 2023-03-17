import React from 'react';
import './App.css';
import HomePage from './HomePage';
import CreateCup from './CreateCup';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from './Navbar.js';
import CompetitionPage from './CompetitionPage';
import Teams from './Teams';
import TeamPage from './TeamPage';


const App = () => {
  return (
    <BrowserRouter>
      <Navbar/>
      <Routes>
          <Route path="/" element={<HomePage />}/>
          <Route path="create-cup" element={<CreateCup />} />
          <Route path="teams" element={<Teams />} />
          <Route path="competition/:id" element={<CompetitionPage />} />
          <Route path="team/:id" element={<TeamPage/>} />
          <Route path="*" element={<h1>404: Not Found</h1>} />
      </Routes>
    </BrowserRouter>
  );

}

export default App;