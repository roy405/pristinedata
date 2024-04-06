# Pristine Data
## Overview
Pristine Data is a Django-based project designed to streamline the process of cleaning and processing data files. At its core is the "Data Cleanser" app, a powerful tool for handling CSV and Excel files, ensuring data is pristine, organized, and ready for analysis or further processing.

This project leverages the robustness of Django and the Django REST Framework for backend operations, alongside Pandas for efficient data manipulation. Whether you're dealing with small datasets or large volumes of data, Pristine Data offers a scalable solution to cleanse and prepare your data.

## Functional Requirements for the System
The system is designed to process and clean data, making it suitable for analysis or further use in machine learning models. It supports various file formats, offers a user-friendly interface for uploading data, and applies a range of cleaning and conversion operations to prepare data for use. Below are the detailed functional requirements:

### File Upload:
Users can upload data files in .csv or .xlsx format.
The system validates the file format upon upload and rejects unsupported formats.

### Data Cleaning and Conversion:
- Automatically detect and convert column data types (e.g., numeric, boolean, datetime, complex numbers, text, and categories).
- Handle missing values, converting them to a uniform representation (e.g., NaN).
- Normalize date formats across the data set.
- Detect and convert boolean values represented as text (e.g., "True" to True).
- Process numeric data, differentiating between integers and floats.
- Identify and process complex numbers represented in text.

### Data Output:
Display the cleaned and converted data within the web interface for review.
Allow users to download the processed data in the original format (.csv or .xlsx).

### User Interface:
Provide a responsive web interface for file uploads and data display.
Support navigation between the upload page, processed data review page, an about us page, and a contact us page.

### Error Handling:
Display informative error messages for unsupported file formats or upload failures.
Provide feedback on data processing issues or conversion errors.

## Conversion Engine Flow-Chart:

![PristineData drawio](https://github.com/roy405/pristinedata/assets/25080286/5086bd08-6400-4d62-adbb-0b1a55070bcb)

## Technology Stack

### Backend:
- Django Rest Framework: Used for creating RESTful APIs to handle file uploads, data processing, and the provision of processed data to the front end.
- Python Pandas: Utilized for data manipulation and cleaning tasks, including detecting data types, handling missing values, and converting data formats.
- Python: Core programming language for server-side logic.

### Frontend:
- ReactJS: A JavaScript library for building the user interface, particularly for creating dynamic single-page applications.
- React Router: Manages navigation between different components of the web application, enabling a seamless user experience without page reloads.
- Tailwind CSS: A utility-first CSS framework for designing custom user interfaces with minimal effort.
- 
### Development Tools:
- Git: Version control system for tracking changes in the source code during development.
- GitHub: Hosts the project repository, facilitating code reviews, issue tracking, and collaboration between developers.

## System Diagram:
![Pythonman](https://github.com/roy405/pristinedata/assets/25080286/327fe619-d8b5-4421-97d1-34c644daada8)


## Getting Started
### Prerequisites
Before setting up the project, ensure you have the following installed on your system:

- Python (3.8 or later)
- pip (Python package installer)
- Virtualenv (for creating isolated Python environments)

### Backend Setup
1. Clone the Repository
   Start by cloning the Pristine Data repository to your local machine.

```bash
git clone https://github.com/your-username/pristine-data.git
cd pristine-data
```

2. Create and Activate a Virtual Environment
   Within the project directory, create a virtual environment and activate it.

   - Windows:
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
      
3. Install Dependencies
Install the required Python packages using pip.
   ```bash
      pip install -r requirements.txt
   ```
This command installs Django, Django REST Framework, Pandas, and any other necessary libraries.

## Configuration
Ensure your settings.py file within the Django project is correctly configured, especially the INSTALLED_APPS section, which must include:

```python
    INSTALLED_APPS = [
    ...
    'rest_framework',
    'data_cleanser',
    ...
    ]
```

## Running the Python/Django Backend
1. Apply Migrations
Before running the server for the first time, apply migrations to set up the database schema.

```bash
  python manage.py migrate

```
2. Start the Development Server
Run the Django development server.

```bash
python manage.py runserver
```

The server will start, typically accessible at *http://127.0.0.1:8000/*.

3. Accessing the Application
With the server running, you can access the Data Cleanser app through your web browser or API testing tools like Postman to upload and process data files.
