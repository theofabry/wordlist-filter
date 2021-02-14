import os
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('[ERROR] Incorrect number of arguments. Use: python wordlist-filter.py <filename>')

        sys.exit()

    file_path_str = sys.argv[1]
    file_path = os.path.normpath(file_path_str)

    special_chars_checked = False
    special_chars_number = 0
    while not special_chars_checked:
        special_chars_input = input('Are special chars mandatory? <number of chars> / [N]: ')

        if not special_chars_input.isdigit() and special_chars_input != '' and special_chars_input.lower() != 'N':
            print('Enter either an integer or N (or press Enter).')
        else:
            special_chars_checked = True
            if special_chars_input.isdigit():
                special_chars_number = int(special_chars_input)

    digits_checked = False
    digits_number = 0
    while not digits_checked:
        digits_input = input('Are digits mandatory? <number of digits> / [N]: ')

        if not digits_input.isdigit() and digits_input != '' and digits_input.lower() != 'N':
            print('Enter either an integer or N (or press Enter).')
        else:
            digits_checked = True
            if digits_input.isdigit():
                digits_number = int(digits_input)

    with open(file_path, 'r') as original_file:
        for line in original_file:
            word = line.rstrip()
            kept = True

            if special_chars_number > 0:
                special_chars_count = 0
                for char in word:
                    if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789':
                        special_chars_count += 1

                if special_chars_count < special_chars_number:
                    print(f'Word {word} filtered, not enough special chars.')
                    kept = False
                    continue

            if digits_number > 0:
                digits_count = 0
                for char in word:
                    if char in '0123456789':
                        digits_count += 1

                if digits_count < digits_number:
                    print(f'Word {word} filtered, not enough digits.')
                    kept = False
                    continue

            print(f'Word {word} kept!')
