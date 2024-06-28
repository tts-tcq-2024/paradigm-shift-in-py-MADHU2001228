def is_in_range(value, lower, upper):
    return lower <= value <= upper

def battery_is_ok(temperature, soc, charge_rate):
    if not is_in_range(temperature, 0, 45) or not is_in_range(soc, 20, 80):
        print('Temperature or State of Charge is out of range!')
        return False
    elif charge_rate > 0.8:
        print('Charge rate is out of range!')
        return False
    return True

if __name__ == '__main__':
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False
