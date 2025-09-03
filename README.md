# SW Blog Pots (Flask)

## 📄 Description
A flask web application to create, manage and delete social pots.


## 🙏 Acknowledgements

Special thanks to [@alexroel] for their excellent course and guidance.

## 🚀 Technologies Used

- Python
- Flask
- SQLite
- Jinja2
- Ckeditor

## ⚙️ How to run
🖥️
python -m venv env-todo
source env-todo/bin/activate  # Linux/Mac
env-todo\Scripts\activate     # Windows
pip install -r requirements.txt
python run.py

## 🌐 Demo
https://btopachu15.pythonanywhere.com/

## 📁 Folder Structure
sw-todo-list-app-flask/
├── env/
├── instance/
├── blogr/
	├── static/ 
	├── templates/ 
        ├── auth/
            ├── create.html
            ├── post.html
            ├── update.html
		├── auth/
			├── login.html
			├── register.html				
            ├── profile.html	
		├── base.html
		├── blog.html
        ├── index.html
	├── auth.py
	├── home.py
	├── models.py
    ├── posts.py
	├── __init__.py
├── .gitignore
├── README.md
├── config.py
├── requirements.txt
├── run.py
