from transaction import Transaction
import datetime
import hashlib


class Block:

    def __init__(self,transactions,block_number,timestamp,parent_block_hash,block_hash,random_number):
        self.transactions = transactions
        self.block_number = 0
        self.timestamp = datetime.datetime.now()
        self.parent_block_hash = parent_block_hash
        self.block_hash = block_hash
        self.cnt=[]

    def transactions(self):
        for i in Transaction():
            cnt.append(i)



    def hash(self):
        if self.block_number < 1:
            return self.block_hash
        if self.parent_block_hash is None:
            return False
        if self.block_number == 5:
            block_hash = hashlib.sha256(str(block_number).encode('utf-8')).hexdigest()

    def timestamp(self):
        for i in self.transactions:
            if len(i) < 5:
                return False
            if len (i) == 5:
                return True

 #   def proof_of_work(self):
#    def parent_hash(self):
