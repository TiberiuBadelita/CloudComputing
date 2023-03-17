import React from "react";
import './HomePage.css';
import './Teams.css';
import { useState, useEffect, useRef} from "react";
import { useParams } from "react-router-dom";

const TeamPage = () => {
    const { id } = useParams();
    const formRef = useRef(null);
    const url = 'http://127.0.0.1:5000/teams';
    const url_players = 'http://127.0.0.1:5000/team/' + id + '/players';
    const [teams, setTeams] = useState([]);
    useEffect(() => {
        fetch(url)
          .then(response => response.json())
          .then(data => setTeams(data.teams));
      }, []);

    const [players, setPlayers] = useState([]);
    useEffect(() => { 
        fetch(url_players)
            .then(response => response.json())
            .then(data => setPlayers(data.players));
    }, []);

    const [showForm, setShowForm] = useState(false);
    const [formData, setFormData] = useState({
        name: "",
        age: "",
        position: "",
        shirt_number: "",
      });

    function handleButtonClick(e) {
        e.stopPropagation();
        setShowForm(true);
    }

    function handleSubmit(e) {
        e.preventDefault();
        const newPlayer = {
            name: formData.name,
            age: formData.age,
            position: formData.position,
            shirt_number: formData.shirt_number,
        }

        const url_post = 'http://127.0.0.1:5000/team/' + id + '/player';

        fetch(url_post, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(newPlayer),
        })
        .then((response) => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error("Error:", error);
        });
        window.location.reload(false);
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


      function handleDelete(e,id,player_id) {
        e.preventDefault();
        const url_delete = 'http://localhost:5000/team/' + id + '/player/' + player_id;
        fetch(url_delete, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then((response) => {response.json();window.location.reload();})
       
        }

    const formRef2 = useRef(null);
    useEffect(() => {
        function handleOutsideClick(event) {
            if (formRef2.current && !formRef2.current.contains(event.target)) {
                setShowUpdateForm(false);
            }
        }

        document.addEventListener('click', handleOutsideClick);

        return () => {
            document.removeEventListener('click', handleOutsideClick);
        };
    }, [formRef2]);

    const [showUpdateForm, setShowUpdateForm] = useState(false);
    const [updateFormData, setUpdateFormData] = useState({
        id:"",
        name: "",
        age: "",
        position: "",
        shirt_number: "",
        });

    function handleUpdate(e,id) {
        e.stopPropagation();
        setShowUpdateForm(true);
        const player = players.filter((data) => data.id === id);
        
        setUpdateFormData({
            id: player[0].id,
            name: player[0].name,
            age: player[0].age,
            position: player[0].position,
            shirt_number: player[0].shirt_number,
        });

        console.log(updateFormData);
    }


    function handleSubmitUpdate(e) {
        e.preventDefault();
        const updatePlayer = {
            name: updateFormData.name,
            age: updateFormData.age,
            position: updateFormData.position,
            shirt_number: updateFormData.shirt_number,
        }
        const url_update = 'http://localhost:5000/team/' + id + '/player/' + updateFormData.id;
        fetch(url_update, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(updatePlayer),
        })
        .then((response) => {response.json();window.location.reload(false);})
        .then(data => console.log(data))
    }

    return (
        <div>
            {showForm && (
                <div class="form-container">
                    <form class = "form" ref={formRef} onSubmit={handleSubmit}>
                    <label htmlFor="name">Name:</label>
                    <input type="text" id="name" name="name"  value={formData.name} onChange={event => setFormData({...formData, name: event.target.value})}/>
                    
                    <label htmlFor="age">Age:</label>
                    <input type="text" id="age" name="age" value={formData.age} onChange={event => setFormData({...formData, age: event.target.value})}/>
                    
                    <label htmlFor="position">Position:</label>
                    <input type="text" id="position" name="position" value={formData.position} onChange={event => setFormData({...formData, position: event.target.value})} />
                    
                    <label htmlFor="shirt_number">Shirt number:</label>
                    <input type="text" id="shirt_number" name="shirt_number" value={formData.shirt_number} onChange={event => setFormData({...formData, shirt_number: event.target.value})} />

                    <button type="submit">ADD</button>
                    </form>
                </div>
            )}
             {showUpdateForm && (
                <div class="form-container">
                    <form class = "form" ref={formRef2} onSubmit={handleSubmitUpdate}>
                    <label htmlFor="name">Name:</label>
                    <input type="text" id="name" name="name"  value={updateFormData.name} onChange={event => setUpdateFormData({...updateFormData, name: event.target.value})}/>
                    
                    <label htmlFor="age">Age:</label>
                    <input type="text" id="age" name="age" value={updateFormData.age} onChange={event => setUpdateFormData({...updateFormData, age: event.target.value})}/>
                    
                    <label htmlFor="position">Position:</label>
                    <input type="text" id="position" name="position" value={updateFormData.position} onChange={event => setUpdateFormData({...updateFormData, position: event.target.value})} />
                    
                    <label htmlFor="shirt_number">Shirt number:</label>
                    <input type="text" id="shirt_number" name="shirt_number" value={updateFormData.shirt_number} onChange={event => setUpdateFormData({...updateFormData, shirt_number: event.target.value})} />

                    <button type="submit">Update</button>
                    </form>
                </div>
            )}
             {teams.map((data) => (
                <div key={data.id}>
                    <h1 align="center"> {data.name}  </h1>
                    <p align="center">Founded: {data.founded}</p>
                    <p align="center">Stadium: {data.stadium}</p>
                </div>
            )).filter((data) => data.key === id)}
             <ul>
                <h2>Players:</h2>
                {players.map((data) => (
                    <li key={data.team_id}>
                        <div class="divFlex">
                        <p> || {data.name} || </p>
                        <p>Age: {data.age}</p>
                        <p>Position: {data.position}</p>
                        <p>Shirt number: {data.shirt_number}</p>
                        </div>
                        <div class="divFlex">
                        <button type = "button" class="button2" onClick={(e)=>handleUpdate(e,data.id)}>UPDATE</button>
                        <button type = "button" class="button2" onClick={(e)=>handleDelete(e,data.team_id,data.id)}>DELETE</button>
                        </div>

                    </li>
                )).filter((data) => data.key === id)}
            </ul> 
            <button type = "button" class="button2" onClick={handleButtonClick}>Add players</button>
        </div>
    );
}

export default TeamPage;