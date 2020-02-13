# Exception handling
def division(a,b):
    try:   # try to run this code, whenever you face issue - you execute except block
        if type(a)==str or type(b)==str:
            return int(a)/int(b)
        return a/b
    except ZeroDivisionError as zde:
        print(zde)
        return f"You cannot devide to zero"
    except:     # except anything else
        return f"please check your input."
    
    
def division2(a,b):
    """ Function without exception"""
    if type(a)==str or type(b)==str:
        return int(a)/int(b)
    return a/b
    

## Testing your code
print(division(45,90))
print(division(-45,90))
print(division('45',90))
print(division('45',0))
print(division('45','90'))
print(division('John', 'Doe'))


print('=======')

print(division2(45,90))
print(division2('45',0)) # Without exception execution stopped on this line and didn't go further
print(division2(-45,90))
print(division2('45',90))
print(division2('45','90'))