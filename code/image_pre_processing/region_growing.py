import numpy as np
import cv2
import random

class Point(object):
 def __init__(self,x,y):
  self.x = x
  self.y = y

 def getX(self):
  return self.x
 def getY(self):
  return self.y

def getGrayDiff(img,currentPoint,tmpPoint):
 return abs(int(img[currentPoint.x,currentPoint.y]) - int(img[tmpPoint.x,tmpPoint.y]))

def selectConnects(p):
 if p != 0:
  connects = [Point(-1, -1), Point(0, -1), Point(1, -1), Point(1, 0), Point(1, 1), \
     Point(0, 1), Point(-1, 1), Point(-1, 0)]
 else:
  connects = [ Point(0, -1), Point(1, 0),Point(0, 1), Point(-1, 0)]
 return connects

def regionGrow(img,seeds,thresh,p = 1):
 height, weight = img.shape
 seedMark = np.zeros((height,weight,3))
 blank=np.zeros((3));
 mainSeedList = []
 for seed in seeds:
  mainSeedList.append(seed)
 connects = selectConnects(p)
 while(len(mainSeedList)>0):
  label = np.array([random.randrange(255)/255,random.randrange(255)/255,random.randrange(255)/255]);
  label_origin = np.array([random.randrange(255),random.randrange(255),random.randrange(255)]);
  seedList = [mainSeedList.pop()]
  while(len(seedList)>0):
      currentPoint = seedList.pop(0)
      seedMark[currentPoint.x,currentPoint.y] = label
      originImg[currentPoint.x,currentPoint.y] = label_origin
      for i in range(8):
       tmpX = currentPoint.x + connects[i].x
       tmpY = currentPoint.y + connects[i].y
       if tmpX < 0 or tmpY < 0 or tmpX >= height or tmpY >= weight:
        continue
       grayDiff = getGrayDiff(img,currentPoint,Point(tmpX,tmpY))
       if (grayDiff < thresh and (seedMark[tmpX,tmpY] == blank).all()):
        seedMark[tmpX,tmpY] = label
        originImg[tmpX,tmpY] = label_origin
        seedList.append(Point(tmpX,tmpY))
 return seedMark


img = cv2.imread('lean.png',0)
originImg=cv2.imread('lean.png')
#seeds = [Point(40,256)]
seedRaw=np.loadtxt('lean.png.haraff',dtype='i',delimiter=' ')[:,:2]
#seedRaw=np.loadtxt('test.txt',dtype='i',delimiter=' ')[:,:2]
seeds=[]
for temp in seedRaw:
    seeds.append(Point(temp[1],temp[0]));
binaryImg = regionGrow(img,seeds,2.5)
cv2.imshow('1',binaryImg)
cv2.imshow('2',originImg)
cv2.waitKey(0)
