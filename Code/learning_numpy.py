import numpy as np
# from keras.datasets import mnist


def play_with_numpy():

    # Create an array using numpy

    np_1d_array = np.array([100, 200, 300])

    # check the datatype of numpy array
    print("Data Type of the object ", type(np_1d_array))

    # Check the length of array
    print("Length of the Array ", len(np_1d_array))

    # check the shape of this array
    print("Shape of the array", np_1d_array.shape)

    # check the dimension of this array
    print("Dimension of the array ", np_1d_array.ndim)

    # check the dimension of this array
    print("Values in the array ", np_1d_array[0], np_1d_array[1], np_1d_array[2])

    print("=======================================================")
    np_2d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # check the datatype of numpy array
    print("Data Type of the object ", type(np_2d_array))

    # Check the length of array
    print("Length of the Array ", len(np_2d_array))

    # check the shape of this array
    print("Shape of the array", np_2d_array.shape)

    # check the dimension of this array
    print("Dimension of the array ", np_2d_array.ndim)

    # check the dimension of this array
    print("Values in the array ", np_2d_array[0, 0], np_2d_array[0, 1], np_2d_array[0, 2])


def add_matrix():

    matrix_1_1D = np.array([100, 200, 300])
    matrix_2_1D = np.array([200, 300, 400])

    print("Value of first matrix = ", matrix_1_1D)
    print("Value of second matrix = ", matrix_1_1D)
    print("The addition of these matrix using + operator  = ", matrix_1_1D + matrix_2_1D)
    print("The addition of these matrix using numpy add   = ", np.add(matrix_1_1D, matrix_2_1D))


def subtract_matrix():

    matrix_1_1D = np.array([100, 200, 300])
    matrix_2_1D = np.array([200, 300, 400])

    print("Value of first matrix = ", matrix_1_1D)
    print("Value of second matrix = ", matrix_1_1D)
    print("The result of these matrix using - operator  = ", matrix_2_1D - matrix_1_1D)
    print("The result of these matrix using numpy subtract = ", np.subtract(matrix_2_1D, matrix_1_1D))


def multiply_matrix():

    matrix_1_1D = np.array([100, 200, 300])
    matrix_2_1D = np.array([200, 300, 400])

    print("Value of first matrix = ", matrix_1_1D)
    print("Value of second matrix = ", matrix_1_1D)
    print("The result of these matrix using x operator  = ", matrix_2_1D * matrix_1_1D)
    print("The result of these matrix using numpy multiply = ", np.multiply(matrix_2_1D, matrix_1_1D))


def transpose_matrix():

    matrix_1_1D = np.array([100, 200, 300])
    matrix_2_1D = np.array([200, 300, 400])

    print("Value of first matrix = ", matrix_1_1D)
    print("Value of second matrix = ", matrix_1_1D)
    print("Shape of second matrix = ", matrix_1_1D)
    print("The result of these matrix using x operator  = ", matrix_2_1D.transpose())
    # print("The result of these matrix using numpy multiply = ", np.multiply(matrix_2_1D, matrix_1_1D))


def dotproduct_matrix():

    # matrix as [9,10]
    matrix_1_1D = np.array([9, 10])
    # matrix as [11]
    #           [12]
    # 9 x 11 + 10 x 12
    # 99 + 120 = 219
    matrix_2_1D = np.array([[11], [12]])

    print("Value of first matrix = ", matrix_1_1D)
    print("Shape of second matrix = ", matrix_1_1D)
    print("Value of second matrix = ", matrix_2_1D)
    print("Shape of second matrix = ", matrix_2_1D)
    output = np.dot(matrix_1_1D, matrix_2_1D)
    print("Value of dot product = ", output)
    print("Shape of dot product = ", output.shape)

    print("The result of these matrix using dot product  = ",output )
    # print("The result of these matrix using numpy multiply = ", np.multiply(matrix_2_1D, matrix_1_1D))


def slice_matrix():

    # Create the following rank 2 array with shape (3,4)
    # [[1 2 3 4]
    #  [5 6 7 8]
    #  [9 10 11 12]
    #
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 101, 11, 12]])
    # use the slicing to pull out the subarray consisting of the first 2 rows and column
    # 1 and 2, b is the following array of shape (2,2)
    # [[2 ,3]
    #  [6 ,7]]
    # In example below
    #   :2 means is two rows
    #   row1 = [1,2,3,4] and
    #   row2= [5,6,7,8]
    # 1:3 means column 1 to 3
    # [row1 , col1] = 2
    # [row1 , col2] = 3
    # [row2 , col1] = 6
    # [row3 , col2] = 7

    print("This is our original matrix ", '\n', a, '\n')

    b = a[:2, 1:3]
    print(b, '\n')

    print("This is our sliced matrix ", '\n', b, '\n')

    b = a[:3, 0:3]
    print("This is our second sliced matrix ", b, '\n')

    # if you change the data on the sliced array than it changes the original rray
    # for example
    b[0,0] = 77

    print("This is our modified matrix ", '\n', b, '\n')

    print("This is our original matrix ", '\n', b, '\n')


def int_indexing_slicing_matrix():
    
    a = np.array([[1, 2], [3, 4], [5, 6]])
    print("Here is original array :")
    print(a,'\n')

    # an example of integer array indexing
    # this gets you value at matrix location [0,0 1,1 2,0]
    # Because a[[0,1,2]] is giving you the first coordinate
    # and a[[0,1,0]] is giving you second coordinate of the matrix
    b = a[[0, 1, 2], [0, 1, 0]]
    print("Here is the value of a[[0,1,2],[0,1,0]] ")
    print(b, '\n')
    # The above example of array indexing is equal to the example below.
    c = a[0,0]
    d = a[1,1]
    e = a[2,0]
    print(c, d , e, '\n')


def create4x3matrix():

    # create an array of 4 X 3
    a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
    print(a)
    # Check what is the shape of array
    shape = a.shape
    print("Shape of array =",shape)
    size = a.size
    print("Shape of array =", size)

    # Create an array of indices
    b = np.array([0, 2, 0, 1])

    # Select one element from each row of a using the indices in b
    # (0,1,2,3) (0,2,0,2)
    print(a[np.arange(4), b])

    # print(a.dtype)

    # mutate one element from each row of a using the indices in b
    print(a)
    print("========================")
    a[np.arange(4), b] += 40
    print(a)


def bool_array_indexing():

    '''
    # Boolean Array indexing lets you pick out arbitrary elements of array.
    # Frequently this type of array are used to select the elements of an array that satisfy some condition

    :return:
    '''

    a = np.array([[1, 2], [3, 4], [5, 6]])
    print("This is the array for this example :")
    print(a)

    bool_idx = (a>2)

    print("This is the boolean index array after applying condition a > 2")
    print(bool_idx)


def adding_array():
    """
    This function will demonstrate how to use Numpy sum function for addition

    :return:
    """

    a = np.array([[1,2],[20,30]])
    print("My array is :")
    print(a)

    total_element_value = a.sum()
    print("The total of array = ", total_element_value)

    sum_col_wise = a.sum(axis=0)
    print("The sum of array col wise = ", sum_col_wise)

    sum_row_wise = a.sum(axis=1)
    print("The sum of array row wise = ", sum_row_wise)


def reshape_array():
    
    a = np.arange(8)
    print("This is newly created array using np.arange(8) ", '\n', a)
    print("Let us reshape this array ")
    a_reshape1 = a.reshape(4, 2)
    print("Reshaped this array into 4X2", '\n', a_reshape1)
    a_reshape2 = a.reshape(2, 4)
    print("Reshaped this array into 2X4", '\n', a_reshape2)

    a_reshape3D = a.reshape(2, 2 , 2)
    # 2X2 array are stacked
    # Stack 1
    # [[[0 1]
    # [2 3]]
    #  Stack 2
    # [[4 5]
    # [6 7]]]
    print("Reshaped this array as 3D array", '\n', a_reshape3D)

    a_reshape_arr = a.reshape(8, 1)
    # 8X1 array are created
    print("Reshaped this array as 3D array", '\n', a_reshape_arr)


from numpy import array

def more_on_reshape_array():

    data = [[11, 12],
            [33, 34],
            [55, 66]]

    data = array(data)

    print('Rows: %d' % data.shape[0])
    print('Columns : %d' % data.shape[1])


def numpy_as_tensors():
    """
    A tensor that contains only one number is called a scaler (or scaler tensor or 0-dimensional tensor or 0D tensor
    In NumPy float32 or float64 is called scaler tensor or scaler array

    :return:

    """
    # A tensor that contains only one number is called a scaler (or scaler tensor or 0-dimensional tensor or 0D tensor
    # In NumPy float32 or float64 is called scaler tensor or scaler array

    x = np.array(12)
    print("Here is the array created using np.array(12) ", x)
    print("Here is the dimensions of array", x.ndim)

    # An array of numbers is called a vector or 1D tensors
    # A 1D tensor is said to have exactly one axis
    # Following is the Numpy Vector

    a = np.array([100, 200, 300]) # Rank 1 array
    print(f"This is 1D Tensor : {a} with dimension {a.ndim}")

    # An array of vectors is called matrix or 2D tensors
    # A matrix have 2 axis
    # Following is the Numpy 2D matrix

    x = np.array([[5, 78, 2, 34, 0],
                 [6, 79, 3, 35, 1],
                 [7, 80, 4, 36, 2]])

    print(f"This is 2D Matrix or 2D Tensor :", '\n', x)
    print(f"This is 2D Matrix or 2D Tensor dimension: ", '\n', x.ndim)

    # if you pack such matrices in a new array , you obtain 3D tensors as shown below
    # A matrix have 2 axis
    # Following is the Numpy 2D matrix

    x = np.array([[[5, 78, 2, 34, 0],
                  [6, 79, 3, 35, 1],
                  [7, 80, 4, 36, 2]],
                 [[5, 78, 2, 34, 0],
                  [6, 79, 3, 35, 1],
                  [7, 80, 4, 36, 2]],
                 [[5, 78, 2, 34, 0],
                  [6, 79, 3, 35, 1],
                  [7, 80, 4, 36, 2]]])

    print(f"This is 3D Matrix or 3D Tensor :", '\n', x)
    print(f"This is 3D Matrix or 3D Tensor dimension: ", '\n', x.ndim)

def playing_with_keras():

    from keras.datasets import mnist

    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    print(train_images.ndim)
    print(train_images.shape)
    print(train_images.dtype)


# play_with_numpy()
# add_matrix()
# subtract_matrix()
# multiply_matrix()
# multiply_matrix()
# transpose_matrix()
# dotproduct_matrix()
# slice_matrix()
# int_indexing_slicing_matrix()
# create4x3matrix()
# bool_array_indexing()
# adding_array()
# reshape_array()
# more_on_reshape_array()
# numpy_as_tensors()

playing_with_keras()