from PIL import Image
from PIL import ImageFilter

img1=Image.open("下載.jpg")
img2=img1.filter(ImageFilter.BLUR)
img2.save("out1.jpg")
img3=img1.filter(ImageFilter.CONTOUR)
img3.save("out2.jpg")
img4=img1.filter(ImageFilter.DETAIL)
img4.save("out3.jpg")
img5=img1.filter(ImageFilter.EDGE_ENHANCE)
img5.save("out4.jpg")
img6=img1.filter(ImageFilter.EDGE_ENHANCE_MORE)
img6.save("out5.jpg")