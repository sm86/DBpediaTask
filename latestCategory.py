import urllib2
from StringIO import StringIO  
import gzip
import pymysql
#This file has the Script that downloads the latest 'category table' from Wikimedia and then dump in SQL Server.
# Url to dowmload latest categories from WIKI Data Dump is https://dumps.wikimedia.org/metawiki/latest/metawiki-latest-category.sql.gz


#Extracting categories from Wikimedia Dump
request = urllib2.Request('https://dumps.wikimedia.org/metawiki/latest/metawiki-latest-category.sql.gz')
request.add_header('Accept', 'application/gzip') #Accept data in gz format
response = urllib2.urlopen(request)  #Get Request for downloading Data Dump.
buf = StringIO(response.read()) #Read String as a gz file 
f = gzip.GzipFile(fileobj=buf) #extract the sql file from the metawiki-latest-category.sql.gz 
data = f.read() #read the data from the file.
# print data


#Dumping Categories into MySQL Database
dbConnection = pymysql.connect(user='your-username',      # Username
								 passwd='your-password',  #Your password
                                 host='localhost', #Your Host name
                                 database='dbpedia') #Database name
cursor = dbConnection.cursor()    
cursor.execute(data)  #Executes the query
dbConnection.close() #Close the database connection