# chat-room

Basic example of a multi-room chatroom, with messages from all rooms a user is in multiplexed over a single WebSocket connection.

There is no chat persistence; you only see messages sent to a room while you are in that room.

Uses the Django auth system to provide user accounts; users are only able to use the chat once logged in, and this provides their username details for the chatroom.

Some channels can be limited to only "staff" users; the example includes code that checks user credentials on incoming WebSockets to allow or deny them access to chatroom streams based on their staff status.

setup instruction on debian 9  

 Installation

Manual installation

Make a new virtualenv(p3) for the project, and run:

virtualenv -p python3 p3  
source/p3/bin/activate

pip install django  
pip install django-channels  
pip install django mysqlclient

then start the project(mchat), and run:  
django-admin startproject mchat  
mysql -u mchat -p  
and create database of the app  

then creating the app(nchat), and run:  
python manage.py startapp nchat  

then fill the code in all files like settings.py,urls.py,routing.py etc

then run :

python manage.py makemigrations  
python manage.py migrate  

then finally run   
python manage.py runserver  

Visit the local development server at 127.0.0.1:8000/accounts/login to test the site.


and the login is   
username=ritik
password=ritik123!@#  
username=ajay  
password=ajay123!@#$  
