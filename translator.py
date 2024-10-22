import sys

# conversions
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

braille_to_english = {
    braille:char for char, braille in english_to_braille.items() if not char.isdigit()
}

braille_to_numbers = {
    braille:num for num, braille in english_to_braille.items() if num.isdigit()
}


def translate_to_english(string):
    translation = ''

    # flags to check if next character is in caps or a num
    caps_flag = False
    number_flag = False

    # splitting into 6 character blocks
    braille_chars = [string[i: i+6] for i in range(0, len(string), 6)]

    for braille in braille_chars:
        # invalid character
        if braille not in braille_to_english:
            continue
        # checking if next character will be in caps, a num or a space
        elif braille_to_english[braille] == 'capital':
            caps_flag = True
        elif braille_to_english[braille] == 'number':
            number_flag = True
        elif braille_to_english[braille] == ' ':
            translation += ' '
            number_flag = False
        else:
            # adding translated value accordingly
            if caps_flag: translation += braille_to_english[braille].upper()
            elif number_flag: translation += braille_to_numbers[braille]
            else: translation += braille_to_english[braille]
            # reset flag
            caps_flag = False

    return translation

def translate_to_braille(string):
    translation = ''

    # flag to check if next characters are nums
    number_flag = False

    for char in string:
        # invalid character
        if char.lower() not in english_to_braille:
            continue
        # checking if character is in caps, a num or a space
        elif char.isupper():
            translation += english_to_braille['capital']
            translation += english_to_braille[char.lower()]
        elif char.isdigit():
            if not number_flag:
                number_flag = True
                translation += english_to_braille['number']
            translation += english_to_braille[char]
        elif char == ' ':
            translation += english_to_braille[' ']
            # reset flag as number ended
            number_flag = False
        else: translation += english_to_braille[char]

    return translation

def check_braille(string):
    return all(char in 'O.' for char in string)

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    string = ' '.join(sys.argv[1:])

    if check_braille(string): print(translate_to_english(string))
    else: print(translate_to_braille(string))

if __name__ == '__main__':
    main()
