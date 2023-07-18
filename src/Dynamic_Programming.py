import random
import time

class DynamicProgramming:
    def __init__(self):
        self.runtime_data = ([],[])
    
    def run(self, algo_name):
        input_sizes = [10,50,100,200,500,1000,2000,4000]

        start_time = time.time()

        algorithms = {
            "Fibonacci Sequence":self.fib,
        }

        algorithm = algorithms[algo_name]

        for size in input_sizes:
            arr = [random.randint(1, 1000) for _ in range(size)]

            start_time = time.time()
            algorithm(arr)
            runtime = time.time() - start_time

            self.runtime_data[0].append(size)
            self.runtime_data[1].append(runtime)
    

    def fib(self, arr):
        fib = [0] * (len(arr)+1)
        fib[0] = 0
        fib[1] = 1

        for i in range(2, len(arr)+1):
            fib[i] = fib[i-1] + fib[i-2]
        
        


