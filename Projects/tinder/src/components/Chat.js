import React from "react";
import "../chat.css";
import { Avatar } from "@material-ui/core";
import { Link } from "react-router-dom";

function Chat({ name, message, senttime, profilepic }) {
  return (
    <Link to={`/chat/${name}`}>
      <div className="chat">
        <Avatar className="chat-pic" alt={name} src={profilepic}></Avatar>
        <div className="chat_container">
          <h2>{name}</h2>
          <p>{message}</p>
        </div>
        <p className="time">{senttime}</p>
      </div>
    </Link>
  );
}

export default Chat;
