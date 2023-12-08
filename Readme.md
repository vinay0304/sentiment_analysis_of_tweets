Twitter Sentiment Analysis Project

Overview-

This project is a real-time Twitter sentiment analysis application that uses Kafka for message processing, Flask for web serving, and MongoDB for data storage. The project consists of four main components:

kafka_producer.py: Reads data from a CSV file and sends it to a Kafka topic.
kafka_consumer.py: Consumes data from the Kafka topic and may forward it to MongoDB.
app.py: A Flask web application that interacts with MongoDB and streams data to the frontend.
index.html: The frontend UI that displays real-time sentiment analysis of tweets.

Prerequisites:

Python 3.9
Java 8.391
Spark 3.2.1 with hadoop 3.2.1
Apache Kafka 3.1.0
Zookeeper 3.7.0
MongoDB compass
Flask
Chart.js (included via CDN in index.html)

Setup and Installation:

Install python 3.9 and add the python.exe to path in environmental variables.
Install apache kafka3.1.0(scala 2.13 version) - https://kafka.apache.org/downloads
open the folder containing Kafka files and head to the “config” folder at “C:\KAFKA\config”,find a file named “server.properties”. Change the line “log.dirs = /tmp/kafka-logs” to “log.dir=C:/KAFKA/kafka-logs” and save it.

Install Zookeeper 3.7.0 - https://www.apache.org/dyn/closer.lua/zookeeper/zookeeper-3.7.0/apache-zookeeper-3.7.0-bin.tar.gz
open the folder containing zookeeper files and head to the “conf” folder at “C:\ZOOKEEPER\conf”,find a file named “zoo_sample.cfg”. Rename the file to “zoo.cfg” and open the file with a text editor.Find and change “dataDir=/tmp/zookeeper” → “dataDir=C:/ZOOKEEPER/data”. then set environmental variables for zookeeper.

Install java 8.391 and set environmental variables
Install spark 3.2.1 -https://spark.apache.org/releases/spark-release-3-2-1.html
Download hadoop 3.2.1 - https://github.com/cdarlint/winutils/tree/master/hadoop-3.2.1/bin
and place the hadoop files in kafka installation folder,place the files in bin folder. It should look like this C:\kafka\hadoop\bin

Install MongoDB compass- https://www.mongodb.com/products/tools/compass .

Running the Application
(I have used VSCODE as IDE)
Click ctrl+shift+P to open search pallete and click on python:create Environment select Venv and select python.
open terminal and run this to activate virtual environment - .venv\Scripts\activate.bat
Install the requirments from requirments.txt with command- pip install -r requirments.txt
Open terminal and go to kafka installation folder and execute this command to start zookeeper - .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
Open another terminal and go to kafka installation folder and enter this command to start kafka server - .\bin\windows\kafka-server-start.bat .\config\server.properties
open another terminal and create kafka topic using this command - bin/kafka-topics.sh --create --topic [topic name] --bootstrap-server localhost:9092 --partitions 1
(this create a kafka topic)
to view the kafka topics use this command- .\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
place this kafka topic in 51'st line in kafka_producer.py
place the data file or .csv file in 42'nd line in kafka_producer.py
start mongodb local server and create database and collection.
place the created topic name in 45'th line in analysis.py
give the URI of mongoDB in 22'nd and 27'th line in analysis.py
the URI is the connectionstring/databasename.collectionname
first execute kafka_producer.py using py kafka_producer.py
In new terminal run this command- spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1,org.mongodb.spark:mongo-spark-connector_2.12:3.0.1 analysis.py
In another new terminal execute app.py
This starts the Flask App
The the server starts, click on the link to navigate to the webpage to view the results.

Features
Real-time processing of Twitter sentiment data.
Visualization of sentiment data using Chart.js.
Live updates of tweet sentiments in the web interface.