def factorial(x):
    fact = 1
    for i in range (x):
        fact *= (i+1)
    

    print("factorial is : ")
    print(fact)

    

x=int(input("Enter the number whose factorial is to be found"))
factorial(x)
