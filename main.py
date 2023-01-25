from tkinter import *
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
window = Tk()
window.title("Elective Projects")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width = 1500
height = 700
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
window.resizable(0, 0)


def temperature():

    matplotlib.use("TkAgg")
    stored_prices = [1,2,3,45,6,6]
    prices_time = ['00:00', '00:05', '00:10', '00:15', '00:20', '00:00']
    x = range(len(prices_time))
    figure = Figure(figsize=(3, 3), dpi=120)
    fig, ax = plt.subplots()
    plot = figure.add_subplot(1, 1, 1)
    plot.plot(0.5, 0.3, color="blue", linestyle="")
    plt.title("X")
    plt.tick_params(axis='y', which='both', labelleft=False, labelright=True)
    plt.plot(x, stored_prices)
    plt.grid()
    plt.subplots_adjust(left=0.03, right=0.86)
    fig.autofmt_xdate()
    ax.set_xticks(x)
    ax.set_xticklabels(prices_time)

    canvas = FigureCanvasTkAgg(figure, temperatureFrame)
    canvas.get_tk_widget().grid(row=0, column=0)

# def temperature():
#     matplotlib.use("TkAgg")
#
#     # Create a figure of specific size
#     figure = Figure(figsize=(3, 3), dpi=120)
#     figure.suptitle("TEMPERATURE")
#     # Define the points for plotting the figure
#     plot = figure.add_subplot(1, 1, 1)
#     plot.plot(0.5, 0.3, color="blue", linestyle="")
#
#     # Define Data points for x and y axis
#     x = [0.2, 0.5, 0.8, 1.0]
#     y = [1.0, 1.2, 1.3, 1.4]
#     plot.plot(x, y, color="red", )
#
#     # Add a canvas widget to associate the figure with canvas
#     canvas = FigureCanvasTkAgg(figure, temperatureFrame)
#     canvas.get_tk_widget().grid(row=0, column=0)

def humidity():
    matplotlib.use("TkAgg")

    # Create a figure of specific size
    figure = Figure(figsize=(3, 3), dpi=120)
    figure.suptitle("HUMIDITY")

    # Define the points for plotting the figure
    plot = figure.add_subplot(1, 1, 1)
    plot.plot(0.5, 0.3, color="blue")

    # Define Data points for x and y axis
    x = [0.2, 0.1, 0.5, 10.0]
    y = [1.0, 1.2, 1.3, 1.4]
    plot.plot(x, y, color="red")

    # Add a canvas widget to associate the figure with canvas
    canvas = FigureCanvasTkAgg(figure, humidityFrame)
    canvas.get_tk_widget().grid(row=2, column=2)


def barometer():
    matplotlib.use("TkAgg")

    # Create a figure of specific size
    figure = Figure(figsize=(3, 3), dpi=120)
    figure.suptitle("BAROMETER")
    # Define the points for plotting the figure
    plot = figure.add_subplot(1, 1, 1)
    plot.plot(0.5, 0.3, color="blue")

    # Define Data points for x and y axis
    x = [5, 3, 1]
    y = [2, 2, 1]
    plot.plot(x, y, color="red")

    # Add a canvas widget to associate the figure with canvas
    canvas = FigureCanvasTkAgg(figure, barometerFrame)
    canvas.get_tk_widget().grid(row=2, column=2)


#===============================Frame==========================================
title = Frame(window, bd=10, bg='green', relief=RAISED, width=100, height=100)
title.pack(side=TOP)
temperatureFrame = Frame(window, bd=1, relief=RAISED, width=400, height=400)
temperatureFrame.pack(side=LEFT, pady=10, padx=90)
humidityFrame = Frame(window, bd=1, relief = RAISED, width=400, height=400)
humidityFrame.pack(side=LEFT, pady=10, padx=50)
barometerFrame = Frame(window, bd=1, relief = RAISED, width=400, height=400)
barometerFrame.pack(side=LEFT, pady=10, padx=50)
temperatureTitle = Frame(temperatureFrame, relief=SUNKEN)






#================================LABEL=========================================
titleLabel = Label(title, text="ELECTIVE PROJECT", font=("Arial", 20), fg='blue', width=100)
titleLabel.pack()


temperature()
humidity()
barometer()



window.mainloop()
