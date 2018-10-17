import mysql.connector

class Database:
	"Database maintainance"
	
	def __init__(self,host,username,password):
		self.host=host
		self.username=username
		self.password=password
		
	def connect(self):
		flag=False
		mydb=mysql.connector.connect(host=self.host,user=self.username,passwd=self.password)
		cursor=mydb.cursor()
		cursor.execute("SHOW DATABASES;")
		for x in cursor:
			if (x[0]=='seriesdb'):
				flag=True
		if(flag!=True):
			cursor.execute("CREATE DATABASE seriesdb;USE seriesdb;CREATE TABLE Users(UID INT PRIMARY KEY 					AUTO_INCREMENT,EmailID VARCHAR(255),Series VARCHAR(255));")		
		mydb.close()
		
	def add(self,email,series):
		mydb=mysql.connector.connect(host=self.host,user=self.username,passwd=self.password,database='seriesdb')
		cursor=mydb.cursor()
		cursor.execute("INSERT INTO Users(EmailID,Series) VALUES(%s,%s);",(email,series));	
		mydb.commit()
	
	def fetch(self,row):
		mydb=mysql.connector.connect(host=self.host,user=self.username,passwd=self.password,database='seriesdb')
		cursor=mydb.cursor()
		cursor.execute("SELECT * FROM Users WHERE UID="+str(row)+";");
		
		for x in cursor:
			return x[1],x[2]
		mydb.commit()
	def total(self):	
		mydb=mysql.connector.connect(host=self.host,user=self.username,passwd=self.password,database='seriesdb')
		cursor=mydb.cursor()
		cursor.execute("SELECT * FROM Users;")
		total=cursor.fetchall()
		return len(total)

