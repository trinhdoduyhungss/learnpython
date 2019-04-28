import numpy as np

#khởi tạo ma trận
mat = np.random.randint(0, 255, (6, 6))

M, N = mat.shape
K = 2 # độ dời
L = 2 # độ dài

MK = M // K
#print(MK)
NL = N // L
#print(NL)
matran_maxpool = mat[:MK*K, :NL*L].reshape(MK, K, NL, L).max(axis=(1, 3))
print(matran_maxpool)
