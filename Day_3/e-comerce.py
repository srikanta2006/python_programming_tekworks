def add_product():
    product=input("Enter the product to add to the cart: ")
    cart.append(product)
    print("Added!")

def remove_product():
    product=input("Enter the product to remove to the cart: ")
    if(product in cart):
        cart.remove(product)
        print("removed")
    else:
        print("Product not found")

def search_product():
    product=input("Enter the product to search in the cart: ")
    if(product in cart):
        print("product in the cart")
    else:
        print("Product not found")

def number_of_products():
    print("Total number of procuts in cart:", len(cart))
def display_products():
    for item in cart:
        print(item)

def sort_cart():
    cart.sort()
    print("Cart sorted")

def clear_cart():
    cart.clear()
    print("Cart is cleared")

def option_input():
    option=0
    while(option!=8):
        option=int(input("Enter a valid option: "))
        option_search(option)
def option_search(option):
    match(option):
        case 1:
            add_product()
        case 2:
            remove_product()
        case 3:
            search_product()
        case 4:
            display_products()
        case 5:
            number_of_products()
        case 6:
            sort_cart()
        case 7:
            clear_cart()
        case _:
            print("Enter correct option!")

cart=[]
print("options:")
print("1. Add Product\n 2. Remove Product\n 3. Search Product\n 4. Display Cart\n 5. Count Products\n 6. sort cart\n 7. clear cart\n 8. exit")
option_input()
