eq1 = input("Enter the first equation: ")

eq2 = input("Enter the second equation: ")


a = len(eq1)


listeq1 = []
for i in range(a):
    listeq1.append(eq1[i])

tt = listeq1.index("=")
eq1_sliced_part1 = listeq1[:tt]
eq1_sliced_part2 = listeq1[tt:]
eq1_sliced_part2.remove("=")
eq1_sliced_part1.append(" ")
eq1_sliced_part2.append(" ")


for i in eq1_sliced_part1:
    if i != "x" and i != "y" and i != "+" and i != "-":
        index_integer = eq1_sliced_part1.index(i)
        if index_integer != len(eq1_sliced_part1) - 1:
            eq1_sliced_part1[index_integer] = int(i)
            while eq1_sliced_part1[index_integer + 1] != "x" and eq1_sliced_part1[index_integer + 1] != "y" and eq1_sliced_part1[index_integer + 1] != "+" and eq1_sliced_part1[index_integer + 1] != "-" and eq1_sliced_part1[index_integer + 1] != " ":
                d = str(eq1_sliced_part1[index_integer]) + eq1_sliced_part1[index_integer + 1]
                eq1_sliced_part1[index_integer] = int(d)
                eq1_sliced_part1.pop(index_integer + 1)
                if eq1_sliced_part1[index_integer + 1] == "x" or eq1_sliced_part1[index_integer + 1] == "y" or eq1_sliced_part1[index_integer + 1] == "+" or eq1_sliced_part1[index_integer + 1] == "-" or eq1_sliced_part1[index_integer + 1] == " ":
                    break

h = len(eq1_sliced_part1)
if eq1_sliced_part1[h - 1] != " ":
    eq1_sliced_part1.append(" ")



index_integer = 0
int_sum = 0
x_sum = 0
y_sum = 0
for i in eq1_sliced_part1:
    if i != "x" and i != "y" and i != "+" and i != "-":
      if eq1_sliced_part1.count(i) == 1:
        index_integer = eq1_sliced_part1.index(i)
        if index_integer != len(eq1_sliced_part1) - 1:
          if eq1_sliced_part1[index_integer + 1] == "x":
            if eq1_sliced_part1[index_integer - 1] == "+":
                x_sum = x_sum + int(i)
            else:
                x_sum = x_sum - int(i)
          elif eq1_sliced_part1[index_integer + 1] == "y":
            if eq1_sliced_part1[index_integer - 1] == "+":
              y_sum = y_sum + int(i)
            else:
              y_sum = y_sum - int(i)
          elif eq1_sliced_part1[index_integer + 1] != "y" and eq1_sliced_part1[index_integer + 1] != "x":
            if eq1_sliced_part1[index_integer - 1] == "+":
              int_sum = int_sum + int(i)
            elif eq1_sliced_part1[index_integer - 1] == "-":
              int_sum = int_sum - int(i)
      else:
        index_integer = eq1_sliced_part1.index(i, index_integer + 1)
        if index_integer != len(eq1_sliced_part1) - 1:
          if eq1_sliced_part1[index_integer + 1] == "x":
            if eq1_sliced_part1[index_integer - 1] == "+":
              x_sum = x_sum + int(i)
            else:
              x_sum = x_sum - int(i)
          elif eq1_sliced_part1[index_integer + 1] == "y":
            if eq1_sliced_part1[index_integer - 1] == "+":
              y_sum = y_sum + int(i)
            else:
              y_sum = y_sum - int(i)
          elif eq1_sliced_part1[index_integer + 1] != "y" and eq1_sliced_part1[index_integer + 1] != "x":
            if eq1_sliced_part1[index_integer - 1] == "+":
              int_sum = int_sum + int(i)
            elif eq1_sliced_part1[index_integer - 1] == "-":
              int_sum = int_sum - int(i)


