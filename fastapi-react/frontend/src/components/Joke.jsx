import React, { useEffect, useState, forwardRef, useImperativeHandle } from 'react';

// Forward the ref to use the fetchJoke function from outside
const Joke = forwardRef((props, ref) => {
  const [jokeData, setJokeData] = useState({ joke: '', gif_url: '' });

  // Function to fetch new joke data
  const fetchJoke = async () => {
    try {
      const response = await fetch("http://localhost:8000");
      const data = await response.json();
      setJokeData(data); // Set the new joke and GIF data
    } catch (error) {
      console.error('Error fetching joke:', error);
    }
  };

  // Expose the fetchJoke method to the parent component via the ref
  useImperativeHandle(ref, () => ({
    fetchJoke,
  }));

  useEffect(() => {
    fetchJoke(); // Fetch a joke when the component mounts
  }, []);

  return (
    <div>
      <h3>{jokeData.joke}</h3>
      {jokeData.gif_url && <img src={jokeData.gif_url} alt="Related GIF" />}
    </div>
  );
});

// Assign display name to prevent ESLint warning
Joke.displayName = 'Joke';

export default Joke;
