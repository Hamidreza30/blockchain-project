from blockchain import Blockchain


simple_bitcoin = Blockchain(name="junior_bitcoin")

assert simple_bitcoin.latest_block_number() == -1

[simple_bitcoin.transact('0000', '1145', 1) for _ in range(5)]
assert simple_bitcoin.latest_block_number() == 0

assert simple_bitcoin.balance_of('1145') == 5

block = simple_bitcoin.get_block_by_number(0) # -> object of Block
assert len(block.get_transactions()) == 5
assert block.block_number == 0
assert block.parent_block_hash == '0'

assert simple_bitcoin.balance_of('1233') == 0
assert simple_bitcoin.balance_of('1213') == 0

simple_bitcoin.transact('1145', '1213', 1)
assert simple_bitcoin.balance_of('1213') == 0
assert simple_bitcoin.balance_of('1145') == 5

simple_bitcoin.transact('1145', '1213', 3)
assert simple_bitcoin.balance_of('1233') == 0
assert simple_bitcoin.transact('1145', '5661', 3) == False
assert simple_bitcoin.balance_of('1145') == 5

simple_bitcoin.transact('0000', '7550', 2)
simple_bitcoin.transact('0000', '7550', 1)
simple_bitcoin.transact('0000', '5661', 1)

assert simple_bitcoin.latest_block_number() == 1
assert simple_bitcoin.balance_of('1145') == 1
assert simple_bitcoin.balance_of('7550') == 3
assert simple_bitcoin.balance_of('1233') == 4
assert simple_bitcoin.balance_of('5661') == 1

block = simple_bitcoin.get_block_by_number(1)
assert block.parent_block_hash[-1] in '2468'
