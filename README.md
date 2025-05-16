````markdown
# TaskNest

TaskNest is a simple Django-based task management web application. It allows users to register, login, create, update, and delete their tasks with priorities, deadlines, and categories.

## Features

- User registration and login system
- Create, update, and delete tasks
- View a list of tasks with details like priority, deadline, and category
- Responsive and clean UI with animation and footer

## Technologies Used

- Django (Python web framework)
- HTML, CSS (with animations)
- Bootstrap (for styling)
- SQLite (default Django database)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ananyasahaanu/todolist.git
   cd tasknest
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   # Windows
   .\env\Scripts\activate
   # Linux/Mac
   source env/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and go to `http://127.0.0.1:8000/`

## Usage

* Register a new account or login with existing credentials.
* Add tasks with details.
* Edit or delete existing tasks.
* View your task list on the dashboard.

## Folder Structure

```
tasknest/
├── tasknest/          # Django project settings
├── tasks/             # Task app containing views, models, templates
├── templates/         # HTML templates
├── static/            # Static files (CSS, JS, images)
├── manage.py          # Django command-line utility
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## License

This project is licensed under the MIT License.

---

© 2025 Ananya Saha

```

