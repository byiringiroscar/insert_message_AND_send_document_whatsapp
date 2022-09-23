# whatsapp_send_vanilla
send message to whatsapp group by using python with mysql

steps to execute this project \n

1. create directory
2. open that direcory by using command prompt by window
3. create envirnment by using this command on window: python -m venv venv
4. activate the envirnment by using this command : venv\Scripts\activate
5.then install requirements by using this command : pip install -r requirements.txt  or pip install requirements.txt
6. configure your credential in file called main.py by checking the user, passwd, database according to your own
7. configure also line ===== mycursor.execute("select * from people")  === change people your table name
8. before run main.py go to this site === https://ultramsg.com/ ====   create account and login accordingly
9. create instance AND get instanceID and token  then replace it in utilis.py
10. then also go ===== https://docs.ultramsg.com/api/get/chats =======  make request then get your whatsapp group id accordingly then also replace it in utilis.py
