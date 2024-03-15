import numpy as np
import cv2

# Fungsi untuk memuat parameter kalibrasi kamera dari file .npz
def load_calibration_data(calibration_file):
    with np.load(calibration_file) as data:
        camera_matrix = data['camMatrix']
        distortion_coefficients = data['distCoeff']
    return camera_matrix, distortion_coefficients

# Fungsi untuk menghilangkan distorsi dari frame
def undistort_frame(frame, camera_matrix, distortion_coefficients):
    h, w = frame.shape[:2]
    new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, distortion_coefficients, (w,h), 1, (w,h))
    undistorted_frame = cv2.undistort(frame, camera_matrix, distortion_coefficients, None, new_camera_matrix)
    x, y, w, h = roi
    undistorted_frame = undistorted_frame[y:y+h, x:x+w]
    return undistorted_frame

# Main program
if __name__ == "__main__":
    # Mengganti 'calibration_data.npz' dengan nama file .npz Anda
    calibration_file = 'calibration.npz'

    # Memuat parameter kalibrasi kamera
    camera_matrix, distortion_coefficients = load_calibration_data(calibration_file)

    # Membuka kamera
    cap = cv2.VideoCapture(0)

    while True:
        # Membaca frame dari kamera
        ret, frame = cap.read()
        if not ret:
            break

        # Menghilangkan distorsi dari frame
        undistorted_frame = undistort_frame(frame, camera_matrix, distortion_coefficients)

        # Menampilkan frame yang sudah diperbaiki
        cv2.imshow('Undistorted Frame', undistorted_frame)

        # Menggunakan tombol escape (ASCII 27) untuk keluar dari loop
        key = cv2.waitKey(1)
        if key == 27:  # ASCII 27 adalah kode escape
            break

    # Melepaskan kamera dan menutup semua jendela
    cap.release()
    cv2.destroyAllWindows()
