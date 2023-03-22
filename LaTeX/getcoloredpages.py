import pdf2image
import numpy as np
import os

print("Splitting PDF...")
basePath = os.path.dirname(os.path.realpath(__file__))
images = pdf2image.convert_from_path(os.path.join(basePath, "DA_Snowboards/_DABA.pdf"))
sw=0
color=0
for pagenumber, image in enumerate(images):
    img = np.array(image.convert('HSV'))
    hsv_sum = img.sum(0).sum(0)
    if hsv_sum[0] == 0 and hsv_sum[1] == 0:
        sw += 1
    else:
        color += 1
        print("Color:" + str(pagenumber + 1))

print("Total: ")
print("SW" + str(sw))
print("CO" + str(color))