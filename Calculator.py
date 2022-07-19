import re

print("Our Magic Calculator")
print("Type quit to exit\n")

run=True
previous=""
equation=""

def performMath():
    global run
    global previous
    global equation

    if previous =="":
        equation = input("Enter an equation:")
        if equation == "quit":
            print("Good bye, human!\n")
            run=False
        else:
            equation = re.sub('[a-zA-Z,.;:?!@#$%¨&\|><~´`}{" "]', '', equation)
            previous = eval(equation)
            print(previous)
    else:
        cont = str(input("Continue your equation?(Y/N)"))
        if cont == "Y":
            equation = input("Continue your equation starting with the operator(+-*/**):")
            equation = re.sub('[a-zA-Z,.;:?!@#$%¨&\|><~´`}{" "]', '', equation)
            previous = eval(str(previous) + equation)
            print(previous)
        elif cont =="N":
            print("Good bye, human!\n")
            run=False
        else:
            print("Y or N please.\nRestart the program.\n")
            run=False

while run:
    performMath()

