from mandelbrot_set import MandelbrotSet
from PIL import Image

mandelbot_set = MandelbrotSet(max_iterations=20)

width, height = 512, 512
scale = 0.0075
GREYSCALE = 'L'

image = Image.new(mode=GREYSCALE, size=(width, height))

for i in range(height):
    for j in range(width):
        c = scale * complex(j - width / 2, height / 2 - i)
        instability = 1 - mandelbot_set.stability(c)
        image.putpixel((j,i), int(255 * instability))

image.show()