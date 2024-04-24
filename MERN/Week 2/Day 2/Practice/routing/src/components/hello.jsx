import React from 'react'
import { useParams , useState} from "react-router-dom"; 

function Hello() {
    const {param} = useParams()
  return (
    <div>{isNaN (param) ? (<h1>the word is :{param}</h1>) : (<h1>the number is :{param} </h1>)}</div>
  )
}

export default Hello