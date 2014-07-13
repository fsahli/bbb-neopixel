import opc, time

class Neopixel:
	def __init__(self):
		self.numLEDs = 8
		self.pixels = [ (0,0,0) ] * self.numLEDs
		self.client = opc.Client('localhost:7890')

	def update_pixels(self,pixels_to_update,rgb):
		print "Updating pixels"
		for pixel in pixels_to_update:
			self.pixels[pixel] = rgb
		print self.pixels
		for i in range (5):
			self.client.put_pixels(self.pixels)
			time.sleep(0.01)


