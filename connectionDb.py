#implementing the database connection in python
### using the mysql database connection
#--------- mysql-connector for python is the desired module for the database connection in python
#############MAKING  THE ACTUAL DB CONNECTION

import mysql.connector


#the connect function belongs to the mysql.connector module
dbconnection=mysql.connector.connect(host="localhost",user="root",passwd="77045109",database="pythonmysql")
cursor=dbconnection.cursor()

#
#command="create table users(id int primary key not null,username varchar(100) not null,phone varchar(10) not null,email varchar(50) not null, password varchar(100) not null)"

command="insert into users(username,phone,email,password) values('samuelbills','0550465223','biliksuunsamuel@gmail.com','77045109')"
#command="select * from users"
try:
	cursor.execute(command)
except Exception as ex:
	print("mysql execution error\n",ex)

