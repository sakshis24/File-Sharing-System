# File-Sharing-System
This python3 code need "pymysql" so as to connect with Mysql command client and for storing the details of transfer of files automatically.

For importing pymysql ,, 
Open command prompt ---> write pip install pymysql 
----> if it shows error that pip is not recognized as internalor external command it means you have to add path of the pip in your envionment variables. do this--->START-->TYPE EDIT ENVIONMENT VARIABLES-->EDIT-->NEW--> COPY PASTE THE PATH OF pip(which is found in Scripts of your python installation)

Then Open your mysql installer open it. CREATE mydb named database and Sample named table and change the password of your mysql in the python code for connecting python code to mysql db.Now run the python code.

This code comprises of MAINLY OPTIMIZING THE DISTRIBUTION OF FILE SIZES AMONG CLIENTS.and Mysql code embedded in it ,when connect with Mysql displays transfer of files among clients.

Steps to run
__________
Terminal 1
python server.py

Terminal 2
______
python client.py

host:localhost
port:33000

