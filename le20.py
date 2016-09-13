import numpy as np
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv',  comments='#')

def xa_to_diameter(xa):
    """
    convert array of cross section area to diameter.
    """

    # compute the diameter
    diameter = np.sqrt(xa * 4/np.pi)
    return diameter
A = np.array([[6.7, 1.3, 3.2, 1.1],
[0.1, 5.5, 2.1, 4.4],
[1.0, 0.2, 0.5, 1.1],
[1.2, 0.4, 0.5, 1.3]])

b= np.array([1.1, 2.2, 3.3, 4.4])

# print row 1 of A
# print columns 1 and 3 of A 
