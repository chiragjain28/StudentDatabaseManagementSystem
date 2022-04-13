# from tkinter.filedialog import askopenfile, askopenfilename
# # import io
from tkinter import *
import cv2
import face_recognition
import numpy as np
from PIL import Image,ImageTk  # to deal with images
import os

class recognition_Class:     
    def __init__(self,root):
        self.root=root      #initialize root
        self.root.title("Student Management System")
        self.root.geometry("400x400+450+130")  #width x height + x axis(left corner) + top position
        self.root.config(bg="white")
        #==== Title =====#
        title=Label(self.root,text="Student Details",
        font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10 , y=15 ,width=1180,height=35)
        
    def myFile(self):
        path = 'faces_rec'
        images = []     # LIST CONTAINING ALL THE IMAGES
        className = []    # LIST CONTAINING ALL THE CORRESPONDING CLASS Names
        myList = os.listdir(path)
        print("Total Classes Detected:",len(myList))
        for x,cl in enumerate(myList):
                curImg = cv2.imread(f'{path}/{cl}')
                images.append(curImg)
                className.append(os.path.splitext(cl)[0])
        return images,className

    def findEncodings(self,images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            print(img)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        print('Encodings Complete')
        return encodeList

    # def captureScreen(bbox=(300,300,690+300,530+300)):
    #     capScr = np.array(ImageGrab.grab(bbox))
    #     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    #     return capScr

    def capture(self,encodeListKnown,className):
        count=0
        cap = cv2.VideoCapture(0)
        while True:
            try:
                
                success, img = cap.read()
                # img = captureScreen()
                # cv2.imwrite('picture.jpg',img)
                # cv2.destroyAllWindows()
                imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25,interpolation = cv2.INTER_CUBIC)
                # frame = cv2.resize(frame,(224,224),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
                imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

                facesCurFrame = face_recognition.face_locations(imgS)
                encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

                for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
                    count=count+1 
                    matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                    print(matches)
                    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                    matchIndex = np.argmin(faceDis)
                    print(matchIndex)
                    # if faceDis[matchIndex]< 0.50:
                    #     name = classNames[matchIndex].upper()
                    #     markAttendance(name)
                    # else: name = 'Unknown'
                    # #print(name)
                    # y1,x2,y2,x1 = faceLoc
                    # y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                    # cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                    # cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    # cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

                    if matches[matchIndex]:
                        name = className[matchIndex]
                    else:
                        name="Unknown"
                    y1,x2,y2,x1=faceLoc
                    y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
                    print(className)
                    if True in matches:
                        print("arey bhr nikal")
                        cv2.destroyAllWindows()
                        cap.release()
                        self.root.destroy()
                        # os.system("python dashboard.py")
                        exit()
        
                cv2.imshow('Webcam',img)
                cv2.waitKey(1)
            except Exception as e:
                print(e)

          
        # cv2.destroyAllWindows()
        # cap.release()
        # break

if __name__=="__main__":
    root=Tk()         #create object of tkinter module
    obj=recognition_Class(root)     #create object of RMS class and pass root obj
    images,className=obj.myFile()
    encodeListKnown = obj.findEncodings(images)
    obj.capture(encodeListKnown,className)
    root.mainloop()  #for continously show on screen



#     if faceDis[matchIndex]< 0.50:
#     name = classNames[matchIndex].upper()
#     markAttendance(name)
# else: name = 'Unknown'
# #print(name)
# y1,x2,y2,x1 = faceLoc
# y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
# cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
# cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
# cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)