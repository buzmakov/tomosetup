from xiApi import Detector

d = Detector()

d.set_exposure(100)
d.enable_cooling()
d.get_image()
