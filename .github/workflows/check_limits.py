def battery_is_ok(temperature, soc, charge_rate):
    temperature_ok = 0 <= temperature <= 45
    soc_ok = 20 <= soc <= 80
    charge_rate_ok = charge_rate <= 0.8
    
    if not temperature_ok:
        print('Temperature is out of range!')
    elif not soc_ok:
        print('State of Charge is out of range!')
    elif not charge_rate_ok:
        print('Charge rate is out of range!')
    else:
        return True
    
    return False

if __name__ == '__main__':
    # Test cases
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False

