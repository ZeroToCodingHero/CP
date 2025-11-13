print("Better Calculator")
def main (num1,num2,operation):
    if operation == '+':
        result = num1 + num2
        print(f'{num1} + {num2} = {result}')
    elif operation == '-':
        result = num1 - num2
        print(f'{num1} - {num2} = {result}')
    elif operation == '*':
        result = num1 * num2
        print(f'{num1} * {num2} = {result}')
    elif operation == '/':
        result = num1 / num2
        print(f'{num1} / {num2} = {result}')
    else:
        print('Invaild Operator')


main()