import React, { useEffect } from "react";
import { useState } from "react";
import TinderCard from "react-tinder-card";
import database from "../firebase";
import "../tindercard.css";
export const TinderCards = () => {
  const [people, setPeople] = useState([]);

  //Push to an array
  // setPeople([...people, 'Gaurav','Shukla'])


//   Piece of a code runs on based of a condition
  useEffect(()=>{
      const unsubscribe =   database.collection('people').onSnapshot((snapshot) =>(
            setPeople(snapshot.docs.map(doc=> doc.data()))
        ));
        
        return ()=>{
            //cleanup
            unsubscribe();
        }

  }, []);
  
  return (
    <div>
      <div className="card_container">
        {people.map((person) => (
          <TinderCard
            className="swipe"
            key={person.name}
            preventSwipe={["up", "down"]}
          >
            <div
              className="cards"
              style={{ backgroundImage: `url(${person.url})` }}
            >
              <h3>{person.name}</h3>
              <h3 className="age">{person.age}yrs</h3>
            </div>
          </TinderCard>
        ))}
      </div>
    </div>
  );
};
