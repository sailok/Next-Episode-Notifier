# Next-Episode-Notifier

Works only for Series and that are available on OMDB api

Instructions:
1) Run config.py file and register the username,password,host of MySQL Database and then register the sender's Email addressa along with its password

2) Run main.py file and enter your email address and Tv series that you want to get notified

Working:
1) After registering in config.py it will create a object using db.py and a connection to the database is established
2) This connection is used by main.py while entering the details of email address and Tv series and add them to Dataabase
3) After exiting from main.py it invokes scraper.py to send Email notifications
4) scraper.py first obtains imdbID of the given show using OmDB Api
5) After getting the imdbID , it scrapes the imdb page using the id and extracts the date of next episode or season or whether show has streamed all its episodes
6) Finally a email notification is sent to the registered email
