import struct
import math

# высота и ширина холста
height = 1500
width = 1500
# создание холста
my_list = []
for i in range(height):
    my_list.append([])
    for j in range(width):
        my_list[i].append(0)
# график функции
for t in range(int(20 * math.pi*750)):
    for i in range(-2, 3):  # высота линии
        for j in range(-2, 3):  # ширина линии
            my_list[int(height / 2 + 4.4 * (math.cos(t) + (math.cos(1.1 * t)) / 1.1) * 70) + i][
                int(width / 2 + 4.4 * (math.sin(t) - (math.sin(1.1 * t)) / 1.1) * 70) + j] = 1

with open("graph.bmp", 'wb') as file:
    # Структура BITMAPFILEHEADER
    file.write(struct.pack("<hihhi", 19778, height*width+62, 0, 0, 62))  # (тип файла, размер в байтах,
    # резервное поле, резервное поле, байтовое смещение до начала массива пикселов)
    # Структура BITMAPINFOHEADER
    file.write(struct.pack("<iiihhiiiiii", 40, width, height, 1, 8, 0, 0, 0, 0, 2, 0))  # (размер структуры,
    # ширина растра, высота растра, количество плоскостей, количество битов на пиксел, алгоритм сжатия, размер
    # массива пикселов в байтах, горизонтальное разрешение устройства вывода, вертикальное разрешение, количество
    # элементов в цветовой таблице, количество элементов, используемых для растра)
    # цвета файла
    file.write(struct.pack("<BBBBBBBB", *(0, 0, 255, 0), *(255, 255, 255, 0)))
    for i in range(height):
        for j in range(width):
            if my_list[i][j] == 1:
                file.write(struct.pack("<B", 0))
            else:
                file.write(struct.pack("<B", 1))
