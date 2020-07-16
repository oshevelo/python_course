def getCount():
    count = None
    while not count:
        try:
            count = int(input("Enter count. Count must > 1: "))
        except ValueError as e:
            print("Only number pleas, not stroke.\n", e)
            
        if count <= 1:
            count = None

    return count


def enterValue():
    value = None
    while not value:
        try:
            value = int(input("Enter number: "))
        except ValueError as e:
            print("Only number pleas, not stroke.\n", e)
            
    return value

def enterOperator(operator, allowedOperators):
    while not operator:
        operator = input("Enter math operator, like: +, -, *, / >>> ")
        if len(operator) > 1:
            print("Too long string, retry.\n")
            operator = None
            continue
            
        for i in allowedOperators:
            if i == operator:
                return operator
        
        print("Not math operator, retry.\n")
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
    valueList = []
    value_a = None
    value_b = None
    operator = None
    operatorsList = []
    equal = None
    allowedOperators = ["+", "-", "*", "/"]
    resultsList = None
    
    print("Hi this simple calculator, it supported next math operators: +, -, *, /\n")
    print("Try my functional!")
    
    count = getCount()

    while count:
        if len(valueList) == 0:
            valueList.append(enterValue())
            count -= 1

        operatorsList.append(enterOperator(operator, allowedOperators))
        valueList.append(enterValue())
        count -= 1
        
    for i in range(len(operatorsList)):
        if resultsList:
            resultsList = mathProcess(value_a = resultsList, operator = operatorsList[i], value_b = valueList[i+1])
        else:
            resultsList = mathProcess(value_a = valueList[i], operator = operatorsList[i], value_b = valueList[i+1])
        
    
    
    print("Greate!\n")
    print(resultsList)
    
classicCalculator()
    