import React from 'react';
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './HomePage.css';


const HomePage = () => {
  const [Competitions, setCompetitions] = useState([]);
  const navigate= useNavigate();
  const url = 'http://127.0.0.1:5000/competitions';
  useEffect(() => {
      fetch(url)
        .then(response => response.json())
        .then(data => {setCompetitions(data.competitions);});
    }, []);
  return (
    <ul>
      {Competitions.map((data) => (
        <li key={data.id}> 
          <button class = "button" onClick={() => navigate(`/competition/${data.id}`)}>
            <p> || {data.name} || </p>
            <p>Data desfasurarii:</p>
            <p>{data.start_date} - {data.end_date}</p>
          </button>
        </li>
      ))}
    </ul>
  );

};

export default HomePage;