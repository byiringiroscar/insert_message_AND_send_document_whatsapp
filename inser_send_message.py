from get_all_message_official import receive_message_sent
from convert_timestamp import convert_time_stamp
import mysql.connector

all_message = receive_message_sent()
if not all_message:
    print("-----------------------connection ------error ------------------")
else:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="whatsapp_send")

    mycursor = mydb.cursor()

    mycursor.execute("select * from receive_send_message")
    result = mycursor.fetchall()
    if result:
        for sent_msg in all_message:
            for message in result:
                try:
                    sql = "INSERT INTO receive_send_message (id, message_body, Time_sent) VALUES (%s, %s, %s)"
                    time_sent_exact = convert_time_stamp(sent_msg['timestamp'])
                    val = (sent_msg['id'], sent_msg['body'], time_sent_exact)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record inserted.")
                except:
                    print("record already in db")

    else:
        for sent_msg in all_message:
            try:
                sql = "INSERT INTO receive_send_message (id, message_body, Time_sent) VALUES (%s, %s, %s)"
                time_sent_exact = convert_time_stamp(sent_msg['timestamp'])
                val = (sent_msg['id'], sent_msg['body'], time_sent_exact)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
            except:
                print("record already in db")


