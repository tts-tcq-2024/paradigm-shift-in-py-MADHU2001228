from battery_monitor_main import battery_Is_Ok

def run_tests():
    assert battery_Is_Ok(25, 70, 0.7) == True  # all parameters are within the normal range
    assert battery_Is_Ok(50, 70, 0.7) == False  # Temperature out of range (high)
    assert battery_Is_Ok(-1, 70, 0.7) == False  # Temperature out of range (low)
    assert battery_Is_Ok(25, 85, 0.7) == False  # SoC out of range (high)
    assert battery_Is_Ok(25, 10, 0.7) == False  # SoC out of range (low)
    assert battery_Is_Ok(25, 70, 0.9) == False  # Charge Rate out of range (high)
    assert battery_Is_Ok(50, 85, 0.7) == False  # Temperature and SoC out of range (high)
    assert battery_Is_Ok(-1, 10, 0.7) == False  # Temperature and SoC out of range (low)
    assert battery_Is_Ok(25, 85, 0.9) == False  # SoC and Charge Rate out of range (high)
    assert battery_Is_Ok(50, 70, 0.9) == False  # Temperature and Charge Rate out of range (high)
    assert battery_Is_Ok(-1, 70, 0.9) == False  # Temperature out of range (too low) and Charge Rate out of range (high)
    assert battery_Is_Ok(50, 85, 0.9) == False  # All parameters out of range (high)
    print("All test cases passed!")
