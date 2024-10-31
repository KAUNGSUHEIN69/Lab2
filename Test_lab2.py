import Lab2

def test_find_min_max():
    input_data = [4,88,12,-1,99]
    result= Lab2.calc_min_max(input_data)
    assert result == [-1,99],f"Expect [-1,99], but got {result}"

def test_cal_average():
    input_data = [10,20,30,40,50]
    result= Lab2.calc_average(input_data)
    assert result== 30, f"Expect 30 but got {result}"

def test_cal_median_temperature_odd():
    input_data = [50,10,20,30,40]
    result = Lab2.calc_median_temperature(input_data)
    assert result== 30,f"expect 30 but got {result}"

def test_cal_median_temperature_even():
    input_data = [50,20,30,10]
    result= Lab2.calc_median_temperature(input_data)
    assert result== 25,f"expect 25 but got {result}"