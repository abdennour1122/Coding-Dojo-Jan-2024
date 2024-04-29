import React ,{useState} from 'react'
import './Display.css'

const Display = ({col}) => {
    
    console.log(col)
    return (<div className='box' style={{backgroundColor:col}}><p>{col}</p></div> )
}

export default Display