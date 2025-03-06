
## Student Model

The system stores the following information for each student:
- Student ID (Primary Key)
- First Name
- Last Name
- Email (Unique)
- Date of Birth
- Course
- Enrollment Date

## Setup and Installation

1. Clone the repository
```bash
git clone <repository-url>
```

2. Create and activate virtual environment
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. Install dependencies
```bash
pip install django
```

4. Apply migrations
```bash
python manage.py migrate
```

5. Run the development server
```bash
python manage.py runserver
```

## Usage

1. **View Students**: Navigate to the home page to see the list of all students
2. **Add Student**: Click on "Add New Student" and fill in the required information
3. **Edit Student**: Click on "Edit" next to any student to modify their information
4. **Delete Student**: Click on "Delete" next to any student to remove their record
5. **Search**: Use the search bar to find students by name or email
6. **Filter**: Use the course dropdown to filter students by course
7. **Sort**: Click on column headers to sort the student list

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details