# Pristine Data
## Overview
Pristine Data is a Django-based project designed to streamline the process of cleaning and processing data files. At its core is the "Data Cleanser" app, a powerful tool for handling CSV and Excel files, ensuring data is pristine, organized, and ready for analysis or further processing.

This project leverages the robustness of Django and the Django REST Framework for backend operations, alongside Pandas for efficient data manipulation. Whether you're dealing with small datasets or large volumes of data, Pristine Data offers a scalable solution to cleanse and prepare your data.

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
