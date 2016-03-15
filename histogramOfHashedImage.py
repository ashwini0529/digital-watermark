from PIL import Image
import numpy

def smoothListGaussian(list,degree=5):
  window=degree*2-1
  weight=numpy.array([1.0]*window)
  weightGauss=[]

  for i in range(window):
    i=i-degree+1
    frac=i/float(window)
    gauss=1/(numpy.exp((4*(frac))**2))
    weightGauss.append(gauss)

  weight=numpy.array(weightGauss)*weight
  smoothed=[0.0]*(len(list)-window)

  for i in range(len(smoothed)):
    smoothed[i]=sum(numpy.array(list[i:i+window])*weight)/sum(weight)

  return smoothed

image_file = 'result.png'
out_file = 'out.tiff'

image = Image.open(image_file).convert('1')
image2 = image.load()
image.save(out_file)

intensities = []

for x in xrange(image.size[0]):
  intensities.append([])

  for y in xrange(image.size[1]):
    intensities[x].append(image2[x, y] )

plot = []

for x in xrange(image.size[0]):
  plot.append(0)

  for y in xrange(image.size[1]):
    plot[x] += intensities[x][y]

plot = smoothListGaussian(plot, 10)

plot_str = ''

for x in range(len(plot)):
  plot_str += str(plot[x]) + "\n"

print(plot_str)