class PaymentService:

    TAX = 0.18
    DAILY_LIMIT = 10000

    def calculate_total(self, amount):
        if amount < 0:
            raise ValueError("Monto inválido")
        return amount * (1 + self.TAX)

    def process_payment(self, amount):
        if amount > self.DAILY_LIMIT:
            raise ValueError("Límite excedido")
        return True