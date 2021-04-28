import numpy as np

def add_arrays(a, b):
    return a + b


if __name__ == "__main__":
    a = np.array([1,2,3])
    b = np.array([4,5,6])
    c = add_arrays(a, b)
    print(c)