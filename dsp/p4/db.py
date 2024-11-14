################ Connection With MySQL ######################
import mysql.connector
conn = mysql.connector.connect(host='localhost',
 database='DataScience',
user='root',
 password='123456')
conn.connect
if(conn.is_connected):
 print('###### Connection With MySql Established Successfullly ##### ')
else:
 print('Not Connected -- Check Connection Properites')
