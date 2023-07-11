@echo off
call D:\Seme\Year_3_Semester_3\WebTracNghiem\Web\.venv\Scripts\activate.bat

python .\manage.py makemigrations 
python .\manage.py migrate
python .\manage.py runserver
