def apply_discount(price, discount):
    return price - (discount/100) * price

def gst(price, gst_percent=18):
    return price + (gst_percent/100) * price

def generate_invoice(cart, discount_percent=0, gst_percent=18):
    subtotal = 0
    print("--------------Invoice---------------")
    for name, price in cart.items():
        print(f"{name:<15}: ₹{price}")
        subtotal += price
    print("------------------------------------")
    print(f"Subtotal: ₹{subtotal}")

    discounted_price = apply_discount(subtotal, discount_percent)
    print(f"After {discount_percent}% discount: ₹{discounted_price:.2f}")

    gst_price = gst(discounted_price, gst_percent)
    print(f"After {gst_percent}% GST: ₹{gst_price:.2f}")
    print("-------------------------------------")
    print("Thank you for shopping with us!")
