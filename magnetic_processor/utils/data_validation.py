def validate_data(data):
    """
    Validate that input data is in acceptable format and range.
    :param data: The data to validate
    :return: bool: True if valid, False otherwise
    """
    # Example validation checks
    if not data:
        return False
    if not isinstance(data, (list, tuple)):
        return False
    for value in data:
        if not isinstance(value, (int, float)):
            return False
    return True


def check_grid_spacing(x_coordinates, y_coordinates):
    """
    Check if the grid spacing between the coordinates is consistent.
    :param x_coordinates: List of x coordinates
    :param y_coordinates: List of y coordinates
    :return: bool: True if spacing is consistent, False otherwise
    """
    if len(x_coordinates) < 2 or len(y_coordinates) < 2:
        return False
    x_spacing = abs(x_coordinates[1] - x_coordinates[0])
    y_spacing = abs(y_coordinates[1] - y_coordinates[0])
    for i in range(1, len(x_coordinates)):
        if abs(x_coordinates[i] - x_coordinates[i - 1]) != x_spacing:
            return False
    for i in range(1, len(y_coordinates)):
        if abs(y_coordinates[i] - y_coordinates[i - 1]) != y_spacing:
            return False
    return True
