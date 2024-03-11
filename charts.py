import matplotlib.pyplot as plt #plt es el alias

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels) #En ese orden lo recibe la libreria
    ax.axis('equal')
    plt.show()

