import random
import matplotlib.pyplot as plt
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Sorting_Algorithm import SortingAlgorithm

class AlgorithmRuntimeVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Algorithm Runtime Visualizer")
        self.layout = QVBoxLayout()
        
        # Create a label for algorithm selection
        self.algorithm_label = QLabel("Select an algorithm:")
        self.layout.addWidget(self.algorithm_label)
        
        # Create a dropdown menu for algorithm selection
        self.algorithm_combobox = QComboBox()
        self.algorithm_combobox.addItem("Bubble Sort")
        # Add more algorithms to the dropdown menu if desired
        
        self.layout.addWidget(self.algorithm_combobox)
        
        # Create a button to run the selected algorithm
        self.run_button = QPushButton("Run Algorithm")
        self.run_button.clicked.connect(self.run_algorithm)
        self.layout.addWidget(self.run_button)
        
        # Create a matplotlib figure and canvas for the plot
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        
        self.setLayout(self.layout)
        
    def run_algorithm(self):
        algorithm = self.algorithm_combobox.currentText()
        
        # Define the input sizes you want to test
        input_sizes = [10, 50, 100, 200, 500, 1000]

        # Initialize lists to store input sizes and corresponding runtimes
        x_values = []
        y_values = []

        # Measure the runtime for each input size
        for size in input_sizes:
            # Generate a random input data of the given size
            input_data = [random.randint(1, 1000) for _ in range(size)]
            
            # Measure the start time
            start_time = time.time()
            
            # Run the selected algorithm with the input data
            if algorithm == "Bubble Sort":
                self.bubble_sort(input_data)
            # Add more algorithms and corresponding function calls here
            
            # Calculate the runtime
            runtime = time.time() - start_time
            
            # Store the input size and runtime
            x_values.append(size)
            y_values.append(runtime)
        
        # Clear the previous plot
        self.figure.clear()
        
        # Create a subplot and plot the data
        ax = self.figure.add_subplot(111)
        ax.plot(x_values, y_values, 'o-')
        ax.set_xlabel('Input Size')
        ax.set_ylabel('Runtime (seconds)')
        ax.set_title('Algorithm Runtime Analysis')
        
        # Redraw the canvas
        self.canvas.draw()
    

# Create a QApplication instance
app = QApplication([])

# Create the main window
window = AlgorithmRuntimeVisualizer()
window.show()

# Run the application event loop
app.exec_()
