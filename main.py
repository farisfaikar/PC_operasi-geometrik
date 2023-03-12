import cv2
import numpy as np


def rotate_image():
    img = cv2.imread('image.jpg')
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h))
    cv2.imshow("Rotated Image", rotated)
    cv2.waitKey(0)


def resize_image():
    img = cv2.imread('image.jpg')
    resized = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow("Resized Image", resized)
    cv2.waitKey(0)


def crop_image():
    img = cv2.imread('image.jpg')
    cropped = img[150:150+300, 100:100+200]
    cv2.imshow("Cropped Image", cropped)
    cv2.waitKey(0)


def flip_image():
    img = cv2.imread('image.jpg')
    flipped = cv2.flip(img, 1)
    cv2.imshow("Flipped Image", flipped)
    cv2.waitKey(0)


def translate_image():
    img = cv2.imread('image.jpg')
    (h, w) = img.shape[:2]
    M = np.float32([[1, 0, 50], [0, 1, 25]])
    translated = cv2.warpAffine(img, M, (w, h))
    cv2.imshow("Translated Image", translated)
    cv2.waitKey(0)


def main():
    rotate_image()
    # resize_image()
    # crop_image()
    # flip_image()
    # translate_image()


if __name__ == '__main__':
    main()