for i in eq1_sliced_part2:
    if i != "x" and i != "y" and i != "+" and i != "-":
        index_integer = eq1_sliced_part2.index(i)
        if index_integer != len(eq1_sliced_part2) - 1:
            eq1_sliced_part2[index_integer] = int(i)
            while eq1_sliced_part2[index_integer + 1] != "x" and eq1_sliced_part2[index_integer + 1] != "y" and eq1_sliced_part2[index_integer + 1] != "+" and eq1_sliced_part2[index_integer + 1] != "-" and eq1_sliced_part2[index_integer + 1] != " ":
                d = str(eq1_sliced_part2[index_integer]) + eq1_sliced_part2[index_integer + 1]
                eq1_sliced_part2[index_integer] = int(d)
                eq1_sliced_part2.pop(index_integer + 1)
                if eq1_sliced_part2[index_integer + 1] == "x" or eq1_sliced_part2[index_integer + 1] == "y" or eq1_sliced_part2[index_integer + 1] == "+" or eq1_sliced_part2[index_integer + 1] == "-" or eq1_sliced_part2[index_integer + 1] == " ":
                    break

j = len(eq1_sliced_part2)
if eq1_sliced_part2[j - 1] != " ":
    eq1_sliced_part2.append(" ")


index_integer2 = 0
int_sum2 = 0
x_sum2 = 0
y_sum2 = 0
for i in eq1_sliced_part2:
    if i != "x" and i != "y" and i != "+" and i != "-":
      if eq1_sliced_part2.count(i) == 1:
        index_integer2 = eq1_sliced_part2.index(i)
        if index_integer2 != len(eq1_sliced_part2) - 1:
          if eq1_sliced_part2[index_integer2 + 1] == "x":
            if eq1_sliced_part2[index_integer2 - 1] == "+":
                x_sum2 = x_sum2 + int(i)
            else:
                x_sum2 = x_sum2 - int(i)
          elif eq1_sliced_part2[index_integer2 + 1] == "y":
            if eq1_sliced_part2[index_integer2 - 1] == "+":
              y_sum2 = y_sum2 + int(i)
            else:
              y_sum2 = y_sum2 - int(i)
          elif eq1_sliced_part2[index_integer2 + 1] != "y" and eq1_sliced_part2[index_integer2 + 1] != "x":
            if eq1_sliced_part2[index_integer2 - 1] == "+":
              int_sum2 = int_sum2 + int(i)
            elif eq1_sliced_part2[index_integer2 - 1] == "-":
              int_sum2 = int_sum2 - int(i)
      else:
        index_integer2 = eq1_sliced_part2.index(i, index_integer2 + 1)
        if index_integer2 != len(eq1_sliced_part2) - 1:
          if eq1_sliced_part2[index_integer2 + 1] == "x":
            if eq1_sliced_part2[index_integer2 - 1] == "+":
              x_sum2 = x_sum2 + int(i)
            else:
              x_sum2 = x_sum2 - int(i)
          elif eq1_sliced_part2[index_integer2 + 1] == "y":
            if eq1_sliced_part2[index_integer2 - 1] == "+":
              y_sum2 = y_sum2 + int(i)
            else:
              y_sum2 = y_sum2 - int(i)
          elif eq1_sliced_part2[index_integer2 + 1] != "y" and eq1_sliced_part2[index_integer2 + 1] != "x":
            if eq1_sliced_part2[index_integer2 - 1] == "+":
              int_sum2 = int_sum2 + int(i)
            elif eq1_sliced_part2[index_integer2 - 1] == "-":
              int_sum2 = int_sum2 - int(i)
print("Equations in the simplified form:")
if y_sum-y_sum2>=0:
  print( str(x_sum-x_sum2)+"x" + "+" +str(y_sum-y_sum2) + "y" + "=" + str(int_sum2-int_sum))
else:
  print(str(x_sum-x_sum2)+"x" + str(y_sum-y_sum2) + "y" + "=" + str(int_sum2-int_sum))


b = len(eq2)


listeq2 = []
for i in range(b):
    listeq2.append(eq2[i])

gg = listeq2.index("=")
eq2_sliced_part1 = listeq2[:gg]
eq2_sliced_part2 = listeq2[gg:]
eq2_sliced_part2.remove("=")
eq2_sliced_part1.append(" ")
eq2_sliced_part2.append(" ")


