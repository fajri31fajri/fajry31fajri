
from PIL import Image, ImageDraw

# Buat gambar kosong
images = []
for i in range(10):
    new_image = Image.new('RGB', (200, 200), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)
    draw.text((50, 50), f'Frame {i}', fill='black')
    images.append(new_image)

# Simpan gambar sebagai GIF
images[0].save('output.gif', save_all=True, append_images=images[1:], duration=100, loop=0)

