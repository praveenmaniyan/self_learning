from skimage.feature import hessian_matrix, hessian_matrix_eigvals
from skimage import io

l_leaf_img = io.imread("C:\\Users\\v-manipr.FAREAST\\Documents\\personal\\github\\self_learning\\udacity\\nanodegree\\machine_learning\\ml_foundations\\ml_capstone_project\\data\\train\\fruitcitere\\20150325_083849.jpg")

hxx, hxy, hyy = hessian_matrix(l_leaf_img, sigma=3)
i1, i2 = hessian_matrix_eigvals(hxx, hxy, hyy)

#i2 is the variable you want.

#Visualise the result
import matplotlib.pyplot as plt
plt.imshow(i2)
plt.show()