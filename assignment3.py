print("[Multiplication Chart]")
print("\nmultiplicant x multiplier")
multiplicand = int(input("\nEnter multiplicand: "))
multiplier = int(input("Enter multiplier length [1 to n]: "))
length = multiplier + 1
result = []
for number in range(1,length):
    product = number * multiplicand
    result.append(product)
print(f"Result: {result}")
