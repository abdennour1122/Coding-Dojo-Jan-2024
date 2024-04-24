import React from 'react'
import { useParams , useState} from "react-router-dom"; 

function Color() {
    const {param,tcol,bgcol} = useParams();
    const style={
        color:tcol,
        backgroundColor:bgcol,
        padding: '10 px',
    }
  return (
    <div style={style}><h1> the word is:{param} </h1> </div>
  )
}

export default Color