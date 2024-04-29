import React from "react";

const Display = ({ tasks, deleteTasks, readTasks }) => {
    //   const { tasks } = props;

    return (
        <div>
            <ul>
                {tasks.map((oneTask, index) => (
                    <li key={index}>
                        <div>
                            <input onChange={(e) => {readTasks(index);}}name="todo1"type="checkbox"checked={oneTask.status}/><label for="todo1" >
                                <span>{oneTask.title}</span>
                            </label>
                        </div>
                        <div>
                            <button onClick={(e) => deleteTasks(index)}type="button">Delete</button>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Display;