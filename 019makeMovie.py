import cv2
import os

#variables for the title rectangle
x,y = 0,0
fontScale = 2
thickness = 2
color = (255, 255, 255)
rectangleColor = (0,0,0)
font = cv2.FONT_HERSHEY_SIMPLEX

#change for each run
framesPerSec = 30
image_type = ".png"
image_folder = 'monte-carlo-png-120'
video_name = 'test-movie.mp4'


#MAGI ;) 
images = [img for img in os.listdir(image_folder) if img.endswith(image_type)]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
video = cv2.VideoWriter(video_name, 0, framesPerSec, (width,height))

for imagePath in images:
	image = cv2.imread(os.path.join(image_folder, imagePath))
	text_size, _ = cv2.getTextSize(imagePath, font, fontScale, thickness)
	text_w, text_h = text_size
	cv2.rectangle(image, (x,y), (x + width, y + text_h*2), rectangleColor, -1)
	cv2.putText(image, imagePath , (x, y + int(text_h*1.5)), font, 
					fontScale, color, thickness, cv2.LINE_AA)
	video.write(image)

cv2.destroyAllWindows()
video.release()