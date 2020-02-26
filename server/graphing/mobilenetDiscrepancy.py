import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  passwd="test1234",
  database="statistics_convnet"
)
mycursor = mydb.cursor()
sql = "SELECT id-50000 FROM `statistics` WHERE id BETWEEN 50001 and 100000 and time between 0.17 and 0.2"
mycursor.execute(sql)
results = mycursor.fetchall()
#print(results)


plt.xlabel('$ i $')
plt.ylabel('$ y_i$',usetex=True)
mb2val1_y = np.array([results[i][0] for i in range(len(results)-1)])
mb2val_y = np.array([50000/3465*i for i in range(len(results)-1)])
diff = mb2val1_y-mb2val_y
print(abs(np.sum(diff)/sum(mb2val_y)))
diffderiv = np.array([diff[i+1]-diff[i] for i in range(len(diff)-1)])

#print(max(mb2val_y))
#print(min(mb2val_y))

plt.plot(mb2val1_y,label = "Real Cumulative Density",color="coral")
plt.plot(mb2val_y, label = 'Ideal Cumulative Density')
#plt.plot(diff,range(len(diff)))

#plt.axis([0,3500,-1000,50000])
plt.legend()
plt.show()
