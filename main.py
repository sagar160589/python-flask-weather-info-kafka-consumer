from flask import Flask, render_template
from consumer.consumer import Consumer
app = Flask(__name__)
consumer = Consumer()

@app.route("/")
def get_weather_data():
    #Get data from Kafka broker
    try:
        weather_data = consumer.consume_data()
        return render_template('index.html', weather=weather_data)
    except ValueError:
        return render_template('index.html', error="Error")
    
    
if __name__ == "__main__":
    app.run(debug=True, port=9001)