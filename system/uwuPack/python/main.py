import numbers


number1 = 0
number2 = 0
math = ""

number1 = int(input("Enter Number1 :> "))
number2 = int(input("Enter Number2 :>  "))
math = int(input("math | 1:+ | 2:- | 3:/ | 4:* | :> "))

while True:

    if math == 1:
        print(f"Number1{number1} + Number2{number2} = ",number1 + number2)
        break  

    elif math == 2:
        print(f"Number1{number1} - Number2{number2} = ",number1 - number2)
        break 

    elif math == 3:
        print(f"Number1{number1} / Number2{number2} = ",number1 / number2)
        break 

    elif math == 4:
        print(f"Number1{number1} * Number2{number2} = ",number1 * number2)
        break 