import React, { useRef } from 'react';
import Joke from './components/Joke';
import NavBar from './components/NavBar';

function App() {
  const jokeRef = useRef(null); // Create a ref for Joke component

  // Function to trigger fetchJoke from NavBar
  const fetchNewJoke = () => {
    if (jokeRef.current) {
      jokeRef.current.fetchJoke(); // Access fetchJoke via ref
    }
  };

  return (
    <div className="App">
      <NavBar fetchJoke={fetchNewJoke} /> {/* Pass fetch function to NavBar */}
      <Joke ref={jokeRef} /> {/* Attach ref to Joke component */}
    </div>
  );
}

export default App;
