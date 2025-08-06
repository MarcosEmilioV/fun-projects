import os 


downloads = r'C:\Users\KSEQUEIRA\Downloads'

extensions = ['.mp3','.pdf','.mp4','.png','.jpg','.exe','.jpeg','.xls','.ogg','.docx','.zip','.rar']


##for file in os.listdir(downloads):
    ##print(file)

for file in os.listdir(downloads):
    for extension in extensions:
        if file.endswith(f"{extension}"):
            print(file)

        else:
            print('not found')
