# SkillKart 🎓

SkillKart is a Django-based web application where users can submit their profile details like name, email, phone number, and skills. The data is saved to a database and a success page is shown after submission.

## 🔧 Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS (Bootstrap)  
- **Database:** SQLite (default)  
- **Deployment:** (optional) Render

## 🚀 Features

- Clean and responsive form  
- Form validation using Django  
- Stores user data in the database  
- Success page on form submission

## 🛠️ How to Run Locally

1. **Clone the Repo**

git clone https://github.com/GaneshMeesala7/skillkart.git
cd skillkart

2. **Create Virtual Environment**

python -m venv venv
# Activate:
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux


3. **Install Dependencies**

pip install -r requirements.txt


4. **Apply Migrations**

python manage.py migrate

5. **Run the Server**

python manage.py runserver

Open your browser and go to:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## 🗂️ Project Structure

skillkart/
├── manage.py
├── requirements.txt
├── Procfile
├── skillkart/  # Project settings
├── users/      # App: forms, views, models, templates


## 🌐 Deployment (Render - optional)

1. Create a Render Web Service
2. Add build command:
   `pip install -r requirements.txt`
3. Add start command:
   `gunicorn skillkart.wsgi:application`
4. Add environment variables:

   * `SECRET_KEY`
   * `DEBUG`
   * `ALLOWED_HOSTS`

## 👨‍💻 Author

**Ganesh Meesala**
GitHub: [GaneshMeesala7](https://github.com/GaneshMeesala7)


## ⭐ Star the Repo

If you like this project, please give it a ⭐ on GitHub!
