# DBpediaTask

This repository contains warm-up tasks for DBpedia Project DBTax. 
http://wiki.dbpedia.org/ideas/idea/291/unsupervised-learning-of-a-dbpedia-taxonomy-dbtax/

It is a python project.Contains a single script to do the following tasks:
-Downloads the latest “category table” from Wikimedia (http://dumps.wikimedia.org)
-Automatically imports the dump in a MySQL DB 

Setup before running:
- Make sure you have Python and MySQL installed. And create a database with name dbpedia("CREATE DATABASE dbpedia")
- Replace password, username with your MySQL username and password respectively.

To run:
	python latestCategory.py

