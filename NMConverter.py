import numpy
import glob
import cv2

def ConvertNormal(path):
    try:
        grey, _, _, alpha = cv2.split(cv2.imread(path, cv2.IMREAD_UNCHANGED))
        r = numpy.array(alpha, dtype = int)
        g = numpy.array(grey, dtype = int)
        b = numpy.ones(grey.shape, dtype = int) * 255
        cv2.imwrite(path, cv2.merge((b, g, r)))
        print("Converting" + path)

    except:
        print(path + " was not converted")
    
bumps = glob.glob("./Textures/*_BumpMap.png")
blends = glob.glob("./Textures/*_BlendNormalMap.png")
details = glob.glob("./Textures/*_DetailNormalMap.png")

for bump in bumps:
    ConvertNormal(bump)

for blend in blends:
    ConvertNormal(blend)

for detail in details:
    ConvertNormal(detail)
