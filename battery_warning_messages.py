def check_warning(value, min_value, max_value, tolerance, lower_warning, upper_warning, parameter_name):
    if min_value <= value < min_value + tolerance:
        print(f"Warning: {parameter_name} is {value}. {lower_warning}")
    elif max_value - tolerance < value <= max_value:
        print(f"Warning: {parameter_name} is {value}. {upper_warning}")

