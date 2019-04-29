import numpy as np

mat = np.random.randint(0, 255, (6, 6))
kernel = np.random.randint(-2, 2, (3, 3))

def conv_transform(kernel):
    kernel_copy = kernel.copy()
    for i in range(kernel.shape[0]):
        for j in range(kernel.shape[1]):
            kernel_copy[i][j] = kernel[kernel.shape[0]-i-1][kernel.shape[1]-j-1]
    return kernel_copy

def conv(matran,kernel):
    kernel = conv_transform(kernel)

    matran_h = matran.shape[0]
    matran_w = matran.shape[1]

    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]

    h = kernel_h//2
    w = kernel_w//2

    matran_conv = np.zeros(matran.shape)

    for i in range(h, matran_h-h):
        for j in range(w, matran_w-w):
            sum = 0
            for m in range(kernel_h):
                for n in range(kernel_w):
                    sum += kernel[m][n]*matran[i-h-m][j-w-n]
                matran_conv[i][j] = sum
    print('matran_conv',matran_conv)
    return matran_conv

conv(mat,kernel)