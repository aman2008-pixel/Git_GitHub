# Product catalogue (dictionary): name -> price in Rs.
CATALOGUE = {
    "Rice": 50,
    "Sugar": 40,
    "Oil": 120,
}

GST_RATE = 0.05          # 5% of subtotal
BILL_FILE = "bill.txt"   # file the final bill is saved to


def find_product(name):
    """Return the catalogue key matching `name` (case-insensitive), else None."""
    for product in CATALOGUE:
        if product.lower() == name.strip().lower():
            return product
    return None


def add_item(bill, name, quantity):
    """Validate and add an item to the bill (a list). Returns True if added."""
    product = find_product(name)
    if product is None:
        print("Invalid product. Available: " + ", ".join(CATALOGUE))
        return False

    try:
        quantity = int(quantity)
    except ValueError:
        print("Quantity must be at least 1.")
        return False

    if quantity < 1:
        print("Quantity must be at least 1.")
        return False

    amount = CATALOGUE[product] * quantity
    bill.append({"name": product, "qty": quantity, "price": CATALOGUE[product], "amount": amount})
    print(f"{product} x{quantity} added | Amount: {amount}")
    return True


def calculate_totals(bill):
    """Return (subtotal, gst, grand_total) for the items in the bill."""
    subtotal = sum(item["amount"] for item in bill)
    gst = subtotal * GST_RATE
    return subtotal, gst, subtotal + gst


def view_bill(bill):
    """Print the items added so far."""
    if not bill:
        print("No items in the bill yet.")
        return
    print("\nItems so far:")
    for item in bill:
        print(f"  {item['name']} x{item['qty']} = {item['amount']}")
    print()


def build_bill_text(bill, customer):
    """Build the neatly formatted bill as a string."""
    subtotal, gst, grand_total = calculate_totals(bill)
    line = "=" * 40
    out = [line, "            YOUR BILL", line]
    out.append(f"Customer: {customer}")
    out.append("-" * 40)
    out.append(f"{'Item':<12}{'Qty':>5}{'Price':>10}{'Amount':>11}")
    out.append("-" * 40)
    for item in bill:
        out.append(f"{item['name']:<12}{item['qty']:>5}{item['price']:>10}{item['amount']:>11}")
    out.append("-" * 40)
    out.append(f"{'Subtotal:':<27}{subtotal:>13.2f}")
    out.append(f"{'GST (5%):':<27}{gst:>13.2f}")
    out.append(f"{'Grand Total:':<27}{grand_total:>13.2f}")
    out.append(line)
    out.append("        Thank you! Visit again.")
    out.append(line)
    return "\n".join(out)


def generate_bill(bill, customer):
    """Print the final bill, show totals and save it to bill.txt."""
    if not bill:
        print("Cannot generate bill: no items added.")
        return False

    subtotal, gst, grand_total = calculate_totals(bill)
    for item in bill:
        print(f"{item['name']} x{item['qty']} = {item['amount']}")
    print(f"Subtotal: {subtotal:g} | GST (5%): {gst:.2f}")
    print(f"Grand Total: {grand_total:.2f}\n")

    text = build_bill_text(bill, customer)
    print(text)

    try:
        with open(BILL_FILE, "w") as f:
            f.write(text + "\n")
        print(f"\nBill saved to {BILL_FILE}")
    except OSError as err:
        print(f"Could not save bill: {err}")
        return False
    return True


def main():
    bill = []
    customer = input("Customer name: ").strip() or "Walk-in Customer"

    while True:
        print("\n--- MENU ---")
        print("1. Add item")
        print("2. View bill")
        print("3. Generate bill")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("Available: " + ", ".join(f"{p} (Rs.{c})" for p, c in CATALOGUE.items()))
            name = input("Add item: ")
            quantity = input("Quantity: ")
            add_item(bill, name, quantity)
        elif choice == "2":
            view_bill(bill)
        elif choice == "3":
            if generate_bill(bill, customer):
                break
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
