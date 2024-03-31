import numpy as np
import matplotlib.pyplot as plt

with open("examp10.txt", 'r') as f:
    robot_x, robot_y, robot_angle = [], [], []
    mas = []
    for i in range(100):
        stroka = f.readline().replace(',', '').replace(';', '').split()
        x = float(stroka[0])
        y = float(stroka[1])
        z = float(stroka[2])
        robot_x.append(x)
        robot_y.append(y)
        robot_angle.append(z)
        mas.append(stroka)
lidar_measurements = np.array([row[3:] for row in mas], dtype=float)
plt.figure(figsize=(15,10))
for i in range(100):
    x = robot_x[i]
    y = robot_y[i]
    angle = robot_angle[i]
    # Преобразование замеров лидара в координаты объектов с использованием numpy
    filtered_coordinates = []
    for j in range(681):
        lidar_distance = float(lidar_measurements[i][j])
        lidar_angle = angle + 3 * np.pi / 4 - ((j * np.pi * (3 / 2)) / 681)
        object_x = x + lidar_distance * np.cos(lidar_angle)
        object_y = y + lidar_distance * np.sin(lidar_angle)
        if 1 <= lidar_distance < 4:
            filtered_coordinates.append((object_x, object_y))
    object_coordinates = np.array(filtered_coordinates)
    # Отображение объектов, обнаруженных лидаром
    plt.scatter(object_coordinates[:, 0], object_coordinates[:, 1], color='red')

plt.plot(robot_x, robot_y, color='blue', label='Маршрут робота' if i == 0 else None)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Карта с маршрутом и объектами, обнаруженными лидаром')
plt.legend()
plt.grid(True)
plt.show()