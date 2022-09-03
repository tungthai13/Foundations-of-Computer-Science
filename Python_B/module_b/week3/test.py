from IPython.core.debugger import set_trace

result = 1
counter = 1
while counter < 100:
    result = result * 2
    counter = counter * 5 % result
set_trace()
raise Exception('Crashed!')