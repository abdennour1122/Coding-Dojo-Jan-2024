import { useState } from 'react';
import React from 'react'


const Tasks = ({ tasks, setTask }) => {
    const [title, setTitle] = useState("");
    const [status, setStatus] = useState("");

    const submit = (e) => {
        e.preventDefault();
        const newTask = {
            title,
            status,
        };

        setTask([...tasks, newTask]);
        setTitle("");
        setStatus("");
    };

    return (

        <div>
            <div>
                <h1 >To-Do List</h1>
            </div>
            <form onSubmit={submit} >
                <div>
                    <input onChange={(e) => { setTitle(e.target.value) }} value={title} type="text" placeholder="Add a task" />
                    <button type="submit">Add</button>
                </div>
            </form>
        </div>

    )
}

export default Tasks;