import os

# Get the current working directory
base_dir = os.getcwd()

# Create destination folders
pdf_dir = os.path.join(base_dir, "pdf_files")
png_dir = os.path.join(base_dir, "png_files")
exe_dir = os.path.join(base_dir, "Programs")
jpg_dir = os.path.join(base_dir, "jpg_files")
text_dir = os.path.join(base_dir, "text_files")
word_dir = os.path.join(base_dir, "word_files")

# Create folders if they do not exist
for folder in [pdf_dir, png_dir, exe_dir]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Walk through all files and folders
for root, dirs, files in os.walk(base_dir):
    for file in files:
        file_path = os.path.join(root, file)
        extension = os.path.splitext(file)[1].lower()

        # Skip files already inside destination folders
        if root in [pdf_dir, png_dir, exe_dir]:
            continue

        # Move files based on extension
        if extension == ".pdf":
            os.rename(file_path, os.path.join(pdf_dir, file))

        elif extension == ".png":
            os.rename(file_path, os.path.join(png_dir, file))

        elif extension == ".exe":
            os.rename(file_path, os.path.join(exe_dir, file))
        elif extension == ".jpg":
            os.rename(file_path,os.path.join(jpg_dir,file))
        elif extension == ".txt":
            os.rename(file_path,os.path.join(text_dir,file))
        elif extension == ".docx":
            os.rename(file_path,os.path.join(word_dir,file))