import React, { useState } from 'react';
import './Navbar.css';

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  function toggleMenu() {
    setIsOpen(!isOpen);
  }

  return (
    <nav className={isOpen ? 'navbar open' : 'navbar'}>
      <div className="logo">
        <a href={'/'}><img src={process.env.PUBLIC_URL+"logo.png"} width="15%" alt="logo"/></a>
      </div>
      <ul className="nav-links">
        <li><a href={'/'}>Home</a></li>
        <li><a href={'/create-cup'}>Create CUP</a></li>
        <li><a href={'/teams'}>Teams</a></li>
      </ul>
      <div className="hamburger" onClick={toggleMenu}>
        <div className="line"></div>
        <div className="line"></div>
        <div className="line"></div>
      </div>
    </nav>
  );
}

export default Navbar;