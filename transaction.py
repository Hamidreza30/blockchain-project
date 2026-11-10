import datetime

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"sender: {self.sender}, recipient: {self.recipient}, amount: {self.amount}"

Transaction('3455','3243',100)