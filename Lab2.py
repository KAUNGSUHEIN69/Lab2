def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    user_input = input("Enter numbers: ")
    num_list = [float(i) for i in user_input.split(",")]
    return num_list


def calc_average(num_list):
    return sum(num_list) / len(num_list)


def calc_min_max(num_list):
    return [min(num_list), max(num_list)]


def sort_temperature(num_list):
    return sorted(num_list)


def calc_median_temperature(num_list):
    sorted_temps = sort_temperature(num_list)
    n = len(sorted_temps)
    
    if n % 2 == 1:  
        return sorted_temps[n // 2]
    else: 
        return (sorted_temps[n // 2 - 1] + sorted_temps[n // 2]) / 2


def main():
    display_main_menu()
    
    temperatures = get_user_input()

    average_temp = calc_average(temperatures)
    print("Average Temperature:", average_temp)

    min_max_temp = calc_min_max(temperatures)
    print("Min Temperature:", min_max_temp[0])
    print("Max Temperature:", min_max_temp[1])

    sorted_temperatures = sort_temperature(temperatures)
    print("Sorted Temperatures:", sorted_temperatures)
    median_temp = calc_median_temperature(temperatures)
    print("Median Temperature:", median_temp)
if __name__ == "__main__":
    main()
