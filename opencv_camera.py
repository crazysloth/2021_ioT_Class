import cv2

cap = cv2.VideoCapture('output.avi') #카메라 장치 열기

if not cap.isOpened():
    print("Camera open failed")
    exit()

#동영상 촬영하기
while True:
    ret, frame = cap.read() #한 프레임 받아오기
    if not ret:
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 13: # 10ms 기다린 후 다음프레임 처리
        break



#사용자 자원 해제 
cap.release()
cv2.destroyAllwindows()