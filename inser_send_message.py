from get_all_message_official import receive_message_sent
from convert_timestamp import convert_time_stamp
import mysql.connector
from check_message_word import check_message_contain
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
                    if check_message_contain((sent_msg['body']).lower()):
                        sql = "INSERT INTO receive_send_message (id, message_body, Time_sent, Identifier) VALUES (%s, %s, %s, %s)"
                        time_sent_exact = convert_time_stamp(sent_msg['timestamp'])
                        val = (sent_msg['id'], sent_msg['body'], time_sent_exact, 0)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        print(mycursor.rowcount, "record inserted.")
                    else:
                        print("============keyword=====not =====found")

                except:
                    print("record already in db")

    else:
        for sent_msg in all_message:
            try:
                if check_message_contain((sent_msg['body']).lower()):
                    sql = "INSERT INTO receive_send_message (id, message_body, Time_sent, Identifier) VALUES (%s, %s, %s, %s)"
                    time_sent_exact = convert_time_stamp(sent_msg['timestamp'])
                    val = (sent_msg['id'], sent_msg['body'], time_sent_exact, 0)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record inserted.")
                else:
                    print("============keyword=====not =====found")
            except:
                print("record already in db")


