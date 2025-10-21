print("SHOPPING CART CALCULATOR")
print("========================================")
subtotal_init = 0

def calculate_item_total(quantity, unit_price): ##
    global subtotal_init
    subtotal_init = unit_price * quantity
    return subtotal_init


def apply_bulk_discount(total, quantity):
    if quantity >= 10:
        discount = total*0.1
        return discount
    elif quantity >= 5:
        discount = total*0.05
        return discount
    else:
        discount = total*0
        return discount


def calculate_tax(subtotal, tax_rate):
    return subtotal*(tax_rate/100)


def is_eligible_for_free_shipping(subtotal):
    return subtotal >= 50

def process_order(item_name, quantity, unit_price, tax_rate):
    item_total = calculate_item_total(quantity, unit_price)
    discount = apply_bulk_discount(item_total, quantity)
    subtotal = item_total-discount
    tax = calculate_tax(item_total-discount, tax_rate)
    final_total = item_total-discount-tax
    print(f"Order Receipt for: {item_name}")
    print(f"    Quantity: {quantity} @ ${unit_price:.2f} each")
    print(f"    Item total: ${item_total:.2f}")
    if discount != 0:
        print(f"    Bulk discount: -${discount:.2f}")
    print(f"    Subtotal: ${subtotal}")
    print(f"    Tax (8%): ${tax:.2f}")
    print(f"    Final total: ${final_total:.2f}")
    if subtotal <= 50:
        print(f"Need ${(50-subtotal):.2f} more for free shipping")
    print("---------------------------------------")


process_order("Notebook", 12, 3.5, 8)
process_order("Pens", 6, 1.25, 8)
process_order("Paper", 3, 4.99, 8)

# total_calculator = calculate_item_total(12, 3.5)
# discount_calculator = apply_bulk_discount(subtotal_init, 12)
# print(discount_calculator)
# print(subtotal_init)