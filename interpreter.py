expression = input("Expression: ")
# Parse variables.
x, y, z = expression.split(" ")
new_x=float(x)
new_z=float(z)
#calculate
if y == "+":
    result = new_x + new_z
if y == "-":
    result = new_x - new_z
if y == "*":
    result = new_x * new_z
if y == "/":
    result= new_x / new_z
print(round(result, 1))
   
          
    