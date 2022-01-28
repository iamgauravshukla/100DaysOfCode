import React, { useState } from 'react';
import { useRef } from 'react';
import './register.scss';
export default function Register() {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');

    const emailRef = useRef();
    const passRef = useRef();

    const handelStart = ()=>{
        setEmail(emailRef.current.value);
    }

    const handelFinish = ()=>{
        setPass(passRef.current.value);
    }
  return (
  <div className='register'>
      <div className="top">
          <div className="wrapper">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" className='logo' alt="" />
            <button className="loginButton">Sign In</button>
          </div>
      </div>
      <div className="container">
          <h1>Unlimited movies, TV Shows, and more.</h1>
          <h2>Watch anywhere. Cancel Anytime</h2>
          <p>Ready to watch? enter your email to create or restart your membership</p>
          {
              !email ? (
                    <div className="input">
                        <input type="email" placeholder='email address' ref={emailRef}/>
                        <button className="registerButton" onClick={handelStart}>Get Started</button>
                    </div>
              ):
              (
                <form className="input">
                    <input type="password" placeholder='password' ref={passRef}/>
                    <button className="registerButton" onClick={handelFinish}>Start Membership</button>
                </form>
              )
          }
      </div>
  </div>
  )
}
