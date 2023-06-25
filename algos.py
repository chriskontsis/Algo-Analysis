import matplotlib.pyplot as plt
import time
import random

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j];

x_values = []
y_values = []
input_sizes = [10,50,100,200,500,1000,1500,2000]

for size in input_sizes:

    input_data = [random.randint(1, 1000) for _ in range(size)]
    start_time = time.time()
    bubbleSort(input_data)
    run_time = time.time() - start_time

    x_values.append(size)
    y_values.append(run_time)


plt.plot(x_values, y_values, 'o-')
plt.xlabel('Input Size')
plt.ylabel('Run Time')
plt.show()