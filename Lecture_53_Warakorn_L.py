def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
price = int (input(" Price Number "))
print("Price+Vat = " , vatCalculate(price))