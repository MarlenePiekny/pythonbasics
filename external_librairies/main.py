import numpy
from matplotlib import pyplot


one_dimensional_array = numpy.array([1, 2, 3, 4, 5, 6])

two_dimensional_array = numpy.array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
])


def get_element_from_a_two_dimensional_array(array_number, index_of_array):
    return two_dimensional_array[array_number, index_of_array]


def main():

    print(get_element_from_a_two_dimensional_array(0, 3))

    pyplot.plot(two_dimensional_array[0], two_dimensional_array[1])
    pyplot.show()


if __name__ == '__main__':
    main()
