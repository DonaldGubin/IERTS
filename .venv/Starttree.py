'''
Толчев, Еличев, Кайлачаков КРБО-01-21
'''

import cv2
import numpy as np
import random


def Fast_tree(img, x, y, threshold):
    center = img[y, x]
    # порог интенсивности
    lower_threshold = center - threshold
    upper_threshold = center + threshold

    positions = [(0, -3), (1, -3), (2, -2), (3, -1), (3, 0), (3, 1), (2, 2), (1, 3), (0, 3), (-1, 3), (-2, 2), (-3, 1),
                 (-3, 0), (-3, -1), (-2, -2), (-1, -3)]
    # счетчик яркости
    brighter_count = 0
    darker_count = 0

    for dx, dy in positions:
        if img[y + dy, x + dx] >= upper_threshold:
            brighter_count += 1
            if brighter_count >= 12:
                return True
        elif img[y + dy, x + dx] <= lower_threshold:
            darker_count += 1
            if darker_count >= 12:
                return True

    return False

def find_keypoints(img, threshold):
    keypoints = []
    height, width = img.shape
    for y in range(3, height - 3):
        for x in range(3, width - 3):
            if Fast_tree(img, x, y, threshold):
                keypoints.append((x, y))

    return keypoints

image_color = cv2.imread('penquinchiks.jpeg')
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
keypoints = find_keypoints(image_gray, 20)

for point in keypoints:
    cv2.circle(image_color, point, 3, (0, 255, 0), 1)
cv2.imshow('FAST', image_color)
cv2.waitKey(0)
cv2.destroyAllWindows()






# def detect_keypoints(image):
#     # Преобразование изображения в оттенки серого
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#     # Инициализация объекта ORB
#     orb = cv2.ORB_create()
#
#     # Поиск ключевых точек
#     keypoints, descriptors = orb.detectAndCompute(gray, None)
#
#     return keypoints
#
#
# # Загрузка изображения
# image = cv2.imread('penquinchiks.jpeg')
#
# # Поиск ключевых точек на изображении
# keypoints = detect_keypoints(image)
#
# # Отрисовка ключевых точек на изображении
# image_with_keypoints = cv2.drawKeypoints(image, keypoints, None)
#
# # Отображение изображения с ключевыми точками
# cv2.imshow('Image with Keypoints', image_with_keypoints)
# cv2.waitKey(0)
# cv2.destroyAllWindows()











# image = cv2.imread('penquinchiks.jpeg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Инициализация детектора FAST
# fast = cv2.FastFeatureDetector_create(threshold=30)  # Установите желаемый порог здесь
#
# # Обнаружение особых точек
# keypoints = fast.detect(gray, None)
#
# # Рисование особых точек на изображении
# img_with_keypoints = cv2.drawKeypoints(image, keypoints, None, color=(255, 0, 0))
#
# # Отображение изображения с особыми точками
# cv2.imshow('FAST keypoints', img_with_keypoints)
# cv2.waitKey(0)
# cv2.destroyAllWindows()