import os 


downloads = r'C:\Users\USER\Downloads'

extensions = ['.mp3','.pdf','.mp4','.png','.jpg','.exe','.jpeg','.xls','.ogg','.docx','.zip','.rar']

files = os.listdir(downloads)

test = os.path.splitext(r'C:\Users\USER\Downloads\DiscordSetup.exe')
print(test[1])

for file in files:
    extension = os.path.splitext(file)
    if extension[1] in extensions:
        #ordernar
  


##for file in os.listdir(downloads):
    ##print(file)

"""for file in os.listdir(downloads):
    for extension in extensions:
        if file.endswith(f"{extension}"):                                         
            print(file)

        else:
            print('not found')"""
