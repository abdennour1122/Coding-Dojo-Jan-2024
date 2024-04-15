import axios from 'axios';
import './App.css';
import { useState } from 'react';

function App() {
  const [pokemon,setPokemon]= useState([])
  const axiospokemon = () => {     
    axios.get("https://pokeapi.co/api/v2/pokemon")       
    .then((res) => {         
      //! -- axios wraps the res in it's own .data key         
      console.log(res.data)         
      setPokemon(res.data.results) // we know from the prev console log that this IS an Array of Data 
    })
      .catch((err) => {         
        console.log("❌❌❌❌❌❌", err)       }) }

  return (
    <div className="App">
        <h1>all pokemon</h1>
        <button onClick={axiospokemon}>Axios Heroes</button>
        <ul>      {pokemon.map(p=><li>{p.name}</li>)}
</ul>
    </div>
  );
}

export default App;
