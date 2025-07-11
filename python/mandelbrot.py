import os
path = os.path.abspath(os.getcwd())
filepath = os.path.join(path, "mandelbrot")

repetition = 30
def mandelbrot(c):
  z = [0, 0]
  for i in range(repetition):
    z = helper(z, c)
    if z[0]**2 + z[1]**2 > 4:
      return False
  return True

def helper(z, c):
  sum_real = z[0]**2 - z[1]**2 + c[0]
  sum_imag = 2*z[0]*z[1] + c[1]
  return [sum_real, sum_imag]

def paint():
  real_range = (-2, 2)
  imaginary_range = (-1.5, 1.5)
  num_points_x = 500
  num_points_y = 200

  real_axis = np.linspace(real_range[0], real_range[1], num_points_x)
  imaginary_axis = np.linspace(imaginary_range[0], imaginary_range[1], num_points_y)

  finaltext = ""

  for scaled_y in imaginary_axis:
    finaltext += "\n"
    for scaled_x in real_axis:
      is_in_set = mandelbrot([scaled_x, scaled_y])
      if scaled_x == real_axis[0]:
        finaltext += f"{scaled_y: >8.3g} | "
      if is_in_set:
        finaltext += "-"
      else:
        finaltext += "#"
  f = open(filepath, "wt")
  f.write(finaltext)
  f.close()
  print(finaltext)

paint()
