import config
import os

def main():
	print("Welcome to Series Buff")
	
	while(1):
		print("\nMENU")
		print("1.Enter Input")
		print("2.Exit")
		
		choice=raw_input()
		
		if(int(choice)==1):	
			print("EMAIL ID:")
			email=raw_input()
			print("TV SERIES:")
			series=raw_input()
			config.db.add(email,series)
		else:
			break	
	print("Exiting the Programme...")
	os.system("python scraper.py")

if __name__=="__main__":
	main()
