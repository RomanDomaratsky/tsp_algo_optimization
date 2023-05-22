import random


def generating_times(works: int):
    """Function for generating data"""
    times = [[random.randint(1, 100)] * 2 for x in range(works)]
    for i in range(works):
        times[i][0] = i + 1
    return times


def sorting(data: list):
    """Function for sorting data from min to max"""
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][1] > data[j][1]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp

    return data


def reverse_sorting(data: list):
    """Function for sorting data from min to max"""
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][1] < data[j][1]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    return data