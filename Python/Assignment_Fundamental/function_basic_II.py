1#
countdown = list(range(0,6,1))
print(countdown)

countdown = []
for i in range(0,6,1):
    countdown.append(i)
print(countdown)


countdown = [0,0,0,0,0]
for i in range(0,6,1):
    countdown[i]=i
print(countdown)


2#
list1 = [1,2]
def print_and_return(i):    
    print(i[0])
    return(i[1])

print_and_return(list1)

3#
list1 = [1,2,3,4,5]
def first_plus_length():
    var = list1[1] +  


