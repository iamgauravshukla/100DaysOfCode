import './login.scss';
export default function Register() {
 
  return (
  <div className='login'>
      <div className="top">
          <div className="wrapper">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" className='logo' alt="" />
          </div>
      </div>
      <div className="container">
          <form action="">
              <h1>Sign In</h1>
              <input type="email" placeholder='email or phone number' />
              <input type="password" placeholder='password' />
              <button className='loginButton'>Sign In</button>
              <span>New to Netflix? <b>Sign up now.</b></span>
              <small>This page is protected by google reCAPTCHA to ensure you are not bot <b>Learn more</b></small>
         </form>         
      </div>
  </div>
  )
}
