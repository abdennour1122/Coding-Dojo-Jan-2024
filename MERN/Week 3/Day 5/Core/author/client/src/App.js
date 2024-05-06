import './App.css';
import { Route, Routes } from 'react-router-dom';
import Authors from './components/Authors';
import Create from './components/Create';
import Edit from './components/Edit';
import Show from './components/Show';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
function App() {
  return (
    <div className="container">
      <Routes>

        <Route path='/' element={<Authors />} />

        <Route path='/new' element={<Create />} />

        <Route path='/update/:id' element={<Edit />} />
        
        <Route path='/c/:id' element={<Show />} />
      </Routes>
    </div>
  );
}

export default App;