class CoffeeOrder:
    def __init__(self, customer, type, price, extra_shot):
        self.customer = customer
        self.type = type
        self.price = price
        self.extra_shot = extra_shot

    def price(self):
        order_price = self.price
        if self.extra_shot:
            order_price += 5000
        return order_price

    def get_detail(self):
        status = "Ha" if self.kuchli_kofe else "Yo'q"
        print(f"Mijoz: {self.customer} | Ichimlik: {self.type} | Kuchli: {status} | Narxi: {self.price()} so'm")

orders = []

while True:
    print("\n--- KOFE DO'KONI TIZIMI ---")
    print("1. Yangi buyurtma qo'shish")
    print("2. Barcha buyurtmalarni ko'rish (Ishchi uchun)")
    print("3. Jami tushumni ko'rish (Ishchi uchun)")
    print("4. Chiqish")
    
    tanlov = input("Tanlovingizni kiriting: ")

    if tanlov == "1":
        customer = input("Ismingiz nima? ")
        type = input("Qanday kofe ichasiz? (Latte/Espresso): ")
        price = int(input("Kofe narxi qancha? "))
        extra_shot = input("Kuchli bo'lsinmi? (yes/no): ").lower() == "yes"
        
        new_order = CoffeeOrder(customer, type, price, extra_shot)
        orders.append(new_order)
        print("Buyurtma qabul qilindi!")

    elif tanlov == "2":
        print("\n--- BARCHA BUYURTMALAR ---")
        for order in orders:
            order.get_detail()

    elif tanlov == "3":
        tushum = sum(order.jami_narxni_hisobla() for order in orders)
        print(f"\nUmumiy tushum: {tushum} so'm")

    elif tanlov == "4":
        print("Xizmatimizdan foydalanganingiz uchun rahmat!")
        break
    
    else:
        print("Noto'g'ri tanlov, qaytadan urinib ko'ring.")