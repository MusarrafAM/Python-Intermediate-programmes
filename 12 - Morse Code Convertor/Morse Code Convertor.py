morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', "'": '.----.',
    '!': '-.-.--', ';': '-.-.-.', '@': '.--.-.', ' ': '/'
}


# Text To Morse Code
def text_to_morse():
    user_text = input("Enter the text that needs to be converted to Morse Code: ").upper()
    converted_text = ""
    for i in user_text:
        if i in morse_code_dict:
            converted_text += morse_code_dict[i] + " "
        else:
            converted_text += i + " "
    print("\nText to Morse Code Conversion:")
    print(converted_text)


# Morse Code To Text
def morse_to_text():
    user_input = input("Enter the Morse code that needs to be converted to text: ")
    user_input = user_input.split()
    converted_text = ""
    for i in user_input:
        if i in morse_code_dict.values():
            for key, value in morse_code_dict.items():
                if value == i:
                    converted_text += key
        else:
            converted_text += i
    print("\nMorse Code to Text Conversion:")
    print(converted_text)


should_continue = True
while should_continue:
    choice = input(
        "\nWhich option do you want to choose?\n1: Text to Morse Code Conversion\n2: Morse Code to Text Conversion\nPlease enter your choice (1 or 2): ")

    if choice == "1":
        text_to_morse()
    elif choice == "2":
        morse_to_text()
    else:
        print("Invalid choice.")

    continue_check = input("\nDo you want to continue? Input 'YES' or 'NO': ").lower()
    if continue_check == 'no':
        print("Goodbye")
        should_continue = False
    elif continue_check != 'yes':
        print("Invalid input. Exiting the program.")
        should_continue = False
