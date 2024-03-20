import re
usernames = input().split(', ')

valid_usernames = []

for username in usernames:
    if 3 <= len(username) <= 16 and re.match("^[a-zA-Z0-9_-]+$", username) and not (username[0].isdigit() or username[-1].isdigit()):
        valid_usernames.append(username)

for valid_username in valid_usernames:
    print(valid_username)
