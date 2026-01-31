from flask import Flask
import random

app = Flask(__name__)

def get_weather_condition():
    num = random.randint(1, 10)
    if num <= 4:
        return "Sunny"
    elif num <= 7:
        return "Cloudy"
    else:
        return "Rainy"



@app.route('/')
def weather():
    weather_today = get_weather_condition()
    
    if weather_today == "Sunny":
        status = "The weather is good! Enjoy your day!"
    elif weather_today == "Cloudy":
        status = "It's cloudy today. A calm day ahead!"
    else: 
        status = "The weather is not so good. Stay safe!"
    
    return f"Today's weather is: {weather_today} {status}"

if __name__ == '__main__':
    app.run(debug=True)
