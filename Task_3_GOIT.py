import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    normalize_number = []
    for el in phone_number:
        el = re.sub(r"[^\+\d]","",el)
        if re.match("^\+38", el): # порівнює шаблон з наданим номером 
            pass
        elif re.match("^38", el):
            el = "+" + el
        elif re.match("^0", el):
            el = "+38" + el
        normalize_number.append(el)
        
        
    return normalize_number
    

print(normalize_phone(raw_numbers))
        
