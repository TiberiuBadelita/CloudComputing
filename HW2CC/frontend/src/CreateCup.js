import React from 'react';
import './CreateCup.css';
import './HomePage.css';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';


const CreateCup= () => {
  const [cupName, setCupName] = useState('');
  const [numTeams, setNumTeams] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [details, setDetails] = useState('');

 const url = 'http://127.0.0.1:5000/competition';
 const nav = useNavigate();

  function handleSubmit(e) {
    e.preventDefault();
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: cupName,
        num_teams: numTeams,
        start_date: startDate,
        end_date: endDate,
        details: details,
      }),
    })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
      }
      )
      .catch((error) => {
        console.error('Error:', error);
      }
      );
      
      nav('/');
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name of Cup:
        <input type="text" value={cupName} onChange={e => setCupName(e.target.value)} />
      </label>
      <label>
        Number of Teams:
        <input type="number" min={0} value={numTeams} onChange={e => setNumTeams(e.target.value)} />
      </label>
      <label>
        Start Date:
        <input type="date" value={startDate} onChange={e => setStartDate(e.target.value)} />
      </label>
      <label>
        End Date:
        <input type="date" value={endDate} onChange={e => setEndDate(e.target.value)} />
      </label>
      <label>
        Details:
        <textarea value={details} onChange={e => setDetails(e.target.value)} />
      </label>
      <button type="submit" class = "button">Create CUP</button>
    </form>
  );
};

export default CreateCup;