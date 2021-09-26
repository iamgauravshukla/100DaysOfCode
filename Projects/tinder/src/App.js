import "./App.css";
import { Header } from "./components/Header";
import Messages from "./components/Messages";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { TinderCards } from "./components/TinderCards";
import Chats from "./components/Chats";
import Buttons from "./components/Buttons";

function App() {
  return (
    <div className="appp">
      <Router>
        <Switch>
          <Route path="/chat/:person">
            <Header backButton="/chat" />
            <Messages/>
          </Route>
          <Route path="/chat">
            <Header backButton="/" />
            <Chats />
          </Route>
          <Route path="/">
            <Header />
            <TinderCards />
            <Buttons />
          </Route>
        </Switch>
      </Router>
    </div>

  );
}

export default App;
