class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'

emails = []

while True:
    email = input()

    if email == 'Stop':
        send_pos = list(map(int, input().split(', ')))
        break
    email = email.split()
    sender = email[0]
    receiver = email[1]
    content = email[2]
    helper = Email(sender, receiver, content)
    emails.append(helper)

for x in send_pos:
    emails[x].send()

for i in emails:
    print(i.get_info())
