import cv2
import os #파일 입출력
import numpy as np # 배열 계산
from PIL import Image # 파이썬 이미지 라이브러리
import RPi.GPIO as GPIO
import time
from lcd import drivers
import datetime
id = 0
path = 'dataset'
switch_pin = 5
buzzer_pin = 4
names = ['0000', '1601', '1602', '1603', '1604', '1605', '1606', '1607', '1608', '1609', '1610', '1611', '1612', '1613', '1614', '1615', '1616', '1617', '1618', '1619', '1620', '1621', '1622', '1623', '1624', '1625', '1626', '1627', '1628', '1629', '1630', '1631', '1632' ]

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buzzer_pin, GPIO.OUT)
recognizer = cv2.face.LBPHFaceRecognizer_create()
face_detector = cv2.CascadeClassifier('./xml/face.xml') #haarcascade 얼굴 인식 xml
font = cv2.FONT_HERSHEY_SIMPLEX

display = drivers.Lcd() # lcd 

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = face_detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids

try:
    while True:
        now = datetime.datetime.now() # 현재 시간
        display.lcd_display_string(now.strftime("%x%X"), 1) # 현재 시간 띄우기
        display.lcd_display_string("Press the button", 2)
        check = GPIO.input(switch_pin) # 버튼 눌리면 check를 1로 설정하고 선택옵션 띄우기
        if(check == 1): #버튼 입력을 받았을 때
            display.lcd_display_string("Select option---", 1)
            display.lcd_display_string("---------------------", 2)
            option = input('1: register\n2: recognize\n3: system down\n')
            print("Look at the blue screen(lcd screen) again")
            option = int(option)
            if(option == 1): #유저 등록 과정(얼굴 데이터 쌓고 훈련시키기)
                display.lcd_display_string("---------------------", 2)
                cam = cv2.VideoCapture(0) 
                cam.set(3, 640)
                cam.set(4, 480)
                display.lcd_display_string("Type number => ----", 1)
                display.lcd_display_string("Range : 1 ~ 35-----", 2)
                face_id = input()
                display.lcd_display_string("Type number =>%s---" %face_id, 1)
                display.lcd_display_string("----------------", 2)
                time.sleep(2)
                display.lcd_display_string("Look camera-----", 1)
                count = 0
                while(True):
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_detector.detectMultiScale(
                        gray,
                        scaleFactor = 1.2, #검색 윈도우 확대 비율, 1보다 커야함
                        minNeighbors = 6, #얼굴 사이 최소 간격(픽셀)
                        minSize=(20,20)) #얼굴 최소 크기, 이것보다 작은 사이즈는 확인 x
                    #얼굴인식 된 곳에 사각형으로 나타내주기
                    for(x, y, w, h) in faces:
                        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                        count += 1
                        #dataset의 디렉토리에 user.[id].[count].jpg로 저장
                        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
                        cv2.imshow('image', img)
                    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
                    if k == 27: # esc키를 누르면 종료
                        break
                    elif count >= 60: #등록 사진을 60장 이상 찍으면 종료
                        break
                cam.release()
                cv2.destroyAllWindows()
                #얼굴 학습 
                display.lcd_display_string("Wait-----------", 1)
                print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
                faces,ids = getImagesAndLabels(path)
                recognizer.train(faces, np.array(ids))
                # Save the model into trainer/trainer.yml
                recognizer.write('./traineddataset/trainer.yml') 
                print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
                display.lcd_display_string("Train success-----", 1)
                time.sleep(2)
                display.lcd_display_string("System off-------", 1)
                time.sleep(2)
                break
            if(option == 2):
                recognizer.read('./traineddataset/trainer.yml')
                cam = cv2.VideoCapture(0)
                cam.set(3, 640)
                cam.set(4, 480)
                minW = 0.1*cam.get(3)
                minH = 0.1*cam.get(4)
                while True:
                    display.lcd_display_string("Recognizing.....-----", 1)
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_detector.detectMultiScale(
                        gray,
                        scaleFactor = 1.2,
                        minNeighbors = 5,
                        minSize = (int(minW), int(minH)),
                    )
                    for(x,y,w,h) in faces:
                        cv2.rectangle(img, (x, y), (x+w,y+h), (0,255,0), 2)
                        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                        if (confidence < 100):
                            id = names[id]
                            #precentage는 100 - confidence를 정수형으로 만들어서 계산을 하기 위한 변수
                            percentage = "{0}".format(round(100 - confidence)) 
                            percentage = int(percentage)
                            #confidence는 화면에 얼마나 비슷한 확률로 인식되는지 띄우기 위한 변수
                            confidence = "  {0}%".format(round(100 - confidence))

                            #71퍼 이상의 확률이 나올경우 lcd에 당신이 누군지 출력해주고 부저음을 울려서 문이 열렸다는 것을 알려준 후 시스템을 종료한다.
                            if(percentage >= 71): 
                                display.lcd_display_string("Recognize success----", 1)
                                display.lcd_display_string("You are %s-----"%id, 2)
                                time.sleep(2)
                                display.lcd_display_string("Open the door------", 1)   
                                display.lcd_display_string("--------------", 2)                             
                                cam.release()
                                cv2.destroyAllWindows()
                                pwm = GPIO.PWM(buzzer_pin, 262)
                                pwm.start(50) # duty cycle(0 ~ 100)
                                time.sleep(2)
                                pwm.ChangeDutyCycle(0)
                                pwm.stop()
                                break
                                #확률일정 넘으면 종료되니까 이제 부저 기능만 넣으면됨
                        else:
                            id = "unknown"
                            confidence = "  {0}%".format(round(100 - confidence))
                        
                        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255, 255, 255), 2) #얼굴인식하고 있을 때 유저아이디가 무엇인지 화면에 뜨게해줌
                        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1) #얼굴인식하고 있을 때 몇퍼센트의 확률로 일치하는지 뜨게해줌.

                    cv2.imshow('camera', img)
                    k = cv2.waitKey(10) & 0xff
                    if k == 27: 
                        cam.release()
                        cv2.destroyAllWindows()
                        break
                break
            #실수로 버튼을 눌러서 시스템을 시작했을 경우 3번을 눌러서 그냥 종료시키면 된다.
            if(option == 3):
                display.lcd_display_string("System off-----", 1)
                time.sleep(5)
                break
finally:
    GPIO.cleanup()    
    display.lcd_clear() 
