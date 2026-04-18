class Card:
    def __init__(self, card_number, pin_code, account):
        self.card_number = card_number
        self.pin_code = pin_code
        self.account = account

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class Transaction:
    def __init__(self, amount, type):
        self.amount = amount
        self.type = type

class ATM:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def authenticate(self, card_number, pin_code):
        for card in self.cards:
            if card.card_number == card_number and card.pin_code == pin_code:
                return card
        return None

    def deposit(self, card, amount):
        card.account.balance += amount
        transaction = Transaction(amount, 'deposit')
        print(f'Deposited {amount} to account {card.account.account_number}')

    def withdraw(self, card, amount):
        if card.account.balance >= amount:
            card.account.balance -= amount
            transaction = Transaction(amount, 'withdrawal')
            print(f'Withdrew {amount} from account {card.account.account_number}')
        else:
            print('Insufficient balance')

    def check_balance(self, card):
        print(f'Account balance: {card.account.balance}')


account1 = Account('12345', 1000)
card1 = Card('1111-1111-1111-1111', '1234', account1)
atm = ATM()
atm.add_card(card1)

card = atm.authenticate('1111-1111-1111-1111', '1234')
if card:
    atm.deposit(card, 500)
    atm.withdraw(card, 200)
    atm.check_balance(card)
else:
    print('Authentication failed')

account2 = Account('67890', 500)
card2 = Card('2222-2222-2222-2222', '5678', account2)
atm.add_card(card2)

card = atm.authenticate('2222-2222-2222-2222', '5678')
if card:
    atm.deposit(card, 200)
    atm.withdraw(card, 100)
    atm.check_balance(card)
else:
    print('Authentication failed')