import imageio as imageio
import numpy as np
import matplotlib.pyplot as plt

def rgb_to_grayscale(image):
    return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])

image_path = r'c:\Users\User\Downloads\RGB.jpeg'
image = imageio.imread(image_path)

grayscale_image = rgb_to_grayscale(image)

imageio.imwrite('grayscale.jpg', grayscale_image.astype(np.uint8))

histogram, bins = np.histogram(grayscale_image, bins=256, range=(0, 256))

plt.figure(figsize=(10, 6))
plt.title('Histogram Gambar Grayscale')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Frekuensi')
plt.bar(range(256), histogram, color='gray', alpha=0.7)
plt.savefig('histogram.png')
plt.show()

print("Proses selesai. Cek file grayscale.jpg dan histogram.png")