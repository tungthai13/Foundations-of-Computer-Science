from IPython.core.debugger import set_trace
# A program to add all even numbers between 0 and 20 (inclusive)

sum = 0
x = 0
i = 20
while i>0:
    set_trace()
    if i%2:
        sum += i
    i-=1
print(sum)
