
def is_temperature_valid(temperature):
    return 0 <= temperature <= 45

def is_soc_valid(soc):
    return 20 <= soc <= 80

def battery_is_ok(temperature, soc, charge_rate):
    if not is_temperature_valid(temperature) or not is_soc_valid(soc):
        print('Temperature or State of Charge is out of range!')
        return False
    elif charge_rate > 0.8:
        print('Charge rate is out of range!')
        return False
    return True

if __name__ == '__main__':
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False

