import firebase from 'firebase/compat/app';
import "firebase/compat/auth";
import "firebase/compat/firestore";

// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDxC9vy3HuJKUXTzXwm3xKdVaRVN0lWzws",
  authDomain: "tinderclone-d358c.firebaseapp.com",
  databaseURL: "https://tinderclone-d358c-default-rtdb.firebaseio.com",
  projectId: "tinderclone-d358c",
  storageBucket: "tinderclone-d358c.appspot.com",
  messagingSenderId: "625391326754",
  appId: "1:625391326754:web:e24b935c3d0be197329c7b",
  measurementId: "G-936XF6NZTJ"
};

  const firebaseApp = firebase.initializeApp(firebaseConfig);
  const database = firebaseApp.firestore();

  export default database