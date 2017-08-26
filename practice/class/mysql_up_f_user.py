import mysql.connector

times = int(input("enter how many times:"))
for i in times:
    table = str(input("enter the tablename:")) 
    collum_name = str(input("collum u want to update:"))
    value = str(input("enter update value:"))
    where_addr =str(input("enter where u want to update"))
    where_value = str(input("enter the where_value")

    
def db_connection():
    db=mysql.connector.connect(host='localhost',port='4406',database='pythondb',user='root',password='toor')


def update():
    s = "update "+table+" set "+collum_name+" = '"+value+"' where "+where_addr+" ='"+where_value+"';"
    c = db.cursor()
    c.execute(s)
    c.commit()


def Display_update(collum_name,): 
    db_connection()
    s = "select "+collum+" from "+where_addr+" where "++" ='"+where_value+"';"
    c = db.cursor()
    c.execute(s)
    c.commit()

def Display_all():
    db_connection()
    c = db.cursor()
    data = c.fetchall()
    for row in data :
        print ('Name:',row[0], ' owner: ',row[1],'species:',row[2],'sex:',row[3],'birth:',row[4],'deth:',row[5])    
    cursor.close()
    db.commit()
    db.close()


if __name__ = "__main__":
                      db_connection()
                      update()
                      Display_update()
                      Display_all()
                      
