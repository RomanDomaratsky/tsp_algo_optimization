from preproccesing import generating_times, sorting, reverse_sorting
from algorithms import spt_algorithm, reverse_spt_algorithm, makespan, average_time, mp_difference
from plots import diff_plot, percentage_diff_plot
from datetime import datetime


if __name__ == '__main__':
    dt = datetime.now()
    mp_spt = []
    mp_reverse_spt = []
    min_works = int(input("Enter start number of works: "))
    max_works = int(input("Enter final number of works: ")) + 1
    step = int(input("Enter step: "))
    machines = int(input("Enter number of machines: "))
    file = open(f'spt_log{dt.strftime ("%I-%M-%S")}.txt', 'w')
    file_r = open(f'reverse_spt_log{dt.strftime("%I-%M-%S")}.txt', 'w')
    for works in range(min_works, max_works, step):
        print("Machines: ", machines, "\nWorks: ", works)
        table = generating_times(works)
        print("Input: ", table)

        spt = spt_algorithm(sorting(table), machines, works)

        for i in range(machines):
            print("Machine number", i+1, spt[i])
            file.write(f'Machine number {i+1} {spt[i]}\n')
        mp_spt.append(makespan(spt))
        file.write(f'Makespan: {makespan(spt)}\n')
        print("Makespan: ", makespan(spt))
        print("Average time: ", average_time(spt))
        file.write(f'Average time: {average_time(spt)}\n')

        reverse_spt = reverse_spt_algorithm(spt, machines, works)

        for i in range(machines):
            print("Machine number", i+1, reverse_spt[i])
            file_r.write(f'Machine number {i + 1} {reverse_spt[i]}\n')
        mp_reverse_spt.append(makespan(reverse_spt))
        file_r.write(f'Makespan: {makespan(reverse_spt)}\n')
        print("Makespan: ", makespan(reverse_spt))
        print("Average time: ", average_time(reverse_spt))
        file_r.write(f'Average time: {average_time(reverse_spt)}\n')

    print("Makespan Difference: ", mp_difference(mp_spt, mp_reverse_spt))
    percentage_diff_plot([x for x in range(min_works, max_works, step)], mp_difference(mp_spt, mp_reverse_spt))
    diff_plot([x for x in range(min_works, max_works, step)], mp_spt, mp_reverse_spt)
