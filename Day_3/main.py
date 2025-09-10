import ecommerce_utils
cart={}
cart["Laptop"]=55000
cart["Phone"]=30000
cart["Head phones"]=2000

ecommerce_utils.generate_invoice(cart,10, 18)