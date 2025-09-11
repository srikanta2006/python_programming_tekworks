class Payment:
        def pay(self,amount):
            pass

class CashPayment(Payment):
      def pay(self,amount):
            print(f"Paid ₹{amount} in cash")

class CardPayment(Payment):
      def pay(self,amount):
            print(f"Paid ₹{amount} using debit/credit card")

class UPIPayment(Payment):
      def pay(self, amount):
            print(f"Paid ₹{amount} using UPI")

