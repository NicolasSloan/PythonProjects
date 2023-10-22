from abc import ABC, abstractmethod

class receipt(ABC):
    def purchaseAmount(self, amount):
        print("Your total purchase amount is {} dollars\n".format(amount))

        @abstractmethod
        def payment(self, amount):
            pass



class debitCard(receipt):
    def payment(self, amount):
        print('{} was charged to your debit card'.format(amount))

class creditCard(receipt):
    def payment(self, amount):
        print('{} was charged to your credit card'.format(amount))

class giftCard(receipt):
    def payment(self, amount):
        print('{} was charged to your gift card'.format(amount))

def getPayment():
    cardType = input('Would you like to pay with a debit(1), credit(2), or gift card(3)?\nPlease input 1, 2, or 3\n>>>')

    if cardType == '1':
        paymentType = debitCard()
        paymentType.purchaseAmount('$300')
        paymentType.payment('$300')
    elif cardType == '2':
        paymentType = creditCard()
        paymentType.purchaseAmount('$300')
        paymentType.payment('$300')
    elif cardType == '3':
        paymentType = giftCard()
        paymentType.purchaseAmount('$300')
        paymentType.payment('$300')
            



if __name__ == "__main__":
    getPayment()
