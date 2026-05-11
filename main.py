cart = {}

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))
    
    if name in cart:
        cart[name]['quantity'] += quantity
    else:
        cart[name] = {'price': price, 'quantity': quantity}
    
    print(f"{name} added to cart.")

def remove_item():
    name = input("Enter item name to remove: ")
    if name in cart:
        del cart[name]
        print(f"{name} removed.")
    else:
        print("Item not found.")

def view_cart():
    if not cart:
        print("Cart is empty.")
        return
    
    total = 0
    print("\nYour Cart:")
    for item, details in cart.items():
        subtotal = details['price'] * details['quantity']
        total += subtotal
        print(f"{item} - ₹{details['price']} x {details['quantity']} = ₹{subtotal}")
    
    print(f"Total: ₹{total}")

def checkout():
    view_cart()
    print("Thank you for shopping!")
    exit()

# Main loop
while True:
    print("\n1. Add Item\n2. Remove Item\n3. View Cart\n4. Checkout")
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        checkout()
    else:
        print("Invalid choice.")