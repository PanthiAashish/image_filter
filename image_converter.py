from PIL import Image
import numpy as np

def list_to_image(img_list) -> Image.Image:
  '''Converts a 2D list to an image.'''
  img_arr = np.uint8(np.asarray(img_list))
  img = Image.fromarray(img_arr)
  return img

def image_to_list(img: Image.Image):
  '''Converts an image to a 2D list.'''
  img_arr = np.uint8(np.asarray(img))
  img_list = img_arr.tolist()
  return img_list