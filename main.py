from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

# Reverse Morse Code Dictionary for Decoding
REVERSED_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

# Convert Text to Morse
def text_to_morse(text):
    text = text.upper()
    morse_list = [MORSE_CODE_DICT.get(char, '/') for char in text]
    return " ".join(morse_list)

# Convert Morse to Text
def morse_to_text(morse_code):
    words = morse_code.split(" / ")  # Split words by '/'
    decoded_words = []

    for word in words:
        letters = word.split(" ")
        decoded_word = "".join(REVERSED_MORSE_CODE_DICT.get(letter, '') for letter in letters)
        decoded_words.append(decoded_word)

    return " ".join(decoded_words)

# AJAX Routes for Encoding & Decoding
@app.route("/encode", methods=["POST"])
def encode():
    data = request.get_json()
    text = data.get("text", "")
    morse_result = text_to_morse(text)
    return jsonify({"morse": morse_result})

@app.route("/decode", methods=["POST"])
def decode():
    data = request.get_json()
    morse = data.get("morse", "")
    text_result = morse_to_text(morse)
    return jsonify({"text": text_result})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
