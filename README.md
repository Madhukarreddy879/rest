# Student CRUD REST API

This is a Django REST API project for managing student records. It provides endpoints for performing CRUD operations on student data.

## Features

- Add a new student
- Get all students
- Get a student by ID
- Update existing student information
- Delete a student record

## Technologies Used

- Django
- Django Rest Framework
- PostgreSQL

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/student-crud-api.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up PostgreSQL database:
   
   - Create a PostgreSQL database.
   - Configure the database settings in `settings.py`.

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the API at `http://127.0.0.1:8000/api/`.

## API Endpoints

- **GET /api/students/**: Get all students
- **POST /api/students/**: Create a new student
- **GET /api/students/<student_id>/**: Get a student by ID
- **PUT /api/students/<student_id>/**: Update a student
- **DELETE /api/students/<student_id>/**: Delete a student

## Testing

To run the tests, execute the following command:

```bash
python manage.py test student_api.tests.test_student_api
