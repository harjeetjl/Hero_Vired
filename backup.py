import sys
import os
import shutil
from datetime import datetime

source_dir = sys.argv[1]
dest_dir = sys.argv[2]

# This is a helper function that checks
# if a directory exists on the file system. It takes a directory name as input and uses the
# `os.path.isdir` function to determine if the specified directory exists. The function returns
# `True` if the directory exists and is a valid directory path, otherwise it returns `False`.
def isDirectoryExists(dirName):
    return os.path.isdir(dirName)

# This function takes a filename as input and appends a timestamp to it
# in the format specified by the `time_format` parameter. It splits the filename into the base
# name and extension, generates a timestamp using the current date and time formatted according to
# the `time_format`, and then concatenates the base name, timestamp, and extension together to
# form a new filename with the timestamp added.
def add_timestamp_to_filename(filename, time_format='%Y%m%d%H%M'):
    base, ext = filename.rsplit('.', 1)
    timestamp = datetime.now().strftime(time_format)
    return f"{base}_{timestamp}.{ext}"

isDirectoryExists(source_dir)
isDirectoryExists(dest_dir)

# fetching all files from source directory
for file_name in os.listdir(source_dir):
    # creating full path
    source_file = os.path.join(source_dir, file_name) 
    dest_file = os.path.join(dest_dir, file_name)
    # To determine whether a file with the same name already exists in the destination directory
    # before copying a file from the source directory. If the file already exists then we are
    # appending timestamp to the file.
    if os.path.exists(dest_file):
        file_name = add_timestamp_to_filename(file_name)
        dest_file = os.path.join(dest_dir, file_name) 
        shutil.copy(source_file, dest_file)
    else:
        shutil.copy(source_file, dest_file)



