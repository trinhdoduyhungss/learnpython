import numpy as np
import random

mat = np.random.randint(0, 255, (6, 6))
kernel = np.random.randint(-2, 2, (3, 3))


def conv(matran, kernel):
    kernel = kernel
    print("kernel:\n")
    print(kernel, "\n")

    matran_h = matran.shape[0]
    matran_w = matran.shape[1]

    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]

    h = kernel_h // 2
    w = kernel_w // 2

    matran_conv = np.zeros(matran.shape)

    for i in range(h, matran_h - h):
        for j in range(w, matran_w - w):
            sum = 0
            for m in range(kernel_h):
                for n in range(kernel_w):
                    sum += kernel[m][n] * matran[i - h - m][j - w - n]
                    matran_conv[i][j] = sum
    print('matran_conv:\n')
    print(matran_conv, "\n")
    return matran_conv


conv(mat, kernel)