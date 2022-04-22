import astropy as apy
from astropy.io import fits

hdul = fits.open("omuamua1.fits.gz")
hdul.info()
hdr = hdul[1].header  


#print(list(hdr.keys()))
#data = hdul[3].data
#print(data.shape)
#print(data.dtype.name)
#print(data[1:4, 1:4])


hdul.close()
