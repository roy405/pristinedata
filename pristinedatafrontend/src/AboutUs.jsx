import React from 'react';
import NavBar from './NavBar';

const AboutUs = () => {
    return (
        <div className="container mx-auto p-4 bg-white shadow rounded-lg mt-8">
            <h2 className="text-2xl font-bold text-gray-800 mb-4">About Us</h2>
            <p className="text-lg text-gray-700 mb-4">
                At PristineData, we are dedicated to providing the highest quality data cleaning services. 
                Our platform focuses on preparing data for analysis, ensuring it is clean, structured, and ready 
                for use in AI training and other data-driven applications. With our advanced algorithms and user-friendly interface, we make data 
                cleaning accessible to data scientists, analysts, and anyone looking to work with impeccably clean datasets. Join us in our mission to make data more reliable
                 and analysis more insightful.
            </p>
            <p className="text-lg text-gray-700">
                Whether you're tackling large datasets or fine-tuning data for precise models, 
                PristineData is your partner in data preparation. Our commitment to excellence and innovation drives us to continuously improve our services, 
                providing you with the best tools to clean and prepare your data for the challenges ahead.
            </p>
        </div>

    );
};

export default AboutUs;