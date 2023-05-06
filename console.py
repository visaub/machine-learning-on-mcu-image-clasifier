import serial
from matplotlib import pyplot as plt
import numpy as np

"""
def complement2(b,comp2):
    if comp2:
        return int.from_bytes(bytes.fromhex(b), byteorder='big', signed=True)/256+0.5
    return int(b,16)/256
"""
def complement2(b,comp2):
    if comp2:
        return ((int(b,16)+128)%256)/256
    return int(b,16)/256

def save_image(l_pixels, title, demo_mode):
    R, G, B = [], [], []
    img = np.zeros((32,32,3))
    comp2 = True
    for i in range(1024):
        R.append(complement2(l_pixels[i][4:6],comp2))
        G.append(complement2(l_pixels[i][6:8],comp2))
        B.append(complement2(l_pixels[i][8:10],comp2))
        if demo_mode:    #This is to fix an error because R and B were switched
            img[i//32][i%32] = [B[i],G[i],R[i]]
        else:
            img[i//32][i%32] = [R[i],G[i],B[i]]

    plt.imshow(img, interpolation='nearest')
    plt.title(title)
    plt.savefig('image_Max78000.png')
    
    #plt.show()


def connect():
    ser = serial.Serial('/dev/ttyACM0', baudrate = 115200)
    img_incoming = False
    s_pixels = ''
    while True:
        s = ser.readline().decode('ascii')
        if '*/' in s:
            img_incoming = False
            l_pixels = s_pixels.replace('\n','').replace(' ','').replace('\\\r','').split(',')[:1024]
            s_pixels = ''
        if img_incoming:
            s_pixels += s
        if '/*' in s:
            img_incoming = True
            s_pixels = ''
        if img_incoming == False and '*/' not in s:
            print(s[:-1])
        if 'Demo' in s and '|' in s:
            demo_mode = int(s[6])
        if 'Predicted class' in s:
            title = s.replace('\n','').replace('\\','').replace('\r','')
            save_image(l_pixels, title, demo_mode)
            demo_mode = 0
        


if __name__ == "__main__":
    connect()