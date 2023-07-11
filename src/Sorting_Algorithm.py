import random 
import time
class SortingAlgorithm:
    def __init__(self):
        self.runtime_data = ([],[])

    def run(self, algo_name):
        input_sizes = [10,50,100,200,500,1000,2000,5000]

        start_time = time.time()

        algorithms = {
            "Bubble Sort":self.bubbleSort,
            "Merge Sort":self.mergeSort,
        }

        algorithm = algorithms[algo_name]

        for size in input_sizes:
            arr = [random.randint(1, 1000) for _ in range(size)]

            start_time = time.time()
            algorithm(arr)
            runtime = time.time() - start_time

            self.runtime_data[0].append(size)
            self.runtime_data[1].append(runtime)


    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n-1):
            for j in range(n - i - 1):
                if(arr[j] > arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    def mergeSort(self, array):
        if(len(array) > 1):
            r = len(array)//2
            L = array[:r]
            M = array[r:]

            self.mergeSort(L)
            self.mergeSort(M)

            i = j = k = 0

            while(i < len(L) and j < len(M)):
                if(L[i] < M[j]):
                    array[k] = L[i]
                    i+=1
                else:
                    array[k] = M[j]
                    j+=1;   
                k+=1
            
            while(i < len(L)):
                array[k] = L[i]
                i+=1
                k+=1
            while(j < len(M)):
                array[k]=M[j]
                j+=1
                k+=1
            
            


        