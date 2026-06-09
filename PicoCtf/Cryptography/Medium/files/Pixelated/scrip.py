import numpy as np
from PIL import Image

# Open images
im1 = Image.open("scrambled1.png")
im2 = Image.open("scrambled2.png")

# Make into Numpy arrays
im1np = np.array(im1)
im2np = np.array(im2)

# Add images safely
result = im1np.astype(np.uint16) + im2np.astype(np.uint16)
result = np.clip(result, 0, 255).astype(np.uint8)

# Convert back to PIL image and save
Image.fromarray(result).save('result.png')

print("Saved result.png successfully!")