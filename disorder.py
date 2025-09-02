import os 

downloads = r'C:\Users\KSEQUEIRA\Downloads'

image_folder = r'C:\Users\KSEQUEIRA\Downloads\images'
doc_folder = r'C:\Users\KSEQUEIRA\Downloads\docs'
spreadsheet_folder = r'C:\Users\KSEQUEIRA\Downloads\spreadsheets'
executables_folder = r'C:\Users\KSEQUEIRA\Downloads\executables'
videos_folder = r'C:\Users\KSEQUEIRA\Downloads\videos'
audio_folder = r'C:\Users\KSEQUEIRA\Downloads\audios'
compressed_folder = r'C:\Users\KSEQUEIRA\Downloads\compressed'



extension_images = [".png", ".jpeg", ".bmp"]
extension_docs = ['.docx','.pdf']
extension_spreadsheets = [".xls"] 
extension_folders = [".rar", ".zip"]
extension_executables = [".exe"]
extension_audio = ['.mp3', '.ogg']
extension_videos = [".mp4"]

files_images = os.listdir(image_folder)
files_docs = os.listdir(doc_folder)
files_executables = os.listdir(executables_folder)
files_audio = os.listdir(audio_folder)
files_video = os.listdir(videos_folder)
files_compressed = os.listdir(compressed_folder)
files_spreadsheets = os.listdir(spreadsheet_folder)



for file in files_images:
    extension = os.path.splitext(file)
    if extension[1] in extension_images:
        old_path = downloads + f"\\{file}"
        new_path = image_folder + f"\\{file}"
        os.rename(new_path, old_path)
for file in files_executables:
    extension = os.path.splitext(file)
    if extension[1] in extension_folders:
        old_path = downloads + f"\\{file}"
        new_path = compressed_folder + f"\\{file}"
        os.rename(new_path, old_path)
for file in files_docs:
    extension = os.path.splitext(file)
    if extension[1] in extension_docs:
        old_path = downloads + f"\\{file}"
        new_path = doc_folder + f"\\{file}"
        os.rename(new_path, old_path)
for file in files_spreadsheets:
    extension = os.path.splitext(file)
    if extension[1] in extension_spreadsheets:
        old_path = downloads + f"\\{file}"
        new_path = spreadsheet_folder + f"\\{file}"
        os.rename(new_path, old_path)
for file in files_compressed:
    extension = os.path.splitext(file)
    if extension[1] in extension_folders:
        old_path = downloads + f"\\{file}"
        new_path = compressed_folder + f"\\{file}"
        os.rename(new_path, old_path)
for file in files_audio:
    extension = os.path.splitext(file)
    if extension[1] in extension_audio:
        old_path = downloads + f"\\{file}"
        new_path = audio_folder + f"\\{file}"
        os.rename(new_path, old_path)
for file in files_video:
    extension = os.path.splitext(file)
    if extension[1] in extension_videos:
        old_path = downloads + f"\\{file}"
        new_path = videos_folder + f"\\{file}"
        os.rename(new_path, old_path)
for file in files_executables:
    extension = os.path.splitext(file)
    if extension[1] in extension_executables:
        old_path = downloads + f"\\{file}"
        new_path = executables_folder + f"\\{file}"
        os.rename(new_path, old_path)
  

