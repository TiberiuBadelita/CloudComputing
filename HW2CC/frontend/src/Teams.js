import React from "react";
import { useState } from "react";
import "./Teams.css";
import "./HomePage.css";

const Teams = () => {
    const teams = [
        {
            id: "01",
            name: "FC Barcelona",
            founded: "29/11/1899",
            stadium: "Camp Nou",

        },
        {
            id: "02",
            name: "Real Madrid",
            founded: "06/03/1902",
            stadium:"Santiago Bernabeu",
        },
        {
            id: "01",
            name: "FC Barcelona",
            founded: "29/11/1899",
            stadium: "Camp Nou",

        },
        {
            id: "02",
            name: "Real Madrid",
            founded: "06/03/1902",
            stadium:"Santiago Bernabeu",
        },
        {
            id: "01",
            name: "FC Barcelona",
            founded: "29/11/1899",
            stadium: "Camp Nou",

        },
        {
            id: "02",
            name: "Real Madrid",
            founded: "06/03/1902",
            stadium:"Santiago Bernabeu",
        },
        {
            id: "01",
            name: "FC Barcelona",
            founded: "29/11/1899",
            stadium: "Camp Nou",

        },
        {
            id: "02",
            name: "Real Madrid",
            founded: "06/03/1902",
            stadium:"Santiago Bernabeu",
        },
        {
            id: "01",
            name: "FC Barcelona",
            founded: "29/11/1899",
            stadium: "Camp Nou",

        },
        {
            id: "02",
            name: "Real Madrid",
            founded: "06/03/1902",
            stadium:"Santiago Bernabeu",
        },
        {
            id: "01",
            name: "FC Barcelona",
            founded: "29/11/1899",
            stadium: "Camp Nou",

        },
        {
            id: "02",
            name: "Real Madrid",
            founded: "06/03/1902",
            stadium:"Santiago Bernabeu",
        },
        {
            id: "01",
            name: "FC Barcelona",
            founded: "29/11/1899",
            stadium: "Camp Nou",

        },
        {
            id: "02",
            name: "Real Madrid",
            founded: "06/03/1902",
            stadium:"Santiago Bernabeu",
        },
        {
            id: "01",
            name: "FC Barcelona",
            founded: "29/11/1899",
            stadium: "Camp Nou",

        },
        {
            id: "02",
            name: "Real Madrid",
            founded: "06/03/1902",
            stadium:"Santiago Bernabeu",
        },
        
    ];

    const [showForm, setShowForm] = useState(false);

    function handleButtonClick() {
        setShowForm(!showForm);
    }

    return (
        <ul>
             {showForm && (
                <div class="form-container">
                    <form class = "form" >
                    <label htmlFor="name">Name:</label>
                    <input type="text" id="name" name="name" />
                    
                    <label htmlFor="founded">Founded:</label>
                    <input type="text" id="founded" name="founded" />
                    
                    <label htmlFor="stadium">Stadium:</label>
                    <input type="text" id="stadium" name="stadium" />
                    
                    <button type="submit">ADD</button>
                    </form>
                </div>
            )}
            {teams.map((data) => (
                <li key={data.id}>
                    <p> || {data.name} || </p>
                    <p>Founded: {data.founded}</p>
                    <p>Stadium: {data.stadium}</p>
                </li>
            ))}

            <div>
            <button onClick={handleButtonClick} class="button">ADD TEAM</button>
            </div>
        </ul>
    );
}

export default Teams;
