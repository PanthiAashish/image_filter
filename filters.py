from PIL import Image
from image_converter import list_to_image, image_to_list
import copy

# An example function provided for you that darkens an image.
def darken(pixels):
  new_pixels = copy.deepcopy(pixels)
  for row in range(len(pixels)):
    for col in range(len(pixels[row])):
      r = new_pixels[row][col][0]
      g = new_pixels[row][col][1]
      b = new_pixels[row][col][2]
      new_pixels[row][col] = [r / 2, g / 2, b / 2]
  return new_pixels


def red_stripes(pixels):
  new_pixels = copy.deepcopy(pixels)

  for row in range(len(pixels)):
    for col in range(len(pixels[row])):
      r = new_pixels[row][col][0]
      g = new_pixels[row][col][1]
      b = new_pixels[row][col][2]
      
      if col % 100 < 50:
        new_pixels[row][col] = [255, 0, 0]
      else:
        new_pixels[row][col] = [r, g, b]
      
  return new_pixels


def border(pixels, color):
  new_pixels = copy.deepcopy(pixels)

  for row in range(30):
    for col in range(len(pixels[row])):
      new_pixels[row][col] = color
  
  for row in range(len(pixels)):
    for col in range(30):
      new_pixels[row][col] = color
  
  for row in range(len(pixels)):
    for col in range(len(pixels[row])-30, len(pixels[row])):
      new_pixels[row][col] = color
  
  for row in range(len(pixels) - 30, len(pixels)):
    for col in range(len(pixels[row])):
      new_pixels[row][col] = color

  return new_pixels