from xiApi import Detector

import numpy as np
import pylab as plt

if __name__ == "__main__": 
	d = Detector()
	d.enable_cooling()
	d.set_exposure(1000)

	res = d.get_image()

	plt.figure()
	plt.imshow(res, cmap=plt.cm.gray)
	plt.colorbar()
	plt.show()