for i in eq2_sliced_part1:
    if i != "x" and i != "y" and i != "+" and i != "-":
        index_integer = eq2_sliced_part1.index(i)
        if index_integer != len(eq2_sliced_part1) - 1:
            eq2_sliced_part1[index_integer] = int(i)
            while eq2_sliced_part1[index_integer + 1] != "x" and eq2_sliced_part1[index_integer + 1] != "y" and eq2_sliced_part1[index_integer + 1] != "+" and eq2_sliced_part1[index_integer + 1] != "-" and eq2_sliced_part1[index_integer + 1] != " ":
                d = str(eq2_sliced_part1[index_integer]) + eq2_sliced_part1[index_integer + 1]
                eq2_sliced_part1[index_integer] = int(d)
                eq2_sliced_part1.pop(index_integer + 1)
                if eq2_sliced_part1[index_integer + 1] == "x" or eq2_sliced_part1[index_integer + 1] == "y" or eq2_sliced_part1[index_integer + 1] == "+" or eq2_sliced_part1[index_integer + 1] == "-" or eq2_sliced_part1[index_integer + 1] == " ":
                    break

k = len(eq2_sliced_part1)
if eq2_sliced_part1[k - 1] != " ":
    eq2_sliced_part1.append(" ")

index_integer3 = 0
int_sum3 = 0
x_sum3 = 0
y_sum3 = 0
for i in eq2_sliced_part1:
    if i != "x" and i != "y" and i != "+" and i != "-":
      if eq2_sliced_part1.count(i) == 1:
        index_integer3 = eq2_sliced_part1.index(i)
        if index_integer3 != len(eq2_sliced_part1) - 1:
          if eq2_sliced_part1[index_integer3 + 1] == "x":
            if eq2_sliced_part1[index_integer3 - 1] == "+":
                x_sum3 = x_sum3 + int(i)
            else:
                x_sum3 = x_sum3 - int(i)
          elif eq2_sliced_part1[index_integer3 + 1] == "y":
            if eq2_sliced_part1[index_integer3 - 1] == "+":
              y_sum3 = y_sum3 + int(i)
            else:
              y_sum3 = y_sum3 - int(i)
          elif eq2_sliced_part1[index_integer3 + 1] != "y" and eq2_sliced_part1[index_integer3 + 1] != "x":
            if eq2_sliced_part1[index_integer3 - 1] == "+":
              int_sum3 = int_sum3 + int(i)
            elif eq2_sliced_part1[index_integer3 - 1] == "-":
              int_sum3 = int_sum3 - int(i)
      else:
        index_integer3 = eq2_sliced_part1.index(i, index_integer3 + 1)
        if index_integer3 != len(eq2_sliced_part1) - 1:
          if eq2_sliced_part1[index_integer3 + 1] == "x":
            if eq2_sliced_part1[index_integer3 - 1] == "+":
              x_sum3 = x_sum3 + int(i)
            else:
              x_sum3 = x_sum3 - int(i)
          elif eq2_sliced_part1[index_integer3 + 1] == "y":
            if eq2_sliced_part1[index_integer3 - 1] == "+":
              y_sum3 = y_sum3 + int(i)
            else:
              y_sum3 = y_sum3 - int(i)
          elif eq2_sliced_part1[index_integer3 + 1] != "y" and eq2_sliced_part1[index_integer3 + 1] != "x":
            if eq2_sliced_part1[index_integer3 - 1] == "+":
              int_sum3 = int_sum3 + int(i)
            elif eq2_sliced_part1[index_integer3 - 1] == "-":
              int_sum3 = int_sum3- int(i)

