import React from "react";
import { useState, useEffect, useRef} from "react";
import { useNavigate } from "react-router-dom";
import "./Teams.css";

const Teams = () => {
    const url = 'http://127.0.0.1:5000/teams';
    const formRef = useRef(null);
    const [teams, setTeams] = useState([]);
    useEffect(() => {
        fetch(url)
          .then(response => response.json())
          .then(data => setTeams(data.teams));
      }, []);
    
    console.log("Echipe:\n" + teams);

    const [showForm, setShowForm] = useState(false);
    const [formData, setFormData] = useState({
        name: "",
        founded: "",
        stadium: "",
      });

    function handleButtonClick(e) {
        e.stopPropagation();
        setShowForm(true);
    }

    function handleSubmit(e) {
        e.preventDefault();
        const newTeam = {
            name: formData.name,
            founded: formData.founded,
            stadium: formData.stadium,
        };

        console.log(newTeam);
        
        const url_post = 'http://127.0.0.1:5000/team';

        fetch(url_post, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(newTeam),
        })
        .then((response) => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error("Error:", error);
        });
        window.location.reload();
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

    function handleDelete(e,id) {
        e.preventDefault();
        const url_delete = 'http://localhost:5000/team/' + id;
        fetch(url_delete, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then((response) => {response.json();;window.location.reload();})
    }

      const navigate= useNavigate();
      
    return (
        <ul>
             {showForm && (
                <div class="form-container">
                    <form class = "form" ref={formRef} onSubmit={handleSubmit}>
                    <label htmlFor="name">Name:</label>
                    <input type="text" id="name" name="name"  value={formData.name} onChange={event => setFormData({...formData, name: event.target.value})}/>
                    
                    <label htmlFor="founded">Founded:</label>
                    <input type="text" id="founded" name="founded" value={formData.founded} onChange={event => setFormData({...formData, founded: event.target.value})}/>
                    
                    <label htmlFor="stadium">Stadium:</label>
                    <input type="text" id="stadium" name="stadium" value={formData.stadium} onChange={event => setFormData({...formData, stadium: event.target.value})} />
                    
                    <button type="submit">ADD</button>
                    </form>
                </div>
            )}
            {teams.map((data) => (
                <li key={data.id}>
                    <div class="divFlex">
                    <p> || {data.name} || </p>
                    <p>Founded: {data.founded}</p>
                    <p>Stadium: {data.stadium}</p>
                    </div>
                    <div class="divFlex">
                    <button class = "button2" onClick={() => navigate(`/team/${data.id}`)}>PLAYERS</button>
                    <button class = "button2" onClick={(e)=>handleDelete(e,data.id)}>DELETE</button>
                    </div>
                </li>
            ))}

            <div>
            <button onClick={handleButtonClick} class="button2">ADD TEAM</button>
            </div>
        </ul>
    );
}

export default Teams;
