import os
import cv2

path = "Images/"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = os.path.join(path, file)
        print(file_name)
        images.append(file_name)

count = len(images)
frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)

print(size)

out = cv2.VideoWriter('Project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(count-1):
    image = cv2.imread(images[i])
    out.write(image)

out.release()
print("Done")
