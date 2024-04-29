import { useState } from 'react'
import './App.css'
import Tabs from './components/Tabs'
import Display from './components/Display'

function App() {
  const [tabs, setTab] = useState(["Tab 1","Tab 2","Tab 3"])
  const [current, setCurrent] = useState("")

  return (
    < >
      <Tabs tabs={tabs} setCurrent={setCurrent}/>
      <Display current={current}/>
    </>
  )
}

export default App
