import math
from collections import namedtuple

#Q1a
def cal_square_root(numb):
    start = numb
    if start > 0:
        base10 = int(math.log10(start))
        if base10 == 0:
            approx_root = 1
        else:
            approx_root = (10**base10)/10
        n = 0
        while n < start:
            n = approx_root**2
            approx_root += 1
        
        quotient = start / approx_root
        mean = (approx_root + quotient)/2

        while round(quotient,6) != round(approx_root,6):
            approx_root = mean
            quotient = start / approx_root
            mean = (approx_root + quotient)/2
        
        return approx_root
    else:
        approx_root = 0
        return approx_root

print('Question 1a',cal_square_root(159))

# Q1b / Q1c
arr_tup = []
arr_sqrt = []
namedtup = namedtuple('Output', ['value','sqrt'])
my_list = [159,3400,67,598,8999]
for each_numb in my_list:
    sqr = cal_square_root(each_numb) 
    arr_sqrt.append(sqr)#Answer 1b
    new_numb = namedtup(each_numb, sqr)
    arr_tup.append(new_numb) #Answer 1c

print('Question 1b',arr_sqrt)
print('Question 1c',arr_tup)

# Q2a

class SquareRoot:

    def __init__(self, value):
        self.value = value
       
    def calculate_square_root(self):
        return cal_square_root(self.value)
        
        
# Q2b
my_class = SquareRoot(159).calculate_square_root()
print('Qestion 2b', my_class)
