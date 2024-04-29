import React from 'react'

const Tabs = ({ tabs, setCurrent }) => {
    const clickHandler = (tab) => {
        setCurrent(tab)
    }
    return (
        <div>
            {tabs.map((tab, idx) => <button key={idx} onClick={() => clickHandler(tab)}>{tab}</button>)}
        </div>
    )
}

export default Tabs