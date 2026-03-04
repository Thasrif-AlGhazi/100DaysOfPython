def is_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

for i in range(15, 34):
    is_even(i)
for i in range(153, 219):
    is_even(i)

def calculate_area(length, width):
    # Write your code below
    return length * width

length = float(input())
width = float(input())
# Call the function below
result=calculate_area(length,width)
print(result)