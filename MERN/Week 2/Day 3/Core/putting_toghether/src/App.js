import './App.css';
import PersonCard from './Components/person';

function App() {
  const people = [{firstname:"Jane", lastname:"Doe", age:45, haircolor:"Black"},
    {firstname:"Smith", lastname:"Maria", age:88, haircolor:"Brown"}];
  return (
    <div className="App">
      {people.map((person,index)=><PersonCard key={index} person={person}/>)}
    </div>
  );
}
export default App;
