import cv2
import numpy as np


def negative(img):
    max_intensity = 255
    img = max_intensity - img
    negative_img = np.array(img, dtype=np.uint8)
    return negative_img


def log(img):
    c = 1
    log_image = c * (np.log2(img + 1))
    log_image = log_image * (255 / np.log2(255))
    log_image = np.array(log_image, dtype=np.uint8)
    return log_image


def inverse_log(img):
    c = 50
    log_inverse = np.exp(img / c) - 1
    log_inverse = np.array(log_inverse, dtype=np.uint8)
    return log_inverse


def nth_power(img):
    power_value = float(input("Enter Value of nth Power: "))

    c = 1
    power_img = c * np.power(img, power_value)
    power_img = power_img * (255 / np.power(255, power_value))
    power_img = np.array(power_img, dtype=np.uint8)
    return power_img


def nth_root(img):
    value = float(input("Enter Value of nth Root: "))
    root_value = 1 / value

    c = 1
    root_img = c * np.power(img, root_value)
    root_img = root_img * (255 / np.power(255, root_value))
    root_img = np.array(root_img, dtype=np.uint8)
    return root_img


def gray_slice_with_bg(img):
    row, column = img.shape
    img2 = np.zeros((row, column), dtype=np.uint8)

    lower_pixel = int(input("Enter Lowest Pixel: "))
    upper_pixel = int(input("Enter Highest Pixel: "))

    for i in range(row):
        for j in range(column):
            if lower_pixel < img[i, j] < upper_pixel:
                img2[i, j] = 255
            else:
                img2[i, j] = img[i, j]
    return img2


def gray_slice_without_bg(img):
    row, column = img.shape
    img1 = np.zeros((row, column), dtype=np.uint8)

    lower_pixel = int(input("Enter Lowest Pixel: "))
    upper_pixel = int(input("Enter Highest Pixel: "))

    for i in range(row):
        for j in range(column):
            if lower_pixel < img[i, j] < upper_pixel:
                img1[i, j] = 255
            else:
                img1[i, j] = 0
    return img1


def bit_plane_slice(img):
    wid = 8

    lst = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            lst.append(np.binary_repr(img[i][j], width=wid))  # width = no. of bits

    bit_img = [k for k in range(wid)]

    for k in range(wid):
        bit_img[k] = (np.array([int(i[k]) for i in lst], dtype=np.uint8) * 2 ** (wid - k - 1)).reshape(img.shape[0],
                                                                                                       img.shape[1])
    l = int(wid / 4)
    final_bit = [i for i in range(l)]

    for i in range(l):
        final_bit[i] = cv2.hconcat([bit_img[i * 4 + 0], bit_img[i * 4 + 1], bit_img[i * 4 + 2], bit_img[i * 4 + 3]])

    final = cv2.vconcat([final_bit[0], final_bit[1]])

    return final


def print_image(convert_image, name):
    cv2.imshow(name, convert_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


while True:
    print("Please Choose From the List: ")
    print("-------------------------------------")
    print("1. Negative Transformation.")
    print("2. Log Transformation")
    print("3. Inverse Log Transformation")
    print("4. Gamma: nth Power Transformation")
    print("5. Gamma: nth Root Transformation")
    print("6. Gray Slicing with Background")
    print("7. Gray Slicing without Background")
    print("8. Bit Plane Slicing")
    print("9. Exit")
    print("-------------------------------------")
    choice = int(input("Enter Your Choice: "))

    image = cv2.imread("images/pic.jpg", 0)
    image_array = np.array(image)
    print_image(image, "Main Image")

    if choice == 1:
        result = negative(image_array)
        print_image(result, "Negative Transformation")
    elif choice == 2:
        result = log(image_array)
        print_image(result, "Log Transformation")
    elif choice == 3:
        result = inverse_log(image_array)
        print_image(result, "Inverse Log Transformation")
    elif choice == 4:
        result = nth_power(image_array)
        print_image(result, "nth Power Transformation")
    elif choice == 5:
        result = nth_root(image_array)
        print_image(result, "nth RootTransformation")
    elif choice == 6:
        result = gray_slice_with_bg(image_array)
        print_image(result, "Gray Slice With Background")
    elif choice == 7:
        result = gray_slice_without_bg(image_array)
        print_image(result, "Gray Slice With Background")
    elif choice == 8:
        result = bit_plane_slice(image_array)
        print_image(result, "Bit Plane Slicing")
    elif choice == 9:
        break
    else:
        print("Please Enter Valid Choice")
