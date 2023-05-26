# pip install opencv-python

import cv2

# 0번 카메라(기본 카메라)를 사용하여 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)

# 비디오 프레임 크기 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # 비디오 프레임 읽기
    ret, frame = cap.read()

    # 프레임이 제대로 읽어지지 않았으면 종료
    if not ret:
        break

    # 프레임에 대한 처리 (여기서는 그냥 그대로 화면에 출력)
    cv2.imshow('frame', frame)

    # ESC 키를 누르면 종료
    if cv2.waitKey(1) == 27:
        break

# 비디오 캡처 객체와 윈도우 창 닫기
cap.release()
cv2.destroyAllWindows()
