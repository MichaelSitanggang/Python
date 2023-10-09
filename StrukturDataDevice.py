def find_min_max(arr):
    if len(arr) == 1:
        return arr[0] , arr[0]# Base case: jika hanya ada satu elemen, itu adalah nilai min dan max.

    mid = len(arr) // 2

    left_min, left_max = find_min_max(arr[:mid])  # Rekursif pada separuh kiri dari daftar.

    right_min, right_max = find_min_max(arr[mid:])  # Rekursif pada separuh kanan dari daftar.
  

    return min(left_min, right_min), max(left_max, right_max)

# Memanggil fungsi dengan daftar yang diberikan.
arr = [9, 8, 7, 10, 1, 2, 5, 4]
min_val, max_val = find_min_max(arr)

# Mencetak hasil
print(f"Min : {min_val}")
print(f"Max : {max_val}")
