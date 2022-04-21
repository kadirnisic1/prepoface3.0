'''
Autor: Estanislau de Sena Filho
Programa: Detecção Facial em imagens.
'''

import cv2

face_detect = cv2.CascadeClassifier("Classificador/haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

while(True):
    conect, image_video = video.read()

    image_video_gray = cv2.cvtColor(image_video, cv2.COLOR_BGR2GRAY)

    faces_video = face_detect.detectMultiScale(image_video_gray, scaleFactor=1.5, minSize=(100, 100))

    for (x, y, width, heigth) in faces_video:
        cv2.rectangle(image_video, (x, y), (x + width, y + heigth), (0, 255, 0), 2)

    cv2.imshow("Faces Detectadas na Webcam", image_video)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
cv2.destroyAllWindows()
