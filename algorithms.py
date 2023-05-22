from timing_decorator import timing
from preproccesing import reverse_sorting


@timing
def reverse_spt_algorithm(data: list, m, n):
    """Reverse SPT-algorithm"""
    temp = []
    for j in range(1, int(n / m), 2):  # extracting data from odd columns
        result = []
        k = 0
        for i in range(0, m):
            result.append(data[i][j])
        temp.append(result)
    for a in range(len(temp)):
        temp[a] = reverse_sorting(temp[a])  # reversing extracted data
    for i in range(1, int(n / m), 2):  # replaceing data in list with reversed data
        k = 0
        for j in range(m):
            data[j][i] = temp[0][k]
            k += 1
    return data


@timing
def spt_algorithm(data: list, m, n):
    """SPT-algorithm"""
    optimal_table = []
    for i in range(0, m):
        result = [0 for x in range(n // m)]
        k = 0
        for j in range(i, n, m):
            result[k] = data[j]
            k += 1
        optimal_table.append(result)
    return optimal_table


def average_time(data: list):
    """Counter of average time of works to be done"""
    mp = 0
    counter = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            mp += (len(data[i]) - j) * data[i][j][1]
            counter += 1
    return mp / counter


def makespan(data: list):
    """Counter of makespan"""
    results = []
    for i in range(len(data)):
        mp = 0
        for j in range(len(data[i])):
            mp += data[i][j][1]
        results.append(mp)
    return max(results)


def mp_difference(spt_list, reverse_spt_list):
    mp_diff = []
    for i in range(len(spt_list)):
        diff = round((((spt_list[i] - reverse_spt_list[i]) / spt_list[i]) * 100), 2)
        mp_diff.append(diff)
    return mp_diff
