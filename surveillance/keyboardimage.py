from djitellopy import tello
import KeyPressModule as kp
import time 
import cv2


kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()
global img



def getKeyboardInput():

    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): 
        lr = - speed
    elif kp.getKey("RIGHT"):
        lr = speed

    if kp.getKey("UP"): 
        fb = - speed
    elif kp.getKey("DOWN"):
        fb = speed
        
    if kp.getKey("w"): 
        ud =  speed
        print("up")
    elif kp.getKey("s"):
        ud = -speed
        print("down")

    if kp.getKey("a"): 
        yv = - speed
        print("yaw ccw")
    elif kp.getKey("d"):
        yv = speed
        print("yaw cc")
    
    if kp.getKey("q"): 
        me.land()
        time.sleep(3)
        print("landing")

    if kp.getKey("t"): 
        me.takeoff()
        print("takeoff")

    if kp.getKey("z"): 
        
        if not cv2.imwrite(f'resources/surveilance_images/{time.time()}.jpg', img):
            print("path error")
            time.sleep(0.3)

        else:
            time.sleep(0.3)
            print("taking picture")
    return lr, fb, ud, yv

while True:
    #print(kp.getKey("s"))
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    time.sleep(0.05)
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image" , img)
    cv2.waitKey(1)
