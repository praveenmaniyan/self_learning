import numpy as np
from scipy.linalg import solve

input_layer = np.array([1,2,3])

hidden_layer_1 = np.array([1,1,-5])

hidden_layer_2 = np.array([3,-4,2])

out_layer = np.array([2,-1])

node_1 = input_layer[0] * hidden_layer_1[0] + input_layer[1] * hidden_layer_1[1] + + input_layer[2] * hidden_layer_1[2]
node_2 = input_layer[0] * hidden_layer_2[0] + input_layer[1] * hidden_layer_2[1] + + input_layer[2] * hidden_layer_2[2]

print node_1
print node_2

node_3 = node_1 * out_layer[0] + node_2 * out_layer[1]

print node_3

dot1 = np.dot(input_layer, hidden_layer_1)
dot2 = np.dot(input_layer, hidden_layer_2)

print dot1
print dot2

for input_layer in np.array([[1,1],[0.5,0.5],[0.25,0.25],[-2,15]]):
# input_layer = np.array([1,1])
	print "New\n\n"
	hidden_layer_1 = np.array([3,2])

	hidden_layer_2 = np.array([-1,4])

	hidden_layer_3 = np.array([3,-5])

	dot1 = np.dot(input_layer, hidden_layer_1)
	dot2 = np.dot(input_layer, hidden_layer_2)
	dot3 = np.dot(input_layer, hidden_layer_3)

	print dot1
	print dot2
	print dot3

# print "New\n\n"

# input_layer = np.array([0.45,0.45])

# hidden_layer_1 = np.array([3,2])

# hidden_layer_2 = np.array([-1,4])

# hidden_layer_3 = np.array([3,-5])

# dot1 = np.dot(input_layer, hidden_layer_1)
# dot2 = np.dot(input_layer, hidden_layer_2)
# dot3 = np.dot(input_layer, hidden_layer_3)

# print dot1
# print dot2
# print dot3
import numpy as np
from scipy.linalg import solve

a = np.array([[3,2],[-1,4],[3,-5]])
b = np.array([1,2,-1])
#x ,resd, rnk, s = np.linalg.lstsq(a,b)
x = solve(a,b)

print x
print resd
print rnk
print s

# x_1 = np.allclose(np.dot(a,x), b)

# print x_1