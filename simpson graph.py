import matplotlib.pyplot as plt

def readdata(filename):
    X = []
    Y = []
    with open(filename, "r") as file:
        for line in file:
                x, y = map(float, line.split())
                X.append(x)
                Y.append(y)
    return X, Y

def plot_graph(X, Y, title):
    plt.figure(figsize=(10, 6))
    plt.plot(X, Y, linestyle='-', color='b')
    plt.title(title)
    plt.grid(True)
    plt.xlabel("N")
    plt.ylabel("eps")
    plt.show()

X, Y = readdata("inNopt.txt")

plot_graph(X, Y, "Залежність похибки від кількості поділів проміжку")