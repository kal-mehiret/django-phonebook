Django Phonebook
A simple and efficient contact management application built with Django.

Features:
   Create, Read, Update, and Delete contacts
    Search and filter contacts
   Contact categorization
   Responsive Bootstrap interface
   Django admin integration

Installation:
1. Clone the repository

git clone https://github.com/kal-mehiret/django-phonebook.git
cd django-phonebook

2. Create and activate virtual environment

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run migrations

python manage.py migrate

5. Create superuser (optional)

python manage.py createsuperuser

6. Run development server

python manage.py runserver
Visit http://127.0.0.1:8000

