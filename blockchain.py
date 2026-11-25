from block import Block
from transaction import Transaction


class Blockchain:
    def __init__(self, name="junior_bitcoin"):
        self.name = name
        self.blocks = []
        self.pending_transactions = []

    def latest_block_number(self):
        if not self.blocks:
            return -1

        return self.blocks[-1].block_number

    def get_block_by_number(self, block_number):
        for block in self.blocks:
            if block.block_number == block_number:
                return block

        return None

    def balance_of(self, account):
        balance = 0

        for block in self.blocks:
            for transaction in block.get_transactions():
                if transaction.sender == account:
                    balance -= transaction.amount

                if transaction.recipient == account:
                    balance += transaction.amount

        return balance

    def transact(self, sender, recipient, amount):
        sender = str(sender)
        recipient = str(recipient)
        amount = int(amount)

        if amount <= 0:
            return False

        if sender != "0000":
            available_balance = self.balance_of(sender)

            for transaction in self.pending_transactions:
                if transaction.sender == sender:
                    available_balance -= transaction.amount

                if transaction.recipient == sender:
                    available_balance += transaction.amount

            if available_balance < amount:
                return False

        transaction = Transaction(sender, recipient, amount)
        self.pending_transactions.append(transaction)

        if len(self.pending_transactions) == 5:
            self.create_block()

        return True

    def create_block(self):
        if not self.pending_transactions:
            return None

        if not self.blocks:
            parent_hash = "0"
        else:
            parent_hash = self.blocks[-1].block_hash

        block = Block(
            self.pending_transactions,
            self.latest_block_number() + 1,
            parent_hash
        )

        block.mine()
        self.blocks.append(block)
        self.pending_transactions = []

        return block

    def chain_info(self):
        transaction_count = 0

        for block in self.blocks:
            transaction_count += len(block.get_transactions())

        return (
            self.name,
            self.latest_block_number(),
            transaction_count
        )