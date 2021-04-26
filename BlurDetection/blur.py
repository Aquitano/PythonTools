import os
import shutil
import cv2

FOCUS_THRESHOLD = 5
BLURRED_DIR = 'blurred'
OK_DIR = 'ok'

blur_count = 0
files = [f for f in os.listdir('.') if f.endswith('.jpeg') or f.endswith('.JPG') or f.endswith(
    '.JPEG') or f.endswith('.HEIC') or f.endswith('.heic') or f.endswith('.png') or f.endswith('.PNG')]

try:
   os.makedirs(BLURRED_DIR)
   os.makedirs(OK_DIR)
except:
   pass

for infile in files:

   cv_image = cv2.imread(infile)

   gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
   variance_of_laplacian = cv2.Laplacian(gray, cv2.CV_64F).var()

   if variance_of_laplacian < FOCUS_THRESHOLD:
      shutil.move(infile, BLURRED_DIR)
      blur_count += 1
   else:
      shutil.move(infile, OK_DIR)

print('Done.  Processed %d files into %d blurred, and %d ok.' % (len(files), blur_count, len(files)-blur_count))
