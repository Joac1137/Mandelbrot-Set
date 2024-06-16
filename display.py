from mandelbrot_set import MandelbrotSet
from PIL import Image

mandelbot_set = MandelbrotSet(max_iterations=30)

width, height = 512, 512
scale = 0.0075
BLACK_AND_WHITE = "1"

image = Image.new(mode=BLACK_AND_WHITE, size=(width, height))

for i in range(height):
    for j in range(width):
        c = scale * complex(j - width / 2, height / 2 - i)
        image.putpixel((j,i), c not in mandelbot_set)

image.show()