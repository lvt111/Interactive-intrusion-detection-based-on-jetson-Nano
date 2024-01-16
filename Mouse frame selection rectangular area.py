import cv2
def OnMouseAction(event, x, y, flags, param):
    global img, position1, position2,a
    if event == cv2.EVENT_LBUTTONDOWN:  # 按下左键
        position1 = (x, y)
        position2 = None

    if event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:  # 按住左键拖曳不放开
        position2 = (x, y)
        a=0

    elif event == cv2.EVENT_LBUTTONUP:  # 放开左键
        position2 = (x, y)
        a=1


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('image')
    cv2.namedWindow('image2')
    cv2.setMouseCallback('image', OnMouseAction)
    position1 = None
    position2 = None
    img = None
    a=0
    while (1):
        ret, img = cap.read()
        img2=img.copy()
        cv2.circle(img, (100, 100), 50, (255, 0, 0), 5)
        if ret:
            if position1 != None :
                #print(position1, position2)
                cv2.rectangle(img, position1, position2, (0, 0, 255), 3, 4)
                #print(position2)
                if position2!=None:
                    #print(position2[0])
                #print(position2[0])
                    if (position1[0]<100) &(position2[0]>100)&(position1[1]<100)&(position2[1]>100):
                        print("Warning")
                    if a==1:
                        x=position1[0]
                        y=position1[1]
                        xw=position2[0]
                        yh=position2[1]
                        #cut_img = img2[100:200,100:200]
                        # print(position1[0])
                        # print(position1[1])
                        # print(position2[0])
                        # print(position2[1])
                        cut_img = img2[y:yh, x:xw]
                        #print(cut_img[120,100])
                        cv2.imshow('image2', cut_img)

        cv2.imshow('image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

