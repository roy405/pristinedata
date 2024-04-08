import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from 'react-router-dom';
import FileUpload from './FileUpload';
import ProcessedDataDisplay from './ProcessedDataDisplay';
import NavBar from './NavBar'; // Import NavBar
import AboutUs from './AboutUs';
import ContactUs from './ContactUs';
import './App.css'

function App() {
  return (
    <Router>
      <NavBar /> {/* Include NavBar */}
      <Routes>
        <Route path="/" element={<FileUpload />} />
        <Route path="/processed-data" element={<ProcessedDataDisplay />} />
        <Route path="/about" element={<AboutUs />} />
        <Route path="/contact" element={<ContactUs />} />
      </Routes>
    </Router>
  );
}

export default App

