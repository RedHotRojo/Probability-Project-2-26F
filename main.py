import math
import random

def generate_calibration_time():
    r = random.random()
    i_cdf = math.sqrt(r) * 2 + 4
    return i_cdf

def simulate_module():
    t = 0
    n = 1 

    while True:
        t += 2  # setup time
        x = generate_calibration_time()
        r = random.random()

        if r < 0.7:
            return t, True  # module passes and process ends
        else:
            if n == 3:
                return t, False  # module fails and process ends
            else:
                r = random.random()
                if r < 0.6:
                    s = random.uniform(1, 2)  # software reset: repair time s between 1 and 2
                else:
                    s = random.uniform(3, 5)  # hardware reset: repair time s between 3 and 5
                t += s
                n += 1

times = []
approvals = []
for i in range(1000):
    t, result = simulate_module()
    times += [t]
    approvals.append(result)

print(times, file=open("times.txt", "w"))
print(approvals, file=open("approvals.txt", "w"))

with open("results.csv", "w") as f:
    f.write("time,approval\n")
    for t, result in zip(times, approvals):
        f.write(f"{t},{result}\n")