for i in eq2_sliced_part2:
    if i != "x" and i != "y" and i != "+" and i != "-":
        index_integer = eq2_sliced_part2.index(i)
        if index_integer != len(eq2_sliced_part2) - 1:
            eq2_sliced_part2[index_integer] = int(i)
            while eq2_sliced_part2[index_integer + 1] != "x" and eq2_sliced_part2[index_integer + 1] != "y" and eq2_sliced_part2[index_integer + 1] != "+" and eq2_sliced_part2[index_integer + 1] != "-" and eq2_sliced_part2[index_integer + 1] != " ":
                d = str(eq2_sliced_part2[index_integer]) + eq2_sliced_part2[index_integer + 1]
                eq2_sliced_part2[index_integer] = int(d)
                eq2_sliced_part2.pop(index_integer + 1)
                if eq2_sliced_part2[index_integer + 1] == "x" or eq2_sliced_part2[index_integer + 1] == "y" or eq2_sliced_part2[index_integer + 1] == "+" or eq2_sliced_part2[index_integer + 1] == "-" or eq2_sliced_part2[index_integer + 1] == " ":
                    break

l = len(eq2_sliced_part2)
if eq2_sliced_part2[l - 1] != " ":
    eq2_sliced_part2.append(" ")

index_integer4 = 0
int_sum4 = 0
x_sum4 = 0
y_sum4 = 0
for i in eq2_sliced_part2:
    if i != "x" and i != "y" and i != "+" and i != "-":
      if eq2_sliced_part2.count(i) == 1:
        index_integer4 = eq2_sliced_part2.index(i)
        if index_integer4 != len(eq2_sliced_part2) - 1:
          if eq2_sliced_part2[index_integer4 + 1] == "x":
            if eq2_sliced_part2[index_integer4 - 1] == "+":
                x_sum4 = x_sum4 + int(i)
            else:
                x_sum4 = x_sum4 - int(i)
          elif eq2_sliced_part2[index_integer4 + 1] == "y":
            if eq2_sliced_part2[index_integer4 - 1] == "+":
              y_sum4 = y_sum4 + int(i)
            else:
              y_sum4 = y_sum4 - int(i)
          elif eq2_sliced_part2[index_integer4 + 1] != "y" and eq2_sliced_part2[index_integer4 + 1] != "x":
            if eq2_sliced_part2[index_integer4 - 1] == "+":
              int_sum4 = int_sum4 + int(i)
            elif eq2_sliced_part2[index_integer4 - 1] == "-":
              int_sum4 = int_sum4 - int(i)
      else:
        index_integer4 = eq2_sliced_part2.index(i, index_integer4 + 1)
        if index_integer4 != len(eq2_sliced_part2) - 1:
          if eq2_sliced_part2[index_integer4 + 1] == "x":
            if eq2_sliced_part2[index_integer4 - 1] == "+":
              x_sum4 = x_sum4 + int(i)
            else:
              x_sum4 = x_sum4 - int(i)
          elif eq2_sliced_part2[index_integer4 + 1] == "y":
            if eq2_sliced_part2[index_integer4 - 1] == "+":
              y_sum4 = y_sum4 + int(i)
            else:
              y_sum4 = y_sum4 - int(i)
          elif eq2_sliced_part2[index_integer4 + 1] != "y" and eq2_sliced_part2[index_integer4 + 1] != "x":
            if eq2_sliced_part2[index_integer4 - 1] == "+":
              int_sum4 = int_sum4 + int(i)
            elif eq2_sliced_part2[index_integer4 - 1] == "-":
              int_sum4 = int_sum4- int(i)

if y_sum3-y_sum4>=0:
  print(str(x_sum3-x_sum4)+"x" + "+" + str(y_sum3-y_sum4) + "y" + "=" + str(int_sum3-int_sum4))
else:
  print(str(x_sum3-x_sum4)+"x" + str(y_sum3-y_sum4) + "y" + "=" + str(int_sum4-int_sum3))


print("Solution:")
v=(y_sum-y_sum2)/(y_sum3-y_sum4)
print("x"+"="+str(int((int_sum2-int_sum-v*int_sum4+v*int_sum3)/(-v*x_sum3+v*x_sum4-x_sum2+x_sum))))

q=(x_sum-x_sum2)/(x_sum3-x_sum4)
print("y"+"="+str(int((int_sum2-int_sum-q*int_sum4+q*int_sum3)/(-q*y_sum3+q*y_sum4-y_sum2+y_sum))))