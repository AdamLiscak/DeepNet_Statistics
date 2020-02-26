
import mysql.connector
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  passwd="test1234",
  database="statistics_convnet"
)

sql = "SELECT * FROM results as a inner join statistics as b WHERE b.id = a.stat_id " 

mycursor = mydb.cursor()
mycursor.execute(sql)
huuuge_string = mycursor.fetchall()
#print(huuuge_string)[0][:10]
k = json.dumps(huuuge_string)
f = open('databasedump.json', 'w')
f.write(k)  # python will convert \n to os.linesep
f.close() 
