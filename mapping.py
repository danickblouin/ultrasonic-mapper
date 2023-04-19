import math
import matplotlib.pyplot as plt
import serial

ser = serial.Serial('/dev/tty.usbmodem11301', 9600) # Replace with the serial port of your Arduino and the baud rate of your program

max_angle = 90
increment_angle = 5

plt.ion()
fig, ax = plt.subplots()
point, = ax.plot([], [], 'o')
trail, = ax.plot([], [], 'r-')

x_values = []
y_values = []
def main():
    current_angle = 0
    xs = []
    ys = []
    ser.readline()
    ser.readline()
    while True:
        data = ser.readline().decode('utf-8').strip()
        try:
            if data:
                print(data)
                distance = int(data)
                x = distance * math.cos(math.radians(current_angle))
                y = distance * math.sin(math.radians(current_angle))

                x_values.append(x) # Add the x coordinate to the list of x values
                y_values.append(y) # Add the y coordinate to the list of y values
                # point.set_data(x, y) # Set the x and y coordinates of the point
                trail.set_data(x_values, y_values) # Set the x and y coordinates of the trail

                ax.relim()
                ax.autoscale_view()
                fig.canvas.draw()
                fig.canvas.flush_events()
                current_angle += increment_angle
        except ValueError:
            pass

    # with open('data/data.txt') as f:
    #     for line in f:
    #         distance = int(line.strip())
    #         x = distance * math.cos(math.radians(current_angle))
    #         y = distance * math.sin(math.radians(current_angle))
    #         xs.append(x)
    #         ys.append(y)
    #         current_angle += increment_angle
    #         # plt.plot(x, y, 'ro')
    #         # print("x: {}, y: {}".format(x, y))
    plt.plot(xs, ys, 'ro')
    plt.show()

if __name__ == "__main__":
    main()
