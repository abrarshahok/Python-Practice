import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # # Required
    # parser.add_argument('num1',help='First Number')
    # parser.add_argument('num2',help='Second Number')
    # parser.add_argument('opt',help='Operator',choices=["+","-",'/','*'])

    # Optional
    parser.add_argument('--num1',help='First Number')
    parser.add_argument('--num2',help='Second Number')
    parser.add_argument('--opt',help='Operator',choices=["+","-",'/','*'])

    args = parser.parse_args()

    res = None
    num1 = int(args.num1)
    num2 = int(args.num2)
    if(args.opt == '-'):
        res = num1 - num2
    elif (args.opt == '+'):
        res = num1 + num2
    elif (args.opt == '*'):
        res = num1 - num2
    elif (args.opt == '/'):
        res = num1 / num2
    else:
        print('Unsupported operation')

    print('Result:',res)