import hashlib
import Image
import io



#Convert image to binary image...
from PIL import Image 
image_file = Image.open("test.png") # open colour image
image_file = image_file.convert('1') # convert image to black and white
image_file.save('result.png')
print 'Given image converted to Binary'

import imagehash
hash = imagehash.average_hash(Image.open('result.png'))
print 'Hash generated by imagehash : ' + str(hash)
'''
Perceptual hashes are a different concept compared to cryptographic hash functions like MD5 and SHA1. 
With cryptographic hashes, the hash values are random. 
The data used to generate the hash acts like a random seed, so the same data will generate the same result, but different data will create different results. 
Comparing two SHA1 hash values really only tells you two things. If the hashes are different, then the data is different. 
And if the hashes are the same, then the data is likely the same.

'''
#Generate hash value from crated binary image.
img = Image.open('result.png')
m = hashlib.md5()
with io.BytesIO() as memf:
    img.save(memf, 'PNG')
    data = memf.getvalue()
    m.update(data)
hashedValue = (m.hexdigest()) # gives image's hashed value.
print 'Hashed value of image : ' + hashedValue

'''
Encrypt a signature and digest.
Return the digest of the strings passed to the update() method so far. This is a string of digest_size bytes which may contain non-ASCII characters, including null bytes.
Like digest() except the digest is returned as a string of double length, containing only hexadecimal digits. This may be used to exchange the value safely in email or other non-binary environments.

'''
hashedSignature = hashlib.new('ripemd160')
hashedSignature.update("This is the secret key along.")
hashedSignature = hashedSignature.hexdigest()
print 'Hashed encrypted Signature :' + hashedSignature

