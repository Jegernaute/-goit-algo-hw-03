import re

raw_numbers = input("Please enter your phone`s number: ")

def normalize_phone(phone_number):
    
    phone_number = re.sub(r"[^\+\d]","",phone_number)
    len_string = len(phone_number)
    if phone_number.startswith("0") or phone_number.startswith("+") or phone_number.startswith("3") :
        if len_string == 13 and re.match("^\+38", phone_number): # порівнює шаблон з наданим номером 
            pass
        elif len_string == 12 and re.match("^38", phone_number):
            phone_number = "+" + phone_number
        elif len_string == 10 and re.match("^0", phone_number):
            phone_number = "+38" + phone_number
        else:
            return "Incorrect number of digits or number format"  
    else:
        return "Incorrect number format"
    
    return phone_number
 

print(normalize_phone(raw_numbers))
        
