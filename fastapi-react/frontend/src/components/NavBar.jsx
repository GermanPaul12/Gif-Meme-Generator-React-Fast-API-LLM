import React from 'react';

export default function NavBar({ fetchJoke }) {
  return (
    <nav className="navbar">
      <button className="nav-button" onClick={fetchJoke}> {/* Trigger the fetch function */}
        Generate new Meme
      </button>
      <a
        href="https://github.com/GermanPaul12"
        target="_blank"
        rel="noopener noreferrer"
        className="nav-link"
      >
        GitHub Repo
      </a>
    </nav>
  );
}
