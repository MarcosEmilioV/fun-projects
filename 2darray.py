import os

path = r"C:\Users\USER\Pictures\programtest"
imagepath= []

imagepath_andindex = []

for image in os.listdir(path):
    imagepath.append(image)

for index, image in enumerate(os.listdir(path)):
    imagepath_andindex.append([image, index])


print(imagepath_andindex)