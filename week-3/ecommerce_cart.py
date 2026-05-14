from abc import ABC, abstractmethod
from uuid import uuid4


class Product:
    def __init__(self, name, price, stock):
        if price < 0 or stock < 0:
            raise ValueError(
                f"Price and stock of the product can't be negative.")
        self.product_id = uuid4()
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if quantity < 0:
            raise ValueError(f"Quantity to reduce stock can't be negative.")
        if (self.stock - quantity) < 0:
            raise ValueError(
                f"Insufficient Stock: Unable to reduce quantity {quantity}.")

        self.stock -= quantity

    def restock(self, quantity):
        if quantity < 0:
            raise ValueError(f"Quantity to restock can't be negative.")

        self.stock += quantity

    def __str__(self):
        return f"Product(Name: {self.name}, Price: {self.price:.2f} Available Stock: {self.stock})"


class CartItem:
    def __init__(self, product, quantity):
        if not isinstance(product, Product):
            raise TypeError("Only Product types can be CartItem.")

        self.product = product
        self.quantity = quantity

    def subtotal(self):
        return round((self.product.price * self.quantity), 2)

    def __str__(self):
        return f"CartItem(Product: {self.product.name}, Price: {self.product.price}, Quantity: {self.quantity}, Subtotal: {self.subtotal():.2f})"


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        if not isinstance(product, Product):
            raise TypeError("Only Product types can be added to the Cart.")

        for item in self.items:
            if item.product.product_id == product.product_id:
                updated_quantity = item.quantity + quantity
                if updated_quantity > item.product.stock:
                    raise ValueError(
                        f"Insufficient Stock: Unable to add {quantity} item(s) of {product.name}.")
                item.quantity = updated_quantity
                print(
                    f"{quantity} item(s) of the product {product.name} added to the Cart.")
                break
        else:
            if quantity > product.stock:
                raise ValueError(
                    f"Insufficient Stock: Unable to add {quantity} item(s) of {product.name}.")
            cart_item = CartItem(product, quantity)
            self.items.append(cart_item)
            print(
                f"{quantity} item(s) of the product {product.name} added to the Cart.")

    def remove_item(self, product_id):
        for index, item in enumerate(self.items):
            if item.product.product_id == product_id:
                del self.items[index]
                print(f"{item.product.name} removed from the Cart.")
                break
        else:
            raise ValueError("Product to be removed is not in the Cart.")

    def update_quantity(self, product_id, quantity):
        for item in self.items:
            if item.product.product_id == product_id:
                if quantity > item.product.stock:
                    raise ValueError(
                        f"Insufficient Stock: Unable to update quantity to {quantity}.")
                item.quantity = quantity
                print(
                    f"Quantity of the product {item.product.name} updated to {quantity} item(s)")
                break
        else:
            raise ValueError("Product to be updated is not in the Cart.")

    def total(self):
        return round(sum(item.subtotal() for item in self.items), 2)

    def item_count(self):
        return sum(item.quantity for item in self.items)

    def display(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print(
                f"{'S.No':<4} {'Product Name':<30} {'Price':>7} {'Quantity':>10} Subtotal")
            for index, item in enumerate(self.items, start=1):
                print(
                    f"{index:<4} {item.product.name:<30} {item.product.price:>7} {item.quantity:>10} {item.subtotal():>8} AED")

            print('-' * 80)
            print(f"{' ' * 43} {self.item_count():>10} {self.total():>8} AED")

    def clear(self):
        self.items = []


class Order:
    def __init__(self, cart, status="pending"):
        if not isinstance(cart, Cart):
            raise TypeError("Only Cart can be added to the Order")
        self.order_id = uuid4()
        self.cart = cart
        self.status = status

    def place_order(self):
        if not self.cart.items:
            raise ValueError("Cart is empty.")

        if self.status != "pending":
            raise ValueError("Only 'pending' orders could be placed.")

        items = self.cart.items

        for item in items:
            item.product.reduce_stock(item.quantity)
        self.status = "confirmed"
        print("Order placed.")

    def cancel_order(self):
        if self.status not in ("pending", "confirmed"):
            raise ValueError(
                "Only 'pending' or 'confirmed' orders can be cancelled.")
        items = self.cart.items
        for item in items:
            item.product.restock(item.quantity)

        self.status = "cancelled"
        print("Order cancelled.")

    def __str__(self):
        return f"Order(Order Id: {self.order_id}, Status: {self.status})"


class Discount(ABC):
    @abstractmethod
    def apply(self, total):
        pass


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        if percentage < 0:
            raise ValueError("Discount percentage can't be negative.")
        self.percentage = percentage

    def apply(self, total):
        return total * (1 - self.percentage / 100)


class FixedDiscount(Discount):
    def __init__(self, amount):
        if amount < 0:
            raise ValueError("Discount amount can't be negative.")
        self.amount = amount

    def apply(self, total):
        return max(0, total - self.amount)


class Checkout:
    def __init__(self, cart, discount=FixedDiscount(0)):
        if not isinstance(discount, Discount):
            raise TypeError("discount must of type Discount.")
        if not isinstance(cart, Cart):
            raise TypeError("cart must be of type Cart.")
        self.cart = cart
        self.discount = discount

    def final_total(self):
        total = self.discount.apply(self.cart.total())

        return round(total, 2)

    def process(self, order):
        if not isinstance(order, Order):
            raise TypeError("order must be of type Order.")

        if order.status == "confirmed":
            self.cart.display()

            total = self.cart.total()
            discount_amount = total - self.discount.apply(total)

            print(f"Discount: {discount_amount:.2f} AED")
            print(f"Final Total: {self.final_total():.2f} AED")
        else:
            print("Order must be placed before checkout process.")


def main():
    try:
        keyboard = Product("Keychron Mechanical Keyboard", 735, 42)
        mouse = Product("Logitech MX Master Mouse", 399, 115)
        macbook = Product("Apple MacBook Pro 16", 12999, 15)
        monitor = Product("LG 4K Monitor", 2199, 28)
        raspberry_pi = Product("Raspberry Pi 5", 320, 67)
        chair = Product("Autonomous ErgoChair", 1850, 11)
        monitor_light = Product("BenQ Monitor Light", -2, -4)
    except ValueError as e:
        print(e)

    cart = Cart()
    try:
        cart.add_item(keyboard, 21)
        cart.add_item(keyboard, 4)
        cart.add_item(mouse, 10)
        cart.add_item(macbook, 2)
        cart.add_item(monitor, 6)
        cart.add_item(raspberry_pi, 18)
        cart.add_item(chair, 4)
        cart.update_quantity(keyboard.product_id, 10)
    except ValueError as e:
        print(e)

    cart.display()

    order = Order(cart)
    order.place_order()

    checkout = Checkout(cart, PercentageDiscount(10))
    checkout.process(order)


if __name__ == "__main__":
    main()
