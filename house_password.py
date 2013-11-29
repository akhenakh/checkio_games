import string 

def checkio(data):
    if len(data) < 10:
        return False
    
    has_upper = False
    has_lower = False
    has_number = False
    
    for x in data:
        if x in string.ascii_lowercase:
            has_lower = True
        elif x in string.ascii_uppercase:
            has_upper = True
        elif x in string.digits:
            has_number = True
        
    return has_upper and has_lower and has_number

#Some hints
#Just check all conditions


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"