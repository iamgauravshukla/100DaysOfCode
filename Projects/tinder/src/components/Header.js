import React from "react";
import "../header.css";
import AccountCircleIcon from "@material-ui/icons/AccountCircle";
import ChatBubbleIcon from "@material-ui/icons/ChatBubble";
import { IconButton } from "@material-ui/core";
import ArrowBackIosIcon from '@mui/icons-material/ArrowBackIos';
import { Link, useHistory } from "react-router-dom";

export const Header = ({backButton}) => {
  const history = useHistory();
  return (
    <div className="header">
      {backButton ? (
        <IconButton onClick= {()=>{ history.replace(backButton)}}>
          <ArrowBackIosIcon className="header_icon" fontSize="large"></ArrowBackIosIcon>
        </IconButton>
      ) : (
      <IconButton>
        <AccountCircleIcon className="header_icon" fontSize="large" />
      </IconButton>)
      }

      <Link to="/">
        <img className="logo" src="/logo.png" alt="" />
      </Link>

      <Link to="/chat">
        <IconButton>
          <ChatBubbleIcon className="header_icon" fontSize="large" />
        </IconButton>
      </Link>
    </div>
  );
};
