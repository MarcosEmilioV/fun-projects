import os

path = r"C:\Users\USER\Downloads\[ROKE] KDA Seraphine [Spanish] [HENTAIERA.COM]"

images = []

element = os.listdir(path)


for index,image in enumerate(element):
    nc = image.replace( image, "sc" + f"{index}" + ".jpg")
    oldfile = os.path.join(path, image)
    newfile = os.path.join(path, nc)
    os.rename(oldfile, newfile)  
    

    
    

