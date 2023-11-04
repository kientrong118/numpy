import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh từ file (ví dụ: 'image.jpg')
image = plt.imread('image.jpg')

# Sao chép ma trận ảnh để tránh thay đổi ảnh gốc
red_image = np.copy(image)
green_image = np.copy(image)
blue_image = np.copy(image)
# Đặt giá trị kênh G và B bằng 0
red_image[:, :, 1] = 0  # Kênh G
red_image[:, :, 2] = 0  # Kênh B
green_image[:, :, 0] = 0  #Kênh R
green_image[:, :, 2] = 0    #Kênh B
blue_image[:, :, 0] = 0 #Kênh R
blue_image[:, :, 1] = 0 #Kênh G
# Hiển thị ảnh gốc và ảnh sau khi chuyển sang màu đỏ
plt.subplot(1, 4, 1)
plt.imshow(image)
plt.title('Ảnh gốc')

plt.subplot(1, 4, 2)
plt.imshow(red_image)
plt.title('Ảnh màu đỏ')

plt.subplot(1, 4, 3)
plt.imshow(green_image)
plt.title('Ảnh màu xanh lá')

plt.subplot(1, 4, 4)
plt.imshow(blue_image)
plt.title('Ảnh màu xanh dương')
plt.show()