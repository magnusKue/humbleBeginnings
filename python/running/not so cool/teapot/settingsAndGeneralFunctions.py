import math
def clamp(val, minV, maxV):
    return max(min(val, maxV), minV)

def normalize(v):
    length = math.sqrt(v[0] * v[0] + v[1] * v[1])
    if length > 0:
        v[0] /= length
        v[1] /= length
    else: v = [0,0]
    return v

def scale(v,fac):
    return [v[0]*fac,v[1]*fac]

def getLength(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1])

gameWindowSize=(1200,800)   # 3:2 aspect ratio