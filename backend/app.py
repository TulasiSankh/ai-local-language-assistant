from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
def ai_response(message, language):
    responses = {
        "en": "This service helps you access government schemes and local services.",
        "hi": "यह सेवा आपको सरकारी योजनाओं और स्थानीय सेवाओं तक पहुंचने में मदद करती है।",
        "kn": "ಈ ಸೇವೆ ನಿಮಗೆ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಮತ್ತು ಸ್ಥಳೀಯ ಸೇವೆಗಳಿಗೆ ಪ್ರವೇಶ ನೀಡುತ್ತದೆ."
    }
    return responses.get(language, responses["en"])
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    return jsonify({"reply": ai_response(data.get("message"), data.get("language","en"))})
if __name__ == "__main__":
    app.run(debug=True)