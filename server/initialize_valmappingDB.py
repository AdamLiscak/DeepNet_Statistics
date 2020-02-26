 
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  passwd="test1234",
  database="statistics_convnet"
)

with open("val_mapping_minimal.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

sql =  "INSERT INTO val_mapping(val) VALUES(%s)"
mycursor = mydb.cursor()
for i in range (len(content)):
 #print(content[i])
    index = (content[i],)
    mycursor.execute(sql,index)

mydb.commit()
