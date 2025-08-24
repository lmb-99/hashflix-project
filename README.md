# Hashflix
Built a full-stack Netflix-like streaming platform with Django, featuring user authentication, embedded video player, search bar, and content categorization.

# Frontend: 
- HTML
- CSS
- JavaScript
- Tailwind CSS
- Bootstrap5 (Django-Crispy-Forms)

# Backend:
- Python (Django)

# Database:
- SQLite

# About:

- The user can update their profile and change password.
- The view counts are counted dynamically.
- The highlight movie is the newest movie added
- Popular movies are sorted by their number of views
- New movies category is sorted by their creation date
- I changed the AbstractUser so the user could log in with the email instead of the username and also to add the 'Continue watching' category for each user
- I implemented my code with a front-end template, also doing some adjustments on the HTML and CSS as necessary


# How To Run The Project:
Open the project folder, open the command prompt in your terminal and run “python manage.py runserver”

Required libraries: 

- asgiref==3.9.0
- crispy-bootstrap5==2025.6
- Django==5.2.4
- django-crispy-forms==2.4
- gunicorn==23.0.0
- packaging==25.0
- pillow==11.3.0
- sqlparse==0.5.3
- tzdata==2025.2
