import time
import random
class GraphAlgorithms:
    def __init__(self):
        self.runtime_data = ([],[])


    def run(self, algo_name):
        input_sizes = [10,50,100,200,500,1000,2000]

        algorithms = {
            "Depth First Search":self.dfs,
            "Dijkstra's Algorithm":self.dijkstra
        }

        algorithm = algorithms[algo_name]

        for size in input_sizes:
            arr = [random.randint(1, 1000) for _ in range(size)]

            start_time = time.time()
            algorithm(arr)
            runtime = time.time() - start_time

            self.runtime_data[0].append(size)
            self.runtime_data[1].append(runtime)
     
