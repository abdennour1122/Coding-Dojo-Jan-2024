import logo from './logo.svg';
import './App.css';
import PersonCard from './component/PersonCard';

const peopleArr = [
  {"firstName":"Jane", "lastName":"Doe", "age":45, "hairColor":"Black"},
  {"firstName":"John", "lastName":"Smith","age":88,"hairColor":"Brown"},
  {"firstName":"Millard", "lastName":"Fillmore","age":50,"hairColor":"Brown"},
  {"firstName":"Maria", "lastName":"Smith","age":62,"hairColor":"Brown"}
];

function App() {
  return (
    <div className="App">
      {peopleArr.map((person, index) => (
        <PersonCard
          key={index}
          firstName={person.firstName}
          lastName={person.lastName}
          age={person.age}
          hairColor={person.hairColor}
        />
      ))}
    </div>
  );
}


export default App;
