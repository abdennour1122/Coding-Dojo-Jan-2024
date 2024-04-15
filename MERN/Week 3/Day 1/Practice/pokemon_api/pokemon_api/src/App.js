import './App.css';
import { useState } from 'react';
function App() {
  const [pokemon,setPokemon]= useState([])
  async function Fetchpokemon() {
  const res= (await fetch("https://pokeapi.co/api/v2/pokemon"))
  const temp=await res.json()
  setPokemon(temp.results)
  // pokemon.map(p=>console.log(p.name))
  console.log(pokemon);
}
  //  new Fetchpokemon( (resolve, reject)) => {
  //   .then(response => {
  //     // not the actual JSON response body but the entire HTTP response
  //     console.log(response);
  //     return response.json();
  // })
  // .then(response => {
  //     // we now run another promise to parse the HTTP response into usable JSON
  //     console.log(response);
  //     setPokemon(response)
  //     console.log(pokemon);
  // }).catch(err=>{
  //     console.log(err);
  // });
  return (
    
    <div className="App">
      <h1>all pokemons</h1>
      <button onClick={Fetchpokemon}>Fetch Pokemon</button>
      <ul>
      {pokemon.map(p=><li>{p.name}</li>)}
        
      </ul>
    </div>
  );
}

export default App;
