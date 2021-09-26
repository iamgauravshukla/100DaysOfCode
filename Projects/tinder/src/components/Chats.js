import React from 'react'
import Chat from './Chat'
import '../chat.css'
function Chats() {
    return (
        <div className="chats">
            <Chat
            name = "Gaurav"
            message = "Hey there" 
            senttime = "30 second ago"
            profilepic = 'https://cdn.shopify.com/s/files/1/0162/2116/files/New_men_s_hairstyles_for_2019_3.jpg?v=1539325262'   
            />

            <Chat
            name = "Sarah"
            message = "Are you there?" 
            senttime = "5 minute ago"
            profilepic = 'https://image.freepik.com/free-photo/young-beautiful-woman-pink-warm-sweater-natural-look-smiling-portrait-isolated-long-hair_285396-896.jpg'   
            />

            <Chat
            name = "Sanidhya"
            message = "Let's meet" 
            senttime = "25 minute ago"
            profilepic = 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8aGFwcHklMjB3b21hbnxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80'   
            />

            <Chat
            name = "Jhon"
            message = "Okay" 
            senttime = "1 day ago"
            profilepic = 'https://media.istockphoto.com/photos/smiling-mixed-race-mature-man-on-grey-background-picture-id1319763895?b=1&k=20&m=1319763895&s=170667a&w=0&h=jhqKyg62cQVZ-NjDQjpcenCdHDrprkN4caRjk4K76E8='   
            />
            
            
        </div>
    )
}

export default Chats
