def odd_even():
    evenodd = ""
    for i in range (1, 201):
        string = str(i)
        if i%2 > 0:
            evenodd = "odd"
        else:
            evenodd = "even"
        print "Number is " + string + ". This is an " + evenodd + " number."

"""odd_even()        
"""

a = [2,4,10,16]
def multiply(list, multiplier):
    new_list = []
    for i in range(0, len(list)):
        new_list.append(list[i]*multiplier)
    return new_list    

"""a = [2,4,10,16]
b = multiply(a, 5)
print b"""


def layered_multiples(arr):
    # your code here
    new_array = []
    one_list = []
    for index in arr:
        value = int(index)
        for i in range(value):
            one_list.append(1)
        new_array.append(one_list)
        one_list = []
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
""">>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]"""


