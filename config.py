from db import Database

host=""
username=""
password=""
sender=""
emailPass=""

db=Database(host,username,password)
db.connect()

def main():
	print("Enter host")
	host=raw_input()
	
	print("Enter Username of the database")
	username=raw_input()
		
	print("Enter Password for the database")
	password=raw_input()
	
	print("Enter Sender Email Address")
	sender=raw_input()
		
	print("Enter Password for the Email")
	emailPass=raw_input()		
	
if __name__=="__main__":
	main()
