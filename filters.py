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



def rotate_180(pixels):
  new_pixels = copy.deepcopy(pixels)
  top = 0
  bottom = len(pixels) - 1
  while bottom > top:
    # new_pixels[top], new_pixels[bottom] = new_pixels[bottom], new_pixels[top]
    temp = new_pixels[top] 
    new_pixels[top] = new_pixels[bottom]
    new_pixels[bottom] = temp

    bottom -= 1
    top += 1

  for row in range(len(pixels)):
    left = 0
    right = len(pixels[0]) - 1
    while right > left:
      # new_pixels[row][l], new_pixels[row][r] = new_pixels[row][r], new_pixels[row][l]
      temp = new_pixels[row][left]
      new_pixels[row][left] = new_pixels[row][right]
      new_pixels[row][right] = temp
      right -= 1
      left += 1

  return new_pixels




pb_img = Image.open("fisk_gate.png")
pixels = image_to_list(pb_img)

# Save an image
new_pb_img = list_to_image(changed_pixels)
new_pb_img.save("fisk_gate_new.png")