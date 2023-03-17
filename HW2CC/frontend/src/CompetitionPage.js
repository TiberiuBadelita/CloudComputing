import React from "react";
import { useState, useEffect, useRef } from "react";
import { useParams } from "react-router-dom";
import './HomePage.css';
import './CompetitionPage.css';

const CompetitionPage = () => {
    const { id } = useParams();
    const [competitions, setCompetitions] = useState([]);
    const [teams, setTeams] = useState([]);
    const [formData, setFormData] = useState({
        team_id: "",
        competition_id: id,
    });
    const formRef = useRef(null);
    const url = 'http://127.0.0.1:5000/competitions';
    useEffect(() => {
        fetch(url)
          .then(response => response.json())
          .then(data => {setCompetitions(data.competitions);});
      }, []);
    const url_teams = 'http://127.0.0.1:5000/teams';
    useEffect(() => {
        fetch(url_teams)
            .then(response => response.json())
            .then(data => setTeams(data.teams));
    }, []);

    const [showForm, setShowForm] = useState(false);

    function handleButtonClick(e) {
        e.stopPropagation();
        setShowForm(true);
    }

    function handleSubmit(e) {
        console.log(formData);
        e.preventDefault();
        const newJunction = {
            team_id: formData.team_id,
            cup_id: formData.competition_id,
        }

        const url_post = 'http://127.0.0.1:5000/junction';

        fetch(url_post, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(newJunction),
        })
        .then((response) => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error("Error:", error);
        });

        window.location.reload(false);
    }

    function handleGenerateCup(e) {
        
        e.preventDefault();
        const url_generate = 'http://127.0.0.1:5000/generate';
        const newGeneration = {
            cup_id: formData.competition_id,
            generated: 1,
        }   
        fetch(url_generate, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(newGeneration),
        })
        .then((response) => response.json())
    }

    useEffect(() => {
        function handleOutsideClick(event) {
          if (formRef.current && !formRef.current.contains(event.target)) {
            setShowForm(false);
          }
        }
    
        document.addEventListener('click', handleOutsideClick);
    
        return () => {
          document.removeEventListener('click', handleOutsideClick);
        };
      }, [formRef]);


      const [junctionData, setJunctionData] = useState([]);

      const url_junction = 'http://127.0.0.1:5000/junctions';
        useEffect(() => {
            fetch(url_junction)
                .then(response => response.json())
                .then(data => setJunctionData(data.junctions));
        }, []);

        const junctionDataUpdated = junctionData.filter((junction) => junction.cup_id === parseInt(id));

        const teamsUpdated = teams.filter((team) => !junctionDataUpdated.map((junction) => junction.team_id).includes(team.id));
        
        const [groupData, setGroupData] = useState([]);

        const url_groups = 'http://127.0.0.1:5000/groups';

        useEffect(() => {
            fetch(url_groups)
                .then(response => response.json())
                .then(data => setGroupData(data.groups));
        }, []);
    
        const[scores, setScores] = useState({
            team1:'',
            team2:'',
            score1:0,
            score2:0,
        });

        function handleScore(e) {
           const url_sms='http://localhost:5000/sms';
           const message = 'Game between '+ scores.team1 +' and '+ scores.team2 + ' ended! With a score of ' + scores.score1 + ' - ' + scores.score2 + '!';
              const newMessage = {
                message: message,
              }
                fetch(url_sms, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(newMessage),
                })
                .then((response) => response.json())
                .then(data => console.log(data))
        }
    
    return (
        <div>
            {showForm && (
                <div class="form-container" >
                    <form class="form" ref={formRef} onSubmit={handleSubmit}>
                    <label for="teams">Choose a team to register:</label>
                    <select name="teams" id="teams" onChange={(e) => setFormData({...formData, team_id: e.target.value})}>
                            {teamsUpdated.map((team) => (
                                <option value={team.id}>{team.name}</option>
                            ))}
                    </select>
                    <button type="submit">Register</button>
                    </form>
                </div>
            )}
            {competitions.map((competition) =>(
                competition.cup_generated === 0 ? (
                <div key={competition.id}>
                    <h1>{competition.name}</h1>
                    <p>Competition Start Date: {competition.start_date}</p>
                    <p>Competition End Date: {competition.end_date}</p>
                    <p>Competition Details: {competition.details}</p>
                    <h2>Number of available spots : {competition.number_of_teams - junctionDataUpdated.length}</h2>
                    <h3>Registered teams:</h3>
                  
                        {junctionDataUpdated.map((junction) => (
                           <div key={junction.cup_id}>
                         <ul>
                        {teams.map((team) => (
                            <li key={team.id}>{team.name}</li>
                        )).filter((team) => parseInt(team.key) === parseInt(junction.team_id))}
                         </ul>
                            </div>
                        ))}
                        <div class="buttonView">
                          <button type = "button" class="button" onClick={handleButtonClick}>Register team</button>
                          <button type = "button" class="button" onClick={(e) => {if (junctionDataUpdated.length > 3) {handleGenerateCup(e);} else {alert("Must be at least 4 teams registered!");}}}>Generate Cup</button>
                        </div>
                </div>
            ) : (
                <div key={competition.id}>
                    <h1>{competition.name}</h1>
                    <p>Competition Start Date: {competition.start_date}</p>
                    <p>Competition End Date: {competition.end_date}</p>
                    <p>Competition Details: {competition.details}</p>
                    <h2>Groups:</h2>      
                        {groupData.map((group,index) => (
                                <div key={group.cup_id}  className={index % 4 === 1 ? 'rowView' : ''}>
                                    {index % 4 === 0 && <h3>Group {group.group_name}</h3>}
                                    <p>{group.team_name}</p>
                                </div>
                            )).filter((group) => parseInt(group.key) === parseInt(competition.id))
                        }
                    <h2>Matches:</h2>
                    {groupData.map((group) => (
                        groupData.map((group2) => (
                            <div key={group2.cup_id} > 
                                {group.group_name === group2.group_name && group.team_name !== group2.team_name 
                                && <p>
                                {group.team_name} 
                                <input type="number"onChange={(e) => setScores({ ...scores, score1: e.target.value, team1:group.team_name })}></input> 
                                vs <input type="number" onChange={(e) => setScores({ ...scores, score2: e.target.value , team2:group2.team_name})}></input> {group2.team_name}
                                <button type="button" class="buttonScore" onClick={handleScore}>SET SCORE</button>
                                </p>}
                                </div>
                            )).filter((group2) => parseInt(group2.key) === parseInt(competition.id))
                        ))}
                </div>
            )
        )).filter((competition)=>parseInt(competition.key) === parseInt(id))}
            
        </div>
    );
}

export default CompetitionPage;