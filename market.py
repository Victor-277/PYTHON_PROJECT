import mysql.connector as  sql


mycon = sql.connect(host = "localhost", user = "root" , passwd = "", database="market")


mycursor = mycon.cursor()




# mycursor.execute("CREATE DATABASE market")  
# mycursor.execute("CREATE TABLE customer(id INT(4) AUTO_INCREMENT  PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50), Phone_number INT(11) UNIQUE, Address VARCHAR(50), state VARCHAR(50))")


class market:
    pass



met = market
