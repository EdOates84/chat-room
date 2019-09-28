# chat-room

Basic example of a multi-room chatroom, with messages from all rooms a user is in multiplexed over a single WebSocket connection.

There is no chat persistence; you only see messages sent to a room while you are in that room.

Uses the Django auth system to provide user accounts; users are only able to use the chat once logged in, and this provides their username details for the chatroom.

Some channels can be limited to only "staff" users; the example includes code that checks user credentials on incoming WebSockets to allow or deny them access to chatroom streams based on their staff status.

setup instruction on debian 9 

  then finally run   
source/p3/bin/activate

python manage.py runserver  

Visit the local development server at 127.0.0.1:8000/accounts/login to test the site.


and the login is   
username=ritik
password=ritik123!@#  
username=ajay  
password=ajay123!@#$  

