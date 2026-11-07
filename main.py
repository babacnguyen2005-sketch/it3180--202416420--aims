from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


def main():
    cart = Cart()
    cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", 19.95))
    cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", 24.95))
    cart.add_dvd(DigitalVideoDisc("The Little Mermaid", "Animation", 18.99))
    print(f"Total cost: {cart.total_cost():.2f} $")


if __name__ == "__main__":
    main()
