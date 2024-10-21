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


def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")