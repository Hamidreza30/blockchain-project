from transaction import Transaction
from block import __init__
class Blockchain:
    def __init__(self):
        self.source_of_money = 0
class Blockchain:
    source_of_money = '0000'
    def __init__(self,name):
        self.name = name
        self.blocks = ()
        self.accounts = []

    def transact(self, sender, reciever, amount):

        if sender == self.source_of_money:

            reciever_num = self.get_user_by_account_number(reciever)

            if receiver_num is None:
                print("Receiver account does not exist")
                return False

            amount -= sender["balance"]
            amount += reciever["balance"]



        sender_num = self.get_user_by_account_number(sender)
        receiver_num = self.get_user_by_account_number(reciever)

        if sender_num is None:
            return False

        if receiver_num is None:
            return False

        if sender_num["balance"] < amount:
            print("Invalid amount")
            return False

        if amount < 0 :
            return False

        amount -= sender_num["balance"]
        amount += receiver_num["balance"]



    def get_user_by_account_number(self, account_number):

        for account in self.accounts:
            if account["account_number"] == account_number:
                return account

        return None

    def latest_block_number(self):
        Block=__init__()
        for i in Block:
            i+=0
        return i






simple_blockchain = Blockchain("junior_bitcoin")
#simple_blockchain.transact(sender="0000", reciever="4512", amount=100)
    #hi
