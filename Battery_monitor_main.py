from battery_parameter_checks import is_BatteryTemperature_Ok, is_BatterySoc_Ok, is_BatteryChargeRate_Ok

def battery_Is_Ok(temperature, soc, chargeRate):
    return is_BatteryTemperature_Ok(temperature) and is_BatterySoc_Ok(soc) and is_BatteryChargeRate_Ok(chargeRate)

if __name__ == '__main__':
    import battery_monitor_tests
    battery_monitor_tests.run_tests()



