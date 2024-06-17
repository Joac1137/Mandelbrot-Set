
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import matplotlib.animation as animation

def z(n, c):
    
    if n == 0:
        return 0
    else:
        return z(n - 1, c)**2 + c
    
def sequence(c, z=0):
    z = 0
    while True:
        yield z
        z = z ** 2 + c

def mandelbrot(candidate):
    return sequence(c=candidate)

def julia(candidate, parameter):
    return sequence(c=candidate, z=parameter)

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))

    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def is_stable(c, num_iterations):
    z = 0
    for _ in tqdm(range(num_iterations)):
        z = z ** 2 + c
    return abs(z) <= 2

def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]

fig = plt.figure(figsize=(10, 10))  # instantiate a figure to draw
ax = plt.axes()  # create an axes object

def animate(i):
    c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=1000)
    
    ax.clear()
    ax.set_xticks([], [])
    ax.set_yticks([], [])

    num_iterations = round(1.15**(i + 1))
    X = is_stable(c=c, num_iterations=num_iterations)
    
    # associate colors to the iterations with an iterpolation
    img = ax.imshow(X, interpolation="bicubic", cmap='magma')
    return [img]
 
anim = animation.FuncAnimation(fig, animate, frames=45, interval=120, blit=True)
anim.save('mandelbrot.gif',writer='imagemagick')



# plt.imshow(is_stable(c, num_iterations=20), cmap="binary")
# plt.gca().set_aspect("equal")
# plt.axis("off")
# plt.tight_layout()
# plt.show()