message = input().split()
deciphered_message = []

for word in message:
    num_part = ''.join(filter(str.isdigit, word))
    char_part = word[len(num_part):]
    first_letter = chr(int(num_part))
    if len(char_part) > 1:
        deciphered_word = first_letter + char_part[-1] + char_part[1:-1] + char_part[0]
    else:
        deciphered_word = first_letter + char_part

    deciphered_message.append(deciphered_word)

print(' '.join(deciphered_message))
