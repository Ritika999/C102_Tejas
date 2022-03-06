import cv2
import dropbox
import random
import time

def take_snapshot():
  print("Went into snapshot function")
  cv = cv2.VideoCapture(0)
  res = True
  imageName = "img" + str(random.randint(1,100)) + ".png"
  while(res):
    result, frame = cv.read()
    cv2.imwrite(imageName, frame)
    res = False
  print("Snapshot taken")
  cv.release()
  cv2.destroyAllWindows()
  return imageName

def upload(imgName):
  dest = "/Demo/" + imgName
  access_token = "uNqQCzFzHnAAAAAAAAAAARf8xrcLcVq2HTPz6KAxFzQxUYnWtPgTp_NBG9pYZotH"
  db = dropbox.Dropbox(access_token)

  f = open(imgName, "rb")
  db.files_upload(f.read(), dest)
def main():
  startTime = time.time()
  while(True):
    currTime = time.time()
    
    if currTime - startTime > 5:
      upload(take_snapshot())
main()