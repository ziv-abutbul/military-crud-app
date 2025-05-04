# ListOfSoldiers

## Overview
ListOfSoldiers is a web application designed to manage soldier information. It is built using Django for the back-end and Angular for the front-end. The application uses a MySQL database to store soldier data.

## Features
- Manage soldier details such as name, address, phone number, unit, role, and emergency contact information.
- Track service start and end dates.
- RESTful API for CRUD operations on soldier data.
- Angular-based front-end for a responsive user interface.

## Project Structure
```
ListOfSoldiers/
├── db.sqlite3
├── manage.py
├── Env/                # Virtual environment
├── front-end/          # Angular front-end
├── ListOfSoldiers/     # Django project settings
├── SoldierApp/         # Django app for soldier management
```

## Prerequisites
- Python 3.13
- Node.js and npm
- MySQL server

## Installation

### Back-end (Django)
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ListOfSoldiers
   ```
2. Activate the virtual environment:
   ```bash
   Env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the database in `ListOfSoldiers/settings.py`:
   ```python
   DATABASES = {
       'default': dj_database_url.parse('mysql://root:yourpassword@localhost:3306/sms')
   }
   ```
5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Front-end (Angular)
1. Navigate to the `front-end` directory:
   ```bash
   cd front-end
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the Angular development server:
   ```bash
   ng serve
   ```

## Usage
- Access the back-end API at `http://127.0.0.1:8000/`.
- Access the front-end application at `http://localhost:4200/`.

## Technologies Used
- **Back-end**: Django 4.2, Django REST Framework
- **Front-end**: Angular
- **Database**: MySQL

## License
This project is licensed under the MIT License.