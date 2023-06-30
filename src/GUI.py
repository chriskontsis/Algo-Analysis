import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Sorting_Algorithm import SortingAlgorithm

class AlgorithmRuntimeVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Algorithm Runtime Visualizer")
        self.layout = QVBoxLayout()

        # Create a label for algorithm type selection
        self.algorithm_type_label = QLabel("Select an algorithm type:")
        self.layout.addWidget(self.algorithm_type_label)

        # Create a dropdown menu for algorithm type selection
        self.algorithm_type_combobox = QComboBox()
        self.algorithm_type_combobox.addItem("Sorting")
        self.algorithm_type_combobox.addItem("Dynamic Programming")
        self.algorithm_type_combobox.addItem("Graph Algorithms")

        #allows for algorithms to be changed based on what type of algorithm is selected
        self.algorithm_type_combobox.currentIndexChanged.connect(self.update_algorithm_combobox)
        self.layout.addWidget(self.algorithm_type_combobox)

        # Create a label for algorithm selection
        self.algorithm_label = QLabel("Select an algorithm:")
        self.layout.addWidget(self.algorithm_label)

        # Create a dropdown menu for algorithm selection
        self.algorithm_combobox = QComboBox()
        self.update_algorithm_combobox()
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
    
    def update_algorithm_combobox(self):

        algorithm_type = self.algorithm_type_combobox.currentText()
        self.algorithm_combobox.clear()

        if algorithm_type == "Sorting":
            self.algorithm_combobox.addItem("Bubble Sort")
            self.algorithm_combobox.addItem("Selection Sort")
       
        elif algorithm_type == "Dynamic Programming":
            self.algorithm_combobox.addItem("Fibonacci Sequence")
            self.algorithm_combobox.addItem("Longest Common Subsequence")

        elif algorithm_type == "Graph Algorithms":
            self.algorithm_combobox.addItem("Dijkstra's Algorithm")
            self.algorithm_combobox.addItem("Depth-First Search")
           
    def run_algorithm(self):
        algorithm_type = self.algorithm_type_combobox.currentText()
        algorithm_name = self.algorithm_combobox.currentText()

        # Retrieve the appropriate algorithm class based on the selected type
        if algorithm_type == "Sorting":
            algorithm_class = SortingAlgorithm

        # Create an instance of the algorithm class and run the algorithm
        algorithm = algorithm_class()
        algorithm.run(algorithm_name)

        # Retrieve the runtime data from the algorithm object
        x_values, y_values = algorithm.runtime_data
        print(x_values, y_values)
        # Clear the previous plot
        self.figure.clear()

        # Create a subplot and plot the data
        ax = self.figure.add_subplot(111)
        ax.plot(x_values, y_values, 'o-')
        ax.set_xlabel('Input Size')
        ax.set_ylabel('Runtime (seconds)')
        ax.set_title('Algorithm Runtime Analysis')
        self.canvas.draw()

# Create a QApplication instance
app = QApplication([])

# Create the main window
window = AlgorithmRuntimeVisualizer()
window.show()

# Run the application event loop
app.exec_()
