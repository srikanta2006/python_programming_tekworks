s_name=input("Enter the name of the consumer ")
s_number=int(input("Enter the number of the consumer "))
cm_units, lm_units=map(int, input("Enter the current month reading and last month reading ").split(" "))
if(cm_units<lm_units):
    print("Incorrect data")
    exit
total_units=cm_units-lm_units
bill_amt=total_units*3.80
#consumer details
print("CONSUMER DETAILS")
print("Name:-", s_name)
print("Number:-", s_number)
print("Total_units consumed:-", total_units)
print("Bill amount:-", round(bill_amt, 2))