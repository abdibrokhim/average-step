from random import *


def main():
    print('\nSession started\n')
    show_result()
    print('\nSession ended successfully\n')


# ------- RANDOM NUMBERS -------#


def generate_random_num():
    i = 1
    random_nums = []
    while i <= 100:
        num = uniform(1, 100)
        random_nums.append(num)
        i += 1
    return random_nums


def dividing_to_two():
    step_list = []
    for i in generate_random_num():
        j = 0
        while i > 1:
            i /= 2
            j += 1
        step_list.append(j)
    return step_list


def average_step():
    average_step = sum(dividing_to_two()) / len(dividing_to_two())
    return average_step


def show_result():
    print('initial random numbers:\n', generate_random_num(), '\n')
    print('initial random numbers length:\n', len(generate_random_num()), '\n')
    print('each random numbers steps until reach -+1:\n', dividing_to_two(), '\n')
    print('each random numbers steps length:\n', len(dividing_to_two()), '\n')
    print('average step (final):\n', average_step(), '\n')


if __name__ == '__main__':
    main()
