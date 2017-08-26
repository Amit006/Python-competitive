import mysql.connector

def Take_input():
    times = int(input("enter how many times "))
    for i in times:
        table = str(input("enter the tablename")) 
        position = str(input("where you want to update"))
        value = str(input("enter the value"))


db=mysql.connector.connect(host='localhost',port='4406',database='pythondb',user='root',password='toor')
s = "select name,owner,species,sex,birth,date from pet"
cursor = db.cursor()
cursor.execute(s)
data = cursor.fetchall()
for row in data :
    print ('Name:',row[0], ' owner: ',row[1],'species:',row[2],'sex:',row[3],'birth:',row[4],'deth:',row[5])
cursor.close()
db.commit()
db.close()

