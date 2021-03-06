import glob
import os
from moviepy.editor import *
from PIL import Image

def padImage(targetDirectory):
	file_list=glob.glob(targetDirectory+'/*.png')

	for FNAME in file_list:
		with open(str(FNAME), 'rb') as FILE:
			print FNAME
			top=Image.open(FILE).convert('RGBA')
			new_w=1500
			new_h=4000
			background=Image.new('RGBA',size=(new_w,new_h),color=(0,0,0,0))
			background.paste(top,(0,0))
			background.save(FNAME)
			FILE.close()


#makes a timelapse from the files within the provided directory
#@targetDirectory: absloute path of the the directory
#@returns: full path to the output file
def exportToTimelapse(targetDirectory, output):

	padImage(targetDirectory)

	file_list=glob.glob(targetDirectory + '/*.png')
	file_list.sort()
	
	clip=ImageSequenceClip(file_list,fps=12)
	clip.write_videofile(output,threads=4,preset="fast",fps=12)


	return os.path.dirname(output)
