import sys
from PIL import Image

class Cartoon:
	def __init__( self ):
		self.imageFileList = []

	def merge( self, targetFileName ):
		total_width = 0
		total_height = 0
		imageList = []
		for imageFile in self.imageFileList:
			img = Image.open( imageFile )
			imageList.append( img )
			(width, height) = img.size
			if total_width < width :
				total_width = width
			total_height += height

		new_image = Image.new( "RGB", (total_width, total_height), "white")
		box = (0,0)
		total_height = 0

		for img in imageList:
			new_image.paste(img, box)
			(width, height) = img.size
			total_height += height
			box = (0, total_height)

		new_image.save( targetFileName, quality=100 )
