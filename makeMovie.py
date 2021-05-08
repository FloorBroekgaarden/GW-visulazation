import cv2
import os
import string
import os
import moviepy.video.io.ImageSequenceClip
from PIL import Image
import glob





def makeMovie_GW(image_folder = '/Users/floorbroekgaarden/Projects/GitHub/GW-visulazation/movie_BHmass_spin/',fps=.4, duration=400, name='movie_BHmass_spin', img_range=259):
	'''
	whichRate = 'intrinsic' or 'observed'
	fps=0.4, frames per second
	duration = duration of the movie 
	'''



	images = []
                
  
	

	# automatize to length -1 no of files. 
	for f_ind  in range(img_range):
		images.append(image_folder +  'img_'  + str(f_ind) + '.png')


	image_files = images
	clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
	clip.write_videofile(image_folder+name + '.mp4')


	# make also gif:
 
	# Create the frames
	frames = []
	# imgs = glob.glob("*.png")
	for i in images:
	    new_frame = Image.open(i)
	    frames.append(new_frame)
	 
	# Save into a GIF file that loops forever
	frames[0].save(image_folder+'gif_'+ name +  '.gif', format='GIF',
	               append_images=frames[1:],
	               save_all=True,
	               duration=duration, loop=0)



	return 



Movie_GW_BHmassVSspin = False 
Movie_GW_BHmassVSradiusISCO = False
Movie_GW_BHmassVSradius  =True 
Movie_GW_BHmassVSradius_NL=True

# Run rhis using python 3!! 

if Movie_GW_BHmassVSspin==True:
	makeMovie_GW(image_folder='/Users/floorbroekgaarden/Projects/GitHub/GW-visulazation/movie_BHmass_spin/', fps=.4, duration=300, name='movie_BHmass_spin')
	
if Movie_GW_BHmassVSradiusISCO==True:
	makeMovie_GW(image_folder='/Users/floorbroekgaarden/Projects/GitHub/GW-visulazation/movie_BHmass_RadiusISCO/', fps=.4, duration=300, name='movie_BHmass_RadiusISCO')


if Movie_GW_BHmassVSradius==True:
	makeMovie_GW(image_folder='/Users/floorbroekgaarden/Projects/GitHub/GW-visulazation/movie_BHmass_Rs/', fps=2, duration=300, name='movie_BHmass_Rs',img_range=230)


if Movie_GW_BHmassVSradius_NL==True:
	makeMovie_GW(image_folder='/Users/floorbroekgaarden/Projects/GitHub/GW-visulazation/movie_BHmass_Rs_NL/', fps=2, duration=300, name='movie_BHmass_Rs_NL',img_range=230)






