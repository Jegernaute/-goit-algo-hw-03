import re

raw_numbers = input("Please enter your phone`s number: ")

def normalize_phone(phone_number):
    
    phone_number = re.sub(r"[^\+\d]","",phone_number)
    if re.match("^\+38", phone_number): # порівнює шаблон з наданим номером 
        pass
    elif re.match("^38", phone_number):
        phone_number = "+" + phone_number
    elif re.match("^0", phone_number):
        phone_number = "+38" + phone_number
    
        
        
    return phone_number
    

print(normalize_phone(raw_numbers))
        
