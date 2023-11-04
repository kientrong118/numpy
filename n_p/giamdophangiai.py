import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh gốc
image = plt.imread('image.jpg')

# Lấy kích thước ảnh gốc
height, width, channels = image.shape

# Giảm độ phân giải theo tỷ lệ scale_factor (ví dụ: giảm 50%)
scale_factor = 0.1
new_height = int(height * scale_factor)
new_width = int(width * scale_factor)

# Giảm độ phân giải của ảnh
resized_image = np.zeros((new_height, new_width, channels), dtype=np.uint8)
for c in range(channels):
    for i in range(new_height):
        for j in range(new_width):
            resized_image[i, j, c] = np.mean(image[int(i/scale_factor):int((i+1)/scale_factor),
                                                  int(j/scale_factor):int((j+1)/scale_factor), c])

# Hiển thị ảnh gốc và ảnh đã giảm độ phân giải
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(resized_image)
plt.title('Resized Image')

plt.show()