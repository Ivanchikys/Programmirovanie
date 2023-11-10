#balance - ekz
#procent - 0.01
#a - argument f.bank
#years - argument f.bank

class Deposit:
    def __init__(self):
        self.procent = 110

    def bank(self, a, years):
        for _ in range(years):
            a *= (self.procent / 100)

        return round(a, 2)
    
balance = Deposit()
print('bank ', balance.bank(100, 2))