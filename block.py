import hashlib
import datetime


class Block:
    def __init__(self, transactions, block_number, parent_block_hash):
        if len(transactions) > 5:
            raise ValueError("A block cannot contain more than 5 transactions")

        self.transactions = tuple(transactions)
        self.block_number = block_number
        self.parent_block_hash = parent_block_hash
        self.timestamp = datetime.datetime.now()
        self.random_number = 0
        self.block_hash = None

    def hash(self):
        data = ""

        for i in self.transactions:
            data += str(i.sender)
            data += str(i.recipient)
            data += str(i.amount)
            data += str(i.timestamp)

        data += str(self.parent_block_hash)
        data += str(self.block_number)
        data += str(self.timestamp)
        data += str(self.random_number)

        result = data.encode("utf-8")
        return hashlib.sha256(result).hexdigest()

    def mine(self):
        block_hash = self.hash()

        while True:
            if block_hash[-1] in "2468":
                self.block_hash = block_hash
                return block_hash

            self.random_number += 1
            block_hash = self.hash()

    def get_transactions(self):
        return self.transactions

    def is_mined(self):
        return self.block_hash is not None