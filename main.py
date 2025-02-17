# Transform input text to morse code  

#Assign Each Letter the Morse Code Representation
# Format the Output 


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

#Create input

word = input("Enter the text to encode : ")
# print(word)

#Separate the String into Characters  
    # Loop through each character and replace it with its Morse equivalent. 
morse_list = []

def text_to_morse(word):
    word = word.upper()  # Convert to uppercase
    morse_list = []  # Store Morse code symbols

    for char in word:
        if char in MORSE_CODE_DICT:
            morse_list.append(MORSE_CODE_DICT[char])  # Convert to Morse
        elif char == " ":
            morse_list.append("/")  # Word separator

    return " ".join(morse_list)  # Join Morse symbols with spaces


result = text_to_morse(word)
print(result)



reversed_morse_code_DICT= {}
for key, value in MORSE_CODE_DICT.items():
    reversed_morse_code_DICT[value] = key

#dict comprehention
#reversed_morse = {value: key for key, value in MORSE_CODE_DICT.items()}

def morse_to_text(morse_code):
    words = morse_code.split("/")
    decoded_words = []


    for word in words:
        letters= word.split(" ")
        decoded_word = "".join(reversed_morse_code_DICT[letter] for letter in letters if letter in reversed_morse_code_DICT )
        decoded_words.append(decoded_word)

    return " ".join(decoded_words)


morse_input = input("Enter Morse code to decode:\n")
decoded_text = morse_to_text(morse_input)
print(decoded_text)


