import struct

# عدد اصلی
dword_value = 1169444480

# تبدیل Dword به float با استفاده از struct
# '>I' نشان‌دهنده استفاده از big-endian برای نمایش عدد صحیح بدون علامت (unsigned int) است
binary_representation = struct.pack('>I', dword_value)

# تبدیل داده باینری به float با استفاده از struct
# '>f' نشان‌دهنده استفاده از big-endian برای نمایش float است
float_value = struct.unpack('>f', binary_representation)[0]

print(f"عدد Dword: {dword_value}")
print(f"عدد Float: {float_value}")
print(f"عدد Float: {float_value}")
