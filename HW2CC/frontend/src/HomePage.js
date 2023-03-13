import React from 'react';
import { useNavigate } from 'react-router-dom';
import './HomePage.css';


const HomePage = () => {
  const Competitions = [
    {
      id: '01',
      name: 'Cupa Nikodemus',
      data_inceput: '20/07/2023',
      data_final: '25/07/2023'
    },
    {
      id: '02',
      name: 'Cupa Vicov',
      data_inceput: '20/07/2023',
      data_final: '25/07/2023'
    },
  ];
  const navigate= useNavigate();
  return (
    <ul>
      {Competitions.map((data) => (
        <li key={data.id}> 
          <button class = "button" onClick={() => navigate(`/competition/${data.id}`)}>
            <p> || {data.name} || </p>
            <p>Data desfasurarii:</p>
            <p>{data.data_inceput} - {data.data_final}</p>
          </button>
        </li>
      ))}
    </ul>
  );

};

export default HomePage;