import React from 'react'
import { useState } from 'react'
import "../message.css"
import { Avatar } from '@material-ui/core'
function Messages() {
    const [input, setInput] = useState('')
    const [messages, setMessages] = useState([
        {
            name: "Sanidhya",
            photo: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8aGFwcHklMjB3b21hbnxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80',
            message: 'Helloie'
        },
        {
            name: "Sanidhya",
            photo: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8aGFwcHklMjB3b21hbnxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80',
            message: 'All good..?'
        },

        {
            message: "How's You???"
        }

])

    const sendMessage = (e)=>{
        e.preventDefault();
        setMessages([...messages, {message: input}]);
        setInput('');

    }


    return (
        <div className="message-screen">
           <p className="matched">You matched with Sanidhya on 10-10-20</p>
           {messages.map((message) =>(
               (message.name ? (
                <div className="messages">
                <Avatar className="message-avatar" alt={message.name} src= {message.photo}/>
                <p className="message-text">
                    {message.message}
                </p>
                
            </div>
               ) : (
                <div className="user-messages">
                <p className="user-text">
                {message.message}
                </p>
                </div>
               ))
           ))}

              <form action="" className="new-message">
                   <input type="text" placeholder='Type a message...' className="chat-input"
                   value = {input}
                   onChange = {(e)=> setInput(e.target.value)} 
                   />
                   <button type='submit' className='send-message'
                   onClick= {sendMessage}>SEND</button>
               </form>

        </div>
    )
}

export default Messages
