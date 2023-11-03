import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh gốc
image = plt.imread('image.jpg')

# Lấy kích thước ảnh gốc
height, width, channels = image.shape

# Phóng to ảnh gấp đôi
new_height = height * 3
new_width = width * 2

# Phóng to ảnh bằng cách resize
resized_image = np.resize(image, (new_height, new_width, channels))

# Hiển thị ảnh gốc và ảnh đã phóng to
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(resized_image)
plt.title('Resized Image')

plt.show()