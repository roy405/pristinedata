import React from 'react';
import NavBar from './NavBar';

const ContactUs = () => {
    return (
        <div className="container mx-auto p-4 bg-white shadow rounded-lg mt-8">
            <h2 className="text-2xl font-bold text-gray-800 mb-4">Contact Us</h2>
            <div className="mb-4">
                <p className="text-lg text-gray-700">
                    We'd love to hear from you! Whether you have a question about our services, need assistance with our platform, or just want 
                    to give us some feedback, please don't hesitate to reach out.
                </p>
            </div>
            <div>
                <p className="text-lg font-semibold text-gray-800">Email Us:</p>
                <p className="text-lg text-blue-600">Support Email</p>
            </div>
            <div className="mt-4">
                <p className="text-lg font-semibold text-gray-800">Follow Us:</p>
                <p className="text-lg text-blue-600">Twitter Page</p>
            </div>
        </div>
    );
};

export default ContactUs;