import matplotlib.pyplot as plt


def diff_plot(frame, mp_spt, mp_reverse_spt):
    plt.plot(frame, mp_spt, marker='o', label="SPT")
    plt.plot(frame, mp_reverse_spt, marker='o', label="reverse SPT")
    plt.xlabel("Number of works")
    plt.ylabel("Makespan difference")
    plt.legend(loc="upper left")
    plt.show()


def percentage_diff_plot(frame, mp_diff):
    plt.plot(frame, mp_diff, marker='o')
    plt.xlabel("Number of works")
    plt.ylabel("Makespan difference %")
    plt.show()