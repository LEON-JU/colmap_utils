import numpy as np

mtx = np.array([[9.85868019e+02, 0.00000000e+00, 1.04366498e+03],
                [0.00000000e+00, 9.87171297e+02, 7.71141218e+02],
                [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
dist = np.array([[ 1.01815114e-01, -1.35854273e-01,  7.60394026e-05,  1.59990156e-03,  9.73049541e-02]])

# 提取内参矩阵的元素
fx = mtx[0, 0]
fy = mtx[1, 1]
cx = mtx[0, 2]
cy = mtx[1, 2]

# 提取畸变系数，OpenCV Camera Model只需要前两个径向畸变系数和两个切向畸变系数 实际对应了k1 k2 k4 k5 等同于k3设置为0！（高阶纵向畸变）
k1 = dist[0][0]
k2 = dist[0][1]
p1 = dist[0][3]
p2 = dist[0][4]

# 打印OpenCV Camera Model参数
print("OpenCV Camera Model Parameters:")
print("fx:", fx)
print("fy:", fy)
print("cx:", cx)
print("cy:", cy)
print("k1:", k1)
print("k2:", k2)
print("p1:", p1)
print("p2:", p2)