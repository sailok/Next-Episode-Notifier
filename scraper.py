import unicodedata
import urllib2
import simplejson as json
from BeautifulSoup import BeautifulSoup
import re
import datetime
import smtplib
import config

def dateConv(date):
	date=str(date)
	if(len(date)==0):
		return str(int(datetime.datetime.now().year)+1)
	elif(len(date)==4):
		return date
	else:
		finDate=""+date[-4:]+"/"
		months={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
		
		if(date[2]==" "):	
			finDate=finDate+months[str(date[3:6])]+"/"+date[:2]
			return finDate
		if(date[1]==" "):
			finDate=finDate+months[str(date[2:5])]+"/0"+date[:1]
			return finDate
	
def getID(title):
	url="https://www.omdbapi.com/?t="+str(title)+"&apikey=82abd081"
	html_page=urllib2.urlopen(url)
	soup=BeautifulSoup(html_page)
	t=str(soup).find("imdbID")
	return str(soup)[t+9:t+18]

def findNext(tid):
	weblinks=[]
	next=[]
	url="https://www.imdb.com/title/"+tid
	html_page=urllib2.urlopen(url)
	soup=BeautifulSoup(html_page)
	
	CurrentDate=datetime.datetime.now()

	divData=soup.findAll('div',attrs={'id': 'title-episode-widget'})
	for div in divData:
		for link in div.findAll('a'):
			weblinks.append(link.get('href'))
	
	for i in range(len(weblinks)):
		temp_page=urllib2.urlopen("https://www.imdb.com"+weblinks[i])
		temp_soup=BeautifulSoup(temp_page)
		
		try:
			temp_div=temp_soup.findAll('div',attrs={'class':'airdate'})
			nextDate=dateConv(temp_div[-1].text)
	
			if(len(nextDate)==4):
				next="The next season begins in "+str(nextDate)
				return next
			else:
				nextDate=datetime.datetime.strptime(nextDate,'%Y/%m/%d')
				if(nextDate >= CurrentDate):
					next="The next episode airs on "+str(nextDate)[:10]
					return next
					break
				else:
					next="The show has finished streaming all its episodes."
					return next
					break
		except:
			print()	
		
	return next
					

def sendEmail(reciever,message):
	smtpObj=smtplib.SMTP('smtp.gmail.com',587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(config.sender,config.emailPass)
	smtpObj.sendmail("sailokchinta2012@gmail.com",reciever,message)
	smtpObj.close()

def main():
	rows=config.db.total()
	for i in range(1,rows+1):
		seriesString=config.db.fetch(i)		
		series=seriesString[1].split(',')
		msg="\n\n"
		for j in range(len(series)):
			status=findNext(getID(series[j].replace(" ","-")))
			msg=msg+"TV series name: "+series[j]+"\nStatus: "+status+"\n\n"
		sendEmail(seriesString[0],msg)		
	
if __name__=="__main__":
	main()
