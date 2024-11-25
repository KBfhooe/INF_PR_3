#Subtask 8.2:
#Code for subtask 7.4
def ListProperties(x):
    n = 0
    s = 0
    a = 0
    index = 0
    m = x[index]
    while(x[index] != -1):
        if x[index] < m:
            m = x[index]
        n += 1
        s += x[index]
        index += 1
    if n == 0:
        print("minimum = -1/nmean = -1")
    else:
        a = s/n
        print("Mean:")
        print(a)
        print("Sum:")
        print(s)
        print("Min:")
        print(m)
print("Subtask 8.2:")
#ListProperties([5,0,5,-1])
# it looks like I learned how to use git today