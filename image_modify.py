from PIL import Image, ImageFilter
import os, sys

ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)

IMAGE_DIR = os.path.join(BASE_DIR, 'images')
IMAGE_EDITED_DIR = os.path.join(BASE_DIR, 'images_edited')

WATERMARK_DIR = os.path.join(BASE_DIR, 'watermark_image')
 
class ImageProcessing:
	def __init__(self, image_dir, image_edited_dir):
		self.WATERMARK_DIR = os.path.join(BASE_DIR, 'watermark_image')
		self.IMAGE_DIR = image_dir
		self.IMAGE_EDITED_DIR = image_edited_dir
		self.EXTENSION_AVAIL = ('jpg', 'jpeg', 'png')


	def __get_image_property(self, image):
		return image.split('.')


	def __create_directory(self, directory):
		IMAGE_STORE_DIR = os.path.join(self.IMAGE_EDITED_DIR, directory)
		if not os.path.exists(IMAGE_STORE_DIR):
			os.makedirs(IMAGE_STORE_DIR)
		return IMAGE_STORE_DIR


	def __join_path(self, BASE, join_to):
		return os.path.join(BASE, join_to)


	def convert_file_extension(self, from_ext, to_ext):
		if from_ext not in self.EXTENSION_AVAIL or to_ext not in self.EXTENSION_AVAIL:
			print("Cannot understand the image format, Please try a jpg, jpeg or png")
			return
		
		if from_ext == to_ext:
			print("From and To extension are the same")
			return

		for image in os.listdir(self.IMAGE_DIR):
			if image.endswith(from_ext):
				image_name, _ = self.__get_image_property(image)
				image_path = self.__join_path(self.IMAGE_DIR, image)

				# Image instance
				img = Image.open(image_path)

				# Create a directory to store converted images
				image_store_dir = self.__create_directory('PNG_FORMAT')

				# Path to store image
				image_store_path = self.__join_path(image_store_dir, f'{image_name}.{to_ext}')
				try:
					img.save(image_store_path)
				except:
					print("Something went wrong")
				else:
					print(f"Successfully converted image {image_name}")


		
	def image_thumbnail(self, size):
		self.SIZE_TUPLE = (size, size)

		for image in os.listdir(self.IMAGE_DIR):
			if image.endswith(self.EXTENSION_AVAIL):
				image_name, image_ext = self.__get_image_property(image)
				image_path = self.__join_path(self.IMAGE_DIR, image)

				# Image instance
				img = Image.open(image_path)
				img.thumbnail(self.SIZE_TUPLE)

				# Create a directory to store converted images
				image_store_dir = self.__create_directory('THUMBNAILS')

				# Path to store image
				image_store_path = self.__join_path(image_store_dir, f'{image_name}-{size}.{image_ext}')
				try:
					img.save(image_store_path)
				except:
					print("Something went wrong")
				else:
					print(f"Converted {image_name} to thumbnail")



	def rotate_image(self, rotate_by):
		try:
			rotate_by = int(rotate_by)
		except:
			print("Not a valid rotate angle")
			return

		for image in os.listdir(self.IMAGE_DIR):
			if image.endswith(self.EXTENSION_AVAIL):
				image_name, image_ext = self.__get_image_property(image)
				image_path = self.__join_path(self.IMAGE_DIR, image)

				# Image instance
				img = Image.open(image_path)

				# Create a directory to store converted images
				image_store_dir = self.__create_directory('ROTATED')

				# Path to store image
				image_store_path = self.__join_path(image_store_dir, f'{image_name}-r{rotate_by}.{image_ext}')
				try:
					img.rotate(rotate_by).save(image_store_path)
				except:
					print("Something went wrong")
				else:
					print(f"Rotated {image_name} by {rotate_by} degree")



	def blackwhite_image(self):
		for image in os.listdir(self.IMAGE_DIR):
			if image.endswith(self.EXTENSION_AVAIL):
				image_name, image_ext = self.__get_image_property(image)
				image_path = self.__join_path(self.IMAGE_DIR, image)

				# Image instance
				img = Image.open(image_path)

				# Create a directory to store converted images
				image_store_dir = self.__create_directory('BW')

				# Path to store image
				image_store_path = self.__join_path(image_store_dir, f'{image_name}-bw.{image_ext}')
				try:
					img.convert(mode="L").save(image_store_path)
				except:
					print("Something went wrong")
				else:
					print(f"Successfully converted {image_name} to black and white image")



	def blur_image(self, blur_by):
		try:
			blur_by = int(blur_by)
		except:
			print("Not a valid Blur value")
			return

		for image in os.listdir(self.IMAGE_DIR):
			if image.endswith(self.EXTENSION_AVAIL):
				image_name, image_ext = self.__get_image_property(image)
				image_path = self.__join_path(self.IMAGE_DIR, image)

				# Image instance
				img = Image.open(image_path)

				# Create a directory to store converted images
				image_store_dir = self.__create_directory('BLURRED')

				# Path to store image
				image_store_path = self.__join_path(image_store_dir, f'{image_name}-blur{blur_by}.{image_ext}')
				try:
					img.filter(ImageFilter.GaussianBlur(blur_by)).save(image_store_path)
				except:
					print("Something went wrong")
				else:
					print(f"Successfully Blurred {image_name} by {blur_by}")



	def compress_image(self, compress_by):
		try:
			compress_by = int(compress_by)
		except:
			print("Not a valid Compress value")
			return

		for image in os.listdir(self.IMAGE_DIR):
			if image.endswith(self.EXTENSION_AVAIL):
				image_name, image_ext = self.__get_image_property(image)
				image_path = self.__join_path(self.IMAGE_DIR, image)

				# Image instance
				img = Image.open(image_path)

				# Create a directory to store converted images
				image_store_dir = self.__create_directory('COMPRESSED')

				# Path to store image
				image_store_path = self.__join_path(image_store_dir, f'{image_name}-c{compress_by}.{image_ext}')
				try:
					img.save(image_store_path, quality = compress_by)
				except:
					print("Something went wrong")
				else:
					print(f"Successfully compressed {image_name} by {compress_by}")



	def add_watermark(self, watermark_img):
		self.WATERMARK_DIM = (42, 42)
		path_to_watermark = self.__join_path(self.WATERMARK_DIR, watermark_img)
		
		if not os.path.isfile(path_to_watermark):
			print("Path to image could not be found")
			return

		for image in os.listdir(self.IMAGE_DIR):
			if image.endswith(self.EXTENSION_AVAIL):
				image_name, image_ext = self.__get_image_property(image)
				if image_ext == 'png':
					print("cannot add watermark to a png file")
					continue
				image_path = self.__join_path(self.IMAGE_DIR, image)

				# Image instance
				img = Image.open(image_path)
				watermark = Image.open(path_to_watermark)

				# Image sizes and dimension
				img_w, img_h = img.size
				watermark_w, watermark_h = watermark.size
				watermark_dim_w, watermark_dim_h = self.WATERMARK_DIM

				if watermark_w >= watermark_dim_w and watermark_h >= watermark_dim_h:
					watermark.thumbnail(self.WATERMARK_DIM)
				
				# Set an offset to paste the watermark on the image
				offset_for_watermark = ((img_w - watermark_dim_w - 5), (img_h - watermark_dim_h - 5)) 

				# Create a directory to store converted images
				image_store_dir = self.__create_directory('WM')

				# Path to store image
				image_store_path = self.__join_path(image_store_dir, f'{image_name}-wm.{image_ext}')
				try:
					img.paste(watermark, offset_for_watermark)
					img.save(image_store_path)
				except:
					print("Something went wrong")
				else:
					print(f"Added watermark to {image_name}")
		


	def filter(self, image, type):
		self.FILTER_TYPE = [
			ImageFilter.BLUR, 
			ImageFilter.CONTOUR, 
			ImageFilter.DETAIL, 
			ImageFilter.EDGE_ENHANCE, 
			ImageFilter.EMBOSS, 
			ImageFilter.FIND_EDGES, 
			ImageFilter.SMOOTH
		]

		if type < 0 or type >= len(self.FILTER_TYPE):
			print("Type is out of range")
			return
		
		image_name, image_ext = self.__get_image_property(image)
		image_path = self.__join_path(self.IMAGE_DIR, image)
		
		if not os.path.isfile(image_path):
			print("Path to image could not be found")
			return
		
		# Image instance
		img = Image.open(image_path)

		# Create a directory to store converted images
		image_store_dir = self.__create_directory('FILTERED')

		# Path to store image
		image_store_path = self.__join_path(image_store_dir, f'{image_name}-filter-{type}.{image_ext}')
		try:
			img.filter(self.FILTER_TYPE[type]).save(image_store_path)
		except:
			print("Something went wrong")
		else:
			print(f"Successfull filtered {image_name}")



	def show_image(self, image):
		image_path = self.__join_path(self.IMAGE_DIR, image)

		if not os.path.isfile(image_path):
			print("Path to image could not be found")
			return
		
		with Image.open(image_path) as img:
			img.show()



if __name__ == "__main__":
	process = sys.argv[1]
	img_processor = ImageProcessing(IMAGE_DIR, IMAGE_EDITED_DIR)
	
	if process == '--convert':
		img_processor.convert_file_extension('jpg', 'png')
	elif process == '--thumbnail':
		img_processor.image_thumbnail(300)
	elif process == '--rotate':
		img_processor.rotate_image(30)
	elif process == '--blackwhite':
		img_processor.blackwhite_image()
	elif process == '--blur':
		img_processor.blur_image(10)
	elif process == '--compress':
		img_processor.compress_image(50)
	elif process == '--filter':
		img_processor.filter('flower.jpg', 3)
	elif process == '--watermark':
		img_processor.add_watermark('mk.png')
	elif process == '--show':
		img_processor.show_image('flower.jpg')
	else:
		print("No matching choice")
