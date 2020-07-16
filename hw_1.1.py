def enterValue(value):
    while not value:
        try:
            value = int(input("Enter number: "))
        except ValueError as e:
            print("Only number pleas, not stroke.", e)
            
    return value

def enterOperator(operator, operatorsList):
    while not operator:
        operator = input("Enter math operator, like: +, -, *, / >>> ")
        if len(operator) > 1:
            print("Too long string, retry.")
            operator = None
            continue
            
        for i in operatorsList:
            if i == operator:
                return operator
        
        print("Not math operator, retry.")
        operator = None
        continue

def mathProcess(value_a, operator, value_b):
    if operator == "+":
        equal = value_a + value_b
    elif operator == "-":
        equal = value_a - value_b
    elif operator == "*":
        equal = value_a * value_b
    else:
        equal = value_a / value_b
    
    return equal
    
    
def classicCalculator():
    
    value = None
    value_a = None
    value_b = None
    operator = None
    equal = None
    operatorsList = ["+", "-", "*", "/"]
    
    print("Hi this simple calculator, it supported next math operators: +, -, *, /")
    print("Try my functional!")
    
    value_a = enterValue(value)
    value = None
    operator = enterOperator(operator, operatorsList)
    value_b = enterValue(value)
    equal = mathProcess(value_a, operator, value_b)
    
    
    print("Greate!")
    print(value_a, operator, value_b, "=", equal)
    
classicCalculator()
    