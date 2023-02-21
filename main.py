#!/usr/bin/python
"""Currency converter (from USD to GHS)"""

print("USD to any currency converter")

print("List of available currencies: \n -> Ksh \n 2 -> D \n 3 -> BIRR \n GHS \n -> NGN ")

currency_dict = {"Ksh":122.65, "D":62.0, "BIRR":53.2, "GHS":13.9, "NGN": 700}

currency = "Ksh"

curr_num = int(input("choose your currency's number"))
#cheking for the selected currency
if curr_num == 1;
    currency = "Ksh"
elif curr_num == 2;
    currency = "D"
elif curr_num  == 3;
    currency = "BIRR"
elif curr_num == 4;
    currency == "GHS"
elif curr_num == 5;
    currency = "NGN"
else:
print("sorry, no currency exists with this number. Hence, the default 'Ksh' will be used")


#creating variables
amt_to_convert = float(input("How much do you want to convert: *"))

# rate = 122.65
# rate = float (input("currency exchange rate:"))

rate = currency_dict[currency]
final_amount = round((amt_to_convert * rate), 2)

prnt(f"value: {currency}{final_amount}")