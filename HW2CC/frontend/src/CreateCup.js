import React from 'react';
import './CreateCup.css';
import './HomePage.css';
import { useState } from 'react';


const CreateCup= () => {
  const [cupName, setCupName] = useState('');
  const [numTeams, setNumTeams] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [details, setDetails] = useState('');

  function handleSubmit(e) {
    e.preventDefault();
    // handle form submission
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
      <button type="submit" class = "button">Generate CUP</button>
    </form>
  );
};

export default CreateCup;