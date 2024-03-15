import numpy as np

# Ganti 'calibration_data.npz' dengan nama file .npz Anda
npz_file = np.load('calibration.npz')

# Mendapatkan daftar kunci dalam file npz
keys = npz_file.files

# Mencetak isi dari setiap kunci
for key in keys:
    print(f"Key: {key}")
    print(npz_file[key])
