ALPHABET_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
}
NUMBERS_CODE = {
    "0": '-----',
    "1": '.----',
    "2": '..---',
    "3": '...--',
    "4": '....-',
    "5": '.....',
    "6": '-....',
    "7": '--...',
    "8": '---..',
    "9": '----.'
}
morse_code = ""
sentence = input("ENTER A STRING: ").strip()
for i in sentence:
    if i == " ":
        morse_code += '/'
    elif i.isalpha():
        morse_code += ALPHABET_CODE[i.upper()]
    else:
        morse_code += NUMBERS_CODE[i]
    morse_code += " "
print(f"Morse code: {morse_code}")
