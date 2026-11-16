# Summary: Simple Billing System (PS No. 34)

## Problem Statement

Develop a console billing system for a small shop where the cashier adds products with quantities for a customer and generates a bill with subtotal, GST and grand total. The bill is saved to a file.

Products: Rice Rs.50, Sugar Rs.40, Oil Rs.120. GST is 5% of the subtotal. The bill is saved to `bill.txt`.

## How It Is Implemented

**Data structures**

- `CATALOGUE` is a dictionary mapping product name to price.
- `bill` is a list. Each entry is a dictionary holding the item name, quantity, price and amount.

**Functions**

| Function | Purpose |
|----------|---------|
| `find_product(name)` | Matches the product name against the catalogue (case-insensitive) |
| `add_item(bill, name, quantity)` | Validates the product and quantity, then adds the item to the bill |
| `calculate_totals(bill)` | Returns subtotal, GST (5%) and grand total |
| `view_bill(bill)` | Prints the items added so far |
| `build_bill_text(bill, customer)` | Builds the neatly formatted bill |
| `generate_bill(bill, customer)` | Prints the bill and saves it to `bill.txt` using file handling |
| `main()` | Menu loop: add item, view bill, generate bill, exit |

**Logic**

1. Ask for the customer name and show the menu.
2. On "Add item", check that the product exists in the catalogue. If not, print the list of available products.
3. Check that the quantity is a whole number and at least 1. If not, print "Quantity must be at least 1."
4. Amount = price x quantity. The item is appended to the bill list.
5. On "Generate bill", subtotal = sum of all amounts, GST = 5% of subtotal, grand total = subtotal + GST.
6. The formatted bill is printed and written to `bill.txt`.

## Test Cases

### Test Case 1: Normal Input

| Input | Expected Output |
|-------|-----------------|
| Add item: Rice, Quantity: 2 | `Rice x2 added \| Amount: 100` |

Result: Pass

Screenshots:

![Test Case 1 - adding Rice x2](screenshots/test1.png)

![Test Case 1 - viewing and generating the bill](screenshots/test1o2.png)

### Test Case 2: Boundary / Minimum Input

| Input | Expected Output |
|-------|-----------------|
| Add item: Sugar, Quantity: 1, Generate bill | `Subtotal: 40 \| GST (5%): 2.00`, `Grand Total: 42.00` |

Result: Pass

Screenshot:

![Test Case 2 - Sugar x1 bill](screenshots/test2.png)

### Test Case 3: Invalid Input

| Input | Expected Output |
|-------|-----------------|
| (a) Add item: Soap | `Invalid product. Available: Rice, Sugar, Oil` |
| (b) Add item: Rice, Quantity: 0 | `Quantity must be at least 1.` |

Result: Pass

Screenshot:

![Test Case 3 - invalid product and quantity](screenshots/test3.png)

### Test Case 4: Different Valid Scenario

| Input | Expected Output |
|-------|-----------------|
| Customer: Riya, Add Rice x2, Oil x1, Sugar x3, Generate bill | `Rice x2 = 100`, `Oil x1 = 120`, `Sugar x3 = 120`, `Subtotal: 340 \| GST (5%): 17.00`, `Grand Total: 357.00`, bill saved to `bill.txt` |

Result: Pass

Sample `bill.txt`:

```
========================================
              YOUR BILL
========================================
Customer: Riya
----------------------------------------
Item          Qty     Price     Amount
----------------------------------------
Rice            2        50        100
Oil             1       120        120
Sugar           3        40        120
----------------------------------------
Subtotal:                         340.00
GST (5%):                          17.00
Grand Total:                      357.00
========================================
        Thank you! Visit again.
========================================
```

Screenshots:

![Test Case 4 - adding Rice, Oil and Sugar](screenshots/test4.png)

![Test Case 4 - final bill saved to bill.txt](screenshots/test4o2.png)

## Screenshots

All screenshots are in the `screenshots` folder and are shown with each test case above.
