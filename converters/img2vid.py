import cv2
import os

image_folder = '.'
video_name = 'dices.mkv'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'H264')
video = cv2.VideoWriter(filename=video_name, fourcc=fourcc, fps=24, frameSize=(width, height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

video.release()