import React from "react";
import { useParams } from "react-router-dom";

const CompetitionPage = () => {
    const { id } = useParams();
    const Competitions = [
        {
          id: '01',
          name: 'Cupa Nikodemus',
          data_inceput: '20/07/2023',
          data_final: '25/07/2023',
          details: 'Cupa este organizata de compania Nikodemus, in perioada 20-25 iulie 2023. Premiile sunt: 1. 4000 lei 2. 2500 lei 3. 1250 lei'
        },
        {
          id: '02',
          name: 'Cupa Vicov',
          data_inceput: '20/07/2023',
          data_final: '25/07/2023',
          details: 'Cupa este organizata de clubul de fotbal Vicov, in perioada 20-25 iulie 2023. Premiile sunt: 1. 4000 lei 2. 2500 lei 3. 1250 lei'
        },
      ];
    return (
        <div>
            <h1>{Competitions[id-1].name}</h1>
            <p>Competition Start Date: {Competitions[id-1].data_inceput}</p>
            <p>Competition End Date: {Competitions[id-1].data_final}</p>
            <p>Competition Details: {Competitions[id-1].details}</p>
        </div>
    );
}

export default CompetitionPage;