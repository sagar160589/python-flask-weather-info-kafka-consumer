# python-flask-weather-info-kafka-consumer
This project is a Kafka consumer which pulls the information of weather in realtime from the topic
"weather_data" from Kafka broker and updates the UI with the weather information.
This will run as a flask project on port 9001. Check main.py

To run this project you need to install kafka as per below steps:

1. Install Kafka by downloading it from https://kafka.apache.org/downloads
2. Create a data folder and create 2 folders inside it to store Kafka and Zookeper logs
3. Open server.properties inside config folder and update log.dirs=E:/kafka_2.12-3.4.0/kafka_2.12-3.4.0/data/kafka-logs with your directory path of the kafka logs folder created inside data folder
4. Open zookeeper.properties and update dataDir=E:/kafka_2.12-3.4.0/kafka_2.12-3.4.0/data/zookeeper as per above for zookeeper logs.
5. Start Zookeeper by opening cmd using command zookeeper-server-start.bat config\zookeeper.properties if outside config folder.
6. Start Kafka by opening cmd using command kafka-server-start.bat config\server.properties if outside config folder
7. Once started access the URL http://127.0.0.1:9001/ and once there is any weather detail inside Kafka broker topic it will appear here.