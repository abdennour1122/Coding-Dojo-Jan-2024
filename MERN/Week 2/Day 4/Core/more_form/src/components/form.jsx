import React, { useState } from 'react';

const UserForm = (props) => {
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [CPass, setCPass] = useState("");

    return (
        <div className='container mt-3 '>
            <form className='mt-3 d-flex justify-content-center'>
                <div className='row g-3 box'>
                    <div className='col-auto'>
                        <label className='col-form-label'>First Name : </label>
                    </div>
                    <div className='col-auto'>
                        <input type="text" className='form-control' onChange={(e) => setFirstName(e.target.value)} />
                    </div>
                </div>
                        {firstName && firstName.length < 2 ? <p style={{ color: "red" }}>Firstname must be at least 2</p> : null}
                <br />
                <div className='row g-3 box'>
                    <div className='col-auto'>
                        <label className='col-form-label'>Last Name : </label>
                    </div>
                    <div className='col-auto'>
                        <input type="text" className='form-control' onChange={(e) => setLastName(e.target.value)} />
                    </div>
                </div>
                        {lastName && lastName.length < 2 ? <p style={{ color: "red" }}>Lastname must be at least 2</p> : null}
                <br />
                <div className='row g-3 box'>
                    <div className='col-auto'>
                        <label className='col-form-label'>Email Address : </label>
                    </div>
                    <div className='col-auto'>
                        <input type="text" className='form-control' onChange={(e) => setEmail(e.target.value)} />
                    </div>
                </div>
                        {email && email.length < 5 ? <p style={{ color: "red" }}>Email must be at least 5</p> : null}
                <br />
                <div className='row g-3 box'>
                    <div className='col-auto'>
                        <label className='col-form-label'>Password : </label>
                    </div>
                    <div className='col-auto'>
                        <input type="text" className='form-control' onChange={(e) => setPassword(e.target.value)} />
                    </div>
                </div>
                        {password && password.length < 8 ? <p style={{ color: "red" }}>Password must be at least 8 characters</p> : null}
                <br />
                <div className='row g-3 box'>
                    <div className='col-auto'>
                        <label className='col-form-label'>Confirm Password : </label>
                    </div>
                    <div className='col-auto'>
                        <input type="text" className='form-control' onChange={(e) => setCPass(e.target.value)} />
                    </div>
                </div>
                        {password && CPass && password !== CPass ? <p style={{ color: "red" }}>Passwords must match</p> : null}
                <br />
            </form>
        </div>
    );
};

export default UserForm;
