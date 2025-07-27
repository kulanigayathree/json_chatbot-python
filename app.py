from flask import Flask, render_template, request, jsonify
import main  # Import your chatbot logic

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_input = request.json.get("msg")
    response = main.get_responses(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
