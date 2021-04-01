import cv2
import os
import string
import os
import moviepy.video.io.ImageSequenceClip
from PIL import Image
import glob





def makeMovie_GW(image_folder = '/Users/floorbroekgaarden/Projects/GitHub/GW-visulazation/movie_BHmass_spin/',fps=.4, duration=400):
	'''
	whichRate = 'intrinsic' or 'observed'
	fps=0.4, frames per second
	duration = duration of the movie 
	'''



	images = []
                
  
	


	for f_ind  in range(88):
		images.append(image_folder +  'img_'  + str(f_ind) + '.png')


	image_files = images
	clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
	clip.write_videofile(image_folder+'movie_BHmass_spin' + '.mp4')


	# make also gif:
 
	# Create the frames
	frames = []
	# imgs = glob.glob("*.png")
	for i in images:
	    new_frame = Image.open(i)
	    frames.append(new_frame)
	 
	# Save into a GIF file that loops forever
	frames[0].save(image_folder+'gif_'+ 'movie_BHmass_spin' +  '.gif', format='GIF',
	               append_images=frames[1:],
	               save_all=True,
	               duration=duration, loop=0)



	return 



Movie_GW=True



# Run rhis using python 3!! 

if Movie_GW==True:
	makeMovie_GW(image_folder='/Users/floorbroekgaarden/Projects/GitHub/GW-visulazation/movie_BHmass_spin/', fps=.4, duration=300)
	

