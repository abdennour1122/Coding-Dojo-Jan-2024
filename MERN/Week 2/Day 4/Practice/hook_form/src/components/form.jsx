import React, { useState } from 'react';

const UserForm = (props) => {
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [CPass, setCPass] = useState("");




    return (
        <div className='container mt-3 '>
            <form className='mt-3'>
                <div className=' g-3 box col-4 p-2 ' >
                    <div className='col-auto'>
                        <label className='col-form-label'>First Name: </label>
                    </div>
                    <div className='col-auto'>
                        <input type="text" className='form-control' onChange={(e) => setFirstName(e.target.value)} />
                    </div>
                </div>
                <br />
                <div className='row g-3 align-items-center box'>
                    <div className='col-auto'>
                        <label className='col-form-label'>Last Name: </label>
                    </div>
                    <div className='col-auto'>
                        <input type="text" className='form-control' onChange={(e) => setLastName(e.target.value)} />
                    </div>
                </div>
                <br />
                <div className='row g-3 align-items-center box'>
                    <div className='col-auto'>
                        <label className='col-form-label'>Email Address : </label>
                    </div>
                    <div className='col-auto'>
                        <input type="text" className='form-control' onChange={(e) => setEmail(e.target.value)} />
                    </div>
                </div>
                <br />
                <div className='row g-3 align-items-center box'>
                    <div className='col-auto'>
                        <label className='col-form-label'>Password : </label>
                    </div>
                    <div className='col-auto'>
                        <input type="text" className='form-control' onChange={(e) => setPassword(e.target.value)} />
                    </div>
                </div>
                <br />
                <div className='row g-3 align-items-center box'>
                    <div className='col-auto'>
                        <label className='col-form-label'>Confirm Password : </label>
                    </div>
                    <div className='col-auto'>
                        <input type="text" className='form-control' onChange={(e) => setCPass(e.target.value)} />
                    </div>
                </div>
                <br />
            </form>
            <div>
                <h5>Your Form Data</h5>
                <br />
                <p>First Name : {firstName} </p>
                <p>Last Name : {lastName} </p>
                <p>Email : {email} </p>
                <p>Password : {password} </p>
                <p>Confirm Password : {CPass} </p>
            </div>
        </div>
    );
};

export default UserForm;