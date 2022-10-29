ENGLISH_MORSE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


def eng_to_char(text):
    morse_code_response = []
    for char in text:
        if char in ENGLISH_MORSE_DICT:

            morse_code_response.append(ENGLISH_MORSE_DICT[char])

    response = ""
    for code in morse_code_response:
        response += " "
        response += code
    return (response)


raw_text = input("Enter the text you would like to convert to morse code\n")
text = raw_text.upper()
response_code = eng_to_char(text)
print(response_code)
