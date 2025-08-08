class CreditCardPayment:
    def pay(self, value):
        print(f'CreditCardPayment: R${float(value)}')

class PixPayment:
    def pay(self, value):
        print(f'PixPayment: R${float(value)}')

class PaymentFactory:

    @staticmethod
    def creat_payment(method: str):
        if method.lower() == 'creditcard':
            return CreditCardPayment()
        elif method.lower() == 'pix':
            return  PixPayment()


payment = PaymentFactory.creat_payment('creditcard')
payment.pay(100)
