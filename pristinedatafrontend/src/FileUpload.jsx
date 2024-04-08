import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate hook
import NavBar from './NavBar';

function FileUpload() {
    const [file, setFile] = useState(null);
    const navigate = useNavigate();

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (!file) {
            alert('Please select a file first!');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('http://127.0.0.1:8000/api/upload/', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error('Something went wrong with the file upload.');
            }

            const result = await response.json();
            navigate('/processed-data', { state: { processedData: result } });
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to upload the file.');
        }
    };

    return (
        <div className="container mx-auto p-4 bg-theme-light shadow rounded-lg mt-8">
            <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                    <label htmlFor="file" className="block text-lg font-medium text-theme">Upload file</label>
                    <input type="file" name="file" id="file" onChange={handleFileChange}
                        className="mt-1 block w-full border-2 border-theme rounded-lg py-2 px-3 text-lg text-theme leading-tight focus:outline-none focus:bg-white" />
                </div>
                <button type="submit" className="px-6 py-3 bg-theme hover:bg-theme-dark text-white rounded transform transition hover:scale-105 duration-300 ease-in-out">
                    Process File
                </button>
            </form>
        </div>
    );
}

export default FileUpload;
