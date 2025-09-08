from flask import Flask, render_template, request, jsonify
import aiml
import os
import requests
import re
from datetime import datetime
import wikipedia

app = Flask(__name__)

# Path to AIML file
aiml_path = os.path.join(os.path.dirname(__file__), "aiml", "chatbot.aiml")

# Initialize AIML kernel
kernel = aiml.Kernel()
kernel.learn(aiml_path)

# Weather API key
WEATHER_API_KEY = "e8415817a3af100a6cb6876f59e5c749"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    # --- WEATHER HANDLER ---
    if "weather" in user_message:
        match = re.search(r'weather in ([a-zA-Z\s]+)', user_message)
        city = match.group(1).strip().title() if match else "Mumbai"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
            temp = weather_data['main']['temp']
            description = weather_data['weather'][0]['description'].title()
            return jsonify({"reply": f"The current temperature in {city} is {temp}°C with {description}."})
        else:
            return jsonify({"reply": f"Sorry, I couldn't fetch the weather for {city}."})

    # --- TIME HANDLER ---
    elif "time" in user_message:
        current_time = datetime.now().strftime("%I:%M %p")
        return jsonify({"reply": f"The current time is {current_time}."})

    # --- DATE HANDLER ---
    elif "date" in user_message:
        current_date = datetime.now().strftime("%d %B %Y")
        return jsonify({"reply": f"Today's date is {current_date}."})

    # --- WIKIPEDIA HANDLER ---
    elif "who is" in user_message or "what is" in user_message:
        try:
            topic = user_message.replace("who is", "").replace("what is", "").strip()
            summary = wikipedia.summary(topic, sentences=2)
            return jsonify({"reply": summary})
        except:
            return jsonify({"reply": "I couldn't find information on that topic."})

    # --- FALLBACK TO AIML ---
    else:
        bot_reply = kernel.respond(user_message)
        if not bot_reply:
            bot_reply = "I'm not sure how to respond to that."
        return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
