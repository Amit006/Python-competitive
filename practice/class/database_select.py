import mysql.connector

db=mysql.connector.connect(host='localhost',port='4406',database='pythondb',user='root',password='toor')
s = "select * from pet"
cursor = db.cursor()
cursor.execute(s)
data = cursor.fetchall()
for row in data :
    no = 1
    print("printing table {}.row data:{} \n".format(no,row))
    print ('Name:',row[0],'\t', 'owner:',row[1],'\t','species:',row[2],'\t','sex:',row[3],'\t','birth:',row[4],'\t','deth:',row[5])
cursor.close()
db.commit()
db.close()
