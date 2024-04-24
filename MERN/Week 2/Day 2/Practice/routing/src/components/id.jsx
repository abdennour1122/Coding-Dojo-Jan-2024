import React from 'react'

import { useParams , useState} from "react-router"; 
function Id() {
    const id= useParams()
  return (
    <div>The number is: {id.num}</div>
  )
}
    
export default Id