import React from 'react';
import { Link } from 'react-router-dom';

const NavBar = () => {
    return (
        <nav className="bg-theme-dark p-4">
            <div className="container mx-auto flex items-center justify-between">
                <div className="text-white">
                    <Link to="/" className="text-2xl font-bold flex items-center">
                        <img src="/src/assets/pristinedatalogo.png" alt="Logo" className="h-16 mr-2" /> PristineData
                    </Link>
                </div>
                <div>
                    <Link to="/about" className="text-white px-4 hover:text-theme-light">About Us</Link>
                    <Link to="/contact" className="text-white px-4 hover:text-theme-light">Contact Us</Link>
                </div>
            </div>
        </nav>
    );
};

export default NavBar;
