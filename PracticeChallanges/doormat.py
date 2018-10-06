num1, num2 = map(str,input().split())
num1, num2 = int(num1), int(num2)



for i in range(num1):
    for j in range(num2):
        if (i==(int(num1/2)+1)):
            dashPrint = int((num2-7)/2)
            print("-"*dashPrint+"WELCOME"+"-"*dashPrint)
        
        
            