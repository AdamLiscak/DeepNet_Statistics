import mysql.connector
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  passwd="test1234",
  database="statistics_convnet"
)
mycursor = mydb.cursor()
x_val = []
y_val = []
def getPointsLeft(offset,mean,step_size,sql_gt):
     while(offset<=mean):
        mycursor.execute(sql_gt,(offset,offset+step_size)) 
        val = mycursor.fetchall()[0][0]
        x_val.append(val)
        y_val.append(offset*1000)
        offset += step_size
        print(val)

def getPointsRight(offset,mean,step_size,sql_lt):
     while(mean<offset):
        mycursor.execute(sql_lt,(mean,mean+step_size))
        val = mycursor.fetchall()[0][0]
        x_val.append(val)
        y_val.append(mean*1000)
        mean += step_size
        print(val)


sql_getavg = "SELECT AVG(time) FROM `statistics` as a INNER JOIN results as b ON b.stat_id = a.id WHERE a.id BETWEEN 1 and 50000"
mycursor.execute(sql_getavg)
mean = mycursor.fetchall()[0][0]
sql_gt = "SELECT count(time)/50000 FROM `statistics` WHERE id BETWEEN 1 and 50000 and time between %s and %s"
sql_lt = "SELECT count(time)/50000 FROM `statistics` WHERE id BETWEEN 1 and 50000 and time between %s and %s"
getPointsLeft(0.1,mean,0.0001,sql_gt)
getPointsRight(0.178,mean,0.0001,sql_lt)
sqval_x = x_val
sqval_y = y_val
x_val = []
y_val = []
sql_getavg = "SELECT AVG(time) FROM `statistics` as a INNER JOIN results as b ON b.stat_id = a.id WHERE a.id BETWEEN 50001 and 100000"
mycursor.execute(sql_getavg)
mean = mycursor.fetchall()[0][0]
sql_gt = "SELECT count(time)/50000 FROM `statistics` WHERE id BETWEEN 50001 and 100000 and time between %s and %s"
sql_lt = "SELECT count(time)/50000 FROM `statistics` WHERE id BETWEEN 50001 and 100000 and time between %s and %s"
getPointsLeft(0.12,mean,0.0001,sql_gt)
getPointsRight(0.25,mean,0.0001,sql_lt)
mb2val_x = x_val
mb2val_y = y_val
x_val = []
y_val = []
sql_getavg = "SELECT AVG(time) FROM `statistics` as a INNER JOIN results as b ON b.stat_id = a.id WHERE a.id BETWEEN 100001 and 150000"
mycursor.execute(sql_getavg)
mean = mycursor.fetchall()[0][0]
sql_gt = "SELECT count(time)/50000 FROM `statistics` WHERE id BETWEEN 100001 and 150000 and time between %s and %s"
sql_lt = "SELECT count(time)/50000 FROM `statistics` WHERE id BETWEEN 100001 and 150000 and time between %s and %s"
getPointsLeft(0.144,mean,0.0001,sql_gt)
getPointsRight(0.25,mean,0.0001,sql_lt)
mb1val_x = x_val
mb1val_y = y_val
x_val = []
y_val = []

sql_getavg = "SELECT AVG(time) FROM `statistics` as a INNER JOIN results as b ON b.stat_id = a.id WHERE a.id BETWEEN 200001 and 250000"
mycursor.execute(sql_getavg)
mean = mycursor.fetchall()[0][0]
sql_gt = "SELECT count(time)/50000 FROM `statistics` WHERE id BETWEEN 200001 and 250000 and time between %s and %s"
sql_lt = "SELECT count(time)/50000 FROM `statistics` WHERE id BETWEEN 200001 and 250000 and time between %s and %s"
getPointsLeft(0.144,mean,0.0001,sql_gt)
getPointsRight(0.25,mean,0.0001,sql_lt)
mb3val_x = x_val
mb3val_y = y_val
x_val = []
y_val = []

plt.xlabel('ms')
plt.ylabel('rel.freq')
plt.plot(sqval_y,sqval_x, label = "SqueezeNet")
plt.plot(mb2val_y,mb2val_x, label = "MobileNetV2")
plt.plot(mb3val_y,mb3val_y, label = "MobileNetV3")
plt.plot(mb1val_y,mb1val_x, label = "MobileNetV1")
plt.legend()
plt.show()
