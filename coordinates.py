import cv2


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"[{x},{y}],")
        


video_path = 'datos/cars.mp4'  
cap = cv2.VideoCapture(video_path)


if not cap.isOpened():
    print("Error al abrir el video")
    exit()

cv2.namedWindow('Video')
cv2.setMouseCallback('Video', click_event)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Video",frame)

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
