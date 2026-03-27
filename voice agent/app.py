from flask import Flask, render_template, jsonify, session
from voice_agent import listen, speak
from local_ai_client import ask_ai
from desktop_control import open_app

app = Flask(__name__)
app.secret_key = "voice-ai-secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/listen", methods=["POST"])
def listen_route():
    user_text = listen()

    if not user_text:
        speak("Sorry, I did not hear anything.")
        return jsonify({"user": "", "ai": "No input detected"})

    # Desktop commands
    app_response = open_app(user_text)
    if app_response:
        speak(app_response)
        save_history(user_text, app_response)
        return jsonify({"user": user_text, "ai": app_response})

    # AI response
    ai_reply = ask_ai(user_text)
    if not ai_reply:
        ai_reply = "Sorry, something went wrong."

    speak(ai_reply)
    save_history(user_text, ai_reply)
    return jsonify({"user": user_text, "ai": ai_reply})

@app.route("/history")
def history():
    return jsonify(session.get("history", []))

@app.route("/clear_history", methods=["POST"])
def clear_history():
    session["history"] = []
    return jsonify({"status": "cleared"})

def save_history(user, ai):
    history = session.get("history", [])
    history.append({"user": user, "ai": ai})

    # limit history size (safe)
    if len(history) > 20:
        history = history[-20:]

    session["history"] = history

if __name__ == "__main__":
    app.run(debug=True)
