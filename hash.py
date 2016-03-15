import hashlib
import Image
import io



#Convert image to binary image...
from PIL import Image 
image_file = Image.open("test.png") # open colour image
image_file = image_file.convert('1') # convert image to black and white
image_file.save('result.png')
print 'Binary converted'

#Generate hash value from crated binary image.
img = Image.open('result.png')
m = hashlib.md5()
with io.BytesIO() as memf:
    img.save(memf, 'PNG')
    data = memf.getvalue()
    m.update(data)
hashedValue = (m.hexdigest()) # gives image's hashed value.
print hashedValue