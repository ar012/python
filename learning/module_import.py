#import my_math.arith.ops as my_ops

from my_math.arith import ops

from my_math.geo import square


#sum = my_math.arith.ops.add(5, 10)
#sum = my_ops.add(5, 10)

sum = ops.add(5, 10)
print(sum)


area = square.area(3)
print(area)