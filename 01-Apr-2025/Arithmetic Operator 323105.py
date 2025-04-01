# Problem: Arithmetic Operator - https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    operations = {'+':lambda x, y : x + y, 
                  '-':lambda x, y : x - y,
                  '*':lambda x, y : x * y}
    for op in operations:
        print(operations[op](a, b))