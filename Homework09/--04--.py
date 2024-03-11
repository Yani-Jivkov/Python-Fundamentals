sequence = input().split()
palindrome_to_find = input()

found_palindromes = []

palindrome_count = 0

for word in sequence:
    if word == word[::-1]:
        found_palindromes.append(word)
        if word == palindrome_to_find:
            palindrome_count += 1

print(found_palindromes)
print(f'Found palindrome {palindrome_count} times')
