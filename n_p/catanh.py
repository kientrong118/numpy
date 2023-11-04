import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh
image = plt.imread('image.jpg')

# Tọa độ vùng cần cắt
x_start, y_start = 300, 300  # Tọa độ góc trái trên của vùng cần cắt
x_end, y_end = 900, 700  # Tọa độ góc phải dưới của vùng cần cắt

# Cắt vùng tự chọn và chuyển các vùng bị cắt thành màu đen
cropped_image = np.copy(image)
cropped_image[:y_start, :] = 0  # Vùng trên vùng cắt
cropped_image[y_end:, :] = 0  # Vùng dưới vùng cắt
cropped_image[:, :x_start] = 0  # Vùng trái vùng cắt
cropped_image[:, x_end:] = 0  # Vùng phải vùng cắt

# Hiển thị ảnh gốc và ảnh đã cắt
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(cropped_image)
plt.title('Cropped Image')

plt.show()