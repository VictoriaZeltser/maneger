class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}
    def add_items(self,item_name, price):
        self.items[item_name] = price
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
    def get_price(self, item_name):
        return self.items.get(item_name, None)
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price


super1 = Store("Ветер","Cолнечная 25")
super2 = Store("Солнце", "Фестивальный 16")
super3 = Store("Теремок", "Загородная 12")

super1.add_items("apples", 0.5)
super1.add_items("bananas", 0.75)

super2. add_items("ananas", 0.96)
super2. add_items("pear", 0.43)

super3. add_items("tomatoes", 0.23)
super3. add_items("potato", 0.37)

print(f"Initial items in {super1.name}: {super1.items}")

super1.add_items("orandes", 0.67)
super1.add_items("cherry", 0.86)
print(f"After adding oranges and cherry: {super1.items}")


# Обновляем цену товара
super1.update_price("apples", 0.55)
print(f"After price update for apples: {super1.items}")

# Удаляем товар
super1.remove_item("bananas")
print(f"After removing bananas: {super1.items}")

# Получаем цену товара
price_of_apples = super1.get_price("apples")
print(f"Price of apples: {price_of_apples}")

# Пытаемся получить цену несуществующего товара
price_of_peaches = super1.get_price("peaches")
print(f"Price of peaches: {price_of_peaches}")


