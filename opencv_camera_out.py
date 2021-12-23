import cv2

cap = cv2.VideoCapture(0) #카메라 장치 열기

if not cap.isOpened():
    print("Camera open failed")
    exit()

# fourcc(four character code)
# DIVX(avi), MP4X(mp4), X264(h264)
fourcc = cv2.VideoWriter_fourcc(*'DIVX') #('D', 'I', 'V', 'X')

out = cv2.VideoWriter('output.avi', fourcc, 30, (640,480)) #파일명, fourcc, 초당프레임, 화면크기
#동영상 촬영하기
while True:
    ret, frame = cap.read() #한 프레임 받아오기
    if not ret:
        break

    cv2.imshow('frame', frame)
    out.write(frame)
    if cv2.waitKey(10) == 13: # 10ms 기다린 후 다음프레임 처리
        break



#사용자 자원 해제 
cap.release()
out.release()
cv2.destroyAllwindows()