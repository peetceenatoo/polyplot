def p(x):
    sum = 0
    for k in range(0, degree+1):
        sum += x**k * coefficients[degree-k]
    return sum

degree = int(input("Enter polynomial degree: "))
toPlot = int(input("Enter the number of points to plot: "))

coefficients = []
oldt = [0 for i in range(0, degree)] 
newt = [0 for i in range(0, degree)]
constants = []

print()
print("You are now required to enter coefficients starting from the one which multiplies x^" + str(degree) + "...")
for i in range(0, degree+1):
    temp = int(input("Enter coefficient n." + str(i+1) + ": "))
    coefficients.append(temp)
print()

constants.append(coefficients[degree])
for i in range(1, degree+1):
    newt[0] = p(i) - p(i-1)
    for k in range(1, i):
        newt[k] = newt[k-1] - oldt[k-1]
        oldt[k-1] = newt[k-1]
    constants.append(newt[i-1])
    oldt[i-1] = newt[i-1]

for i in range(0,degree):
    newt[i] = constants[i+1]

plotted = []
plotted.append(p(0))
print("The algorythm for x = 0 returns " + str(plotted[-1]))
for i in range(0, toPlot-1):
    plotted.append(plotted[-1]+newt[0])
    print("The algorythm for x = " + str(i+1) + " returns " + str(plotted[-1]))
    for k in range(0, degree-1):
        newt[k] += newt[k+1]




