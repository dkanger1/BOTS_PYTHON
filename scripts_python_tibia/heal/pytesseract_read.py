import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
from time import sleep 
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


cap = cv2.VideoCapture(0)
while(True):
    _, frame = cap.read()
    # cv2.imshow("Frame", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("gray", gray)
    plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
    bfilter = cv2.bilateralFilter(gray,11,17,17)
    edged = cv2.Canny(bfilter, 30, 200)
    # cv2.imshow('bila', edged)

    plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
    try:
        keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(keypoints)
        contours = sorted(contours, key = cv2.contourArea, reverse=True)[:10]

        location = None
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:
                location = approx
                break
        location
        mask = np.zeros(gray.shape, np.uint8)
        new_image=cv2.drawContours(mask, [location], 0, 255, -1)
        new_image = cv2.bitwise_and(frame,frame, mask=mask)
        plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
        cv2.imshow("new_image", new_image)

        (x,y) = np.where(mask==255)
        (x1,y1) = (np.min(x), np.min(y))
        (x2,y2) = (np.max(x), np.max(y))
        cropped_image = gray[x1:x2+1, y1:y2+1]

        print(pytesseract.image_to_string(cropped_image))
        # reader = easyocr.Reader(['en'])
        # result = reader.readtext(cropped_image)
        # print(result)

        # text = result [0][-2]
        # print(text)
    except:
        pass
    key = cv2.waitKey(1)  
    if key == 27:
        break      
cap.release()
cv2.destroyAllWindows()