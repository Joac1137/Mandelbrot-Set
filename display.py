from mandelbrot_set import MandelbrotSet
from PIL import Image

mandelbrot_set = MandelbrotSet(max_iterations=20, escape_radius=2)

width, height = 512, 512
scale = 0.0075
GREYSCALE = 'L'

image = Image.new(mode=GREYSCALE, size=(width, height))

for i in range(height):
    for j in range(width):
        c = scale * complex(j - width / 2, height / 2 - i)
        instability = 1 - mandelbrot_set.stability(c, smooth=False)
        image.putpixel((j,i), int(255 * instability))



image.show()