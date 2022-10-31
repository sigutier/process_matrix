from functools import reduce


def process_matrix(matrix):
    if matrix == []:
        return []
    elif _is_numerical_matrix(matrix):
        return _process_matrix(matrix)
    else:
        raise ValueError("Only works on numerical matrices")


def _is_numerical_matrix(matrix):
    """
    Check that you work with numerical matrices with columns of the same size
    """
    if type(matrix) != list:
        return False
    size = 0
    for i, column in enumerate(matrix):
        if type(column) != list:
            return False
        if i == 0:
            size = len(matrix[i])
        elif size != len(matrix[i]):
            return False
        for value in column:
            if type(value) != int:
                return False
    return True


def _process_matrix(matrix):
    """
    Receives a numeric matrix and returns a new matrix where each element 
    will be the average between the old value and its neighbors
    """
    new_matrix = []
    for i, column in enumerate(matrix):
        new_column = []
        new_matrix.append(new_column)
        for j in range(len(column)):
            new_value = _process_element(i, j, matrix)
            new_column.append(new_value)
    return new_matrix


def _process_element(i, j, matrix):
    """
    Receives an element of a matrix, calculates its average 
    with its neighbors, and returns that average
    """
    coordinates = _get_neighbour_coordinates(i, j, matrix)
    values = _get_neighbour_values(coordinates, matrix)
    average = _calculate_average(values)
    return average


def _get_neighbour_coordinates(i, j, matrix):
    """
    Returns a list with the [column,row] coordinates of 
    its neighbors and also those of the element itself
    """
    valid_coordinates = []
    if i >= 0 and i < len(matrix) and j - 1 >= 0 and j - 1 < len(matrix[i]):
        valid_coordinates.append([i, j - 1])
    if i >= 0 and i < len(matrix) and j + 1 >= 0 and j + 1 < len(matrix[i]):
        valid_coordinates.append([i, j + 1])
    if i - 1 >= 0 and i - 1 < len(matrix) and j >= 0 and j < len(matrix[i]):
        valid_coordinates.append([i - 1, j])
    if i + 1 >= 0 and i + 1 < len(matrix) and j >= 0 and j < len(matrix[i]):
        valid_coordinates.append([i + 1, j])

    valid_coordinates.append([i, j])
    return valid_coordinates


def _get_neighbour_values(valid_coordinates, matrix):
    """
    Returns a list of valid coordinate values
    """
    values = []
    for index in valid_coordinates:
        i = index[0]
        j = index[1]
        values.append(matrix[i][j])
    return values


def _calculate_average(numbers):
    """
    Receive a list of numbers and return their average
    """
    return reduce(lambda a, b: a + b, numbers) / len(numbers)
