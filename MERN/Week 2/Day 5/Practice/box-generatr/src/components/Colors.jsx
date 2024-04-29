import React, { useState } from 'react';
import Display from './Display'
import './Colors.css'

const Color = () => {

const [colors, setColors] = useState([]);
const [color,setColor]=useState("");

const add = (event) => {
        event.preventDefault() 
        setColors([...colors,color])
        setColor("")
    };
    return (
    <>
    <fieldset>
    <legend>Form</legend>
        <form onSubmit={(event) => add(event)}>
            <label>Color </label>
            <input type="text" value={color} onChange={ (e) => setColor(e.target.value )} />
            <button> Add </button>
        </form>
    </fieldset>
    <fieldset className='box-container' >
        <legend>Box View</legend>
        {colors.map((col,idx) => <Display key={idx} col={col}/> )}
    </fieldset>
    </>
    
    )
}

export default Color