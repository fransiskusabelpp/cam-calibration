import numpy as np
import cv2

# Dimensi papan catur
n_rows = 9  # Number of rows
n_cols = 9  # Number of columns

# Ukuran kotak
square_size = 50

# Warna kotak
white = (255, 255, 255)
black = (0, 0, 0)

# Buat gambar kosong
img = np.zeros((n_rows * square_size, n_cols * square_size, 3), np.uint8)

# Isi kotak dengan warna
for i in range(n_rows):
    for j in range(n_cols):
        color = white if (i + j) % 2 == 0 else black
        cv2.rectangle(img, (j * square_size, i * square_size),
                      ((j + 1) * square_size, (i + 1) * square_size), color, -1)

# Tampilkan gambar
cv2.imshow('Chessboard', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Simpan gambar (opsional)
cv2.imwrite('chessboard_custom.png', img)

