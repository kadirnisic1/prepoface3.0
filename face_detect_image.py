# '''
# Autor: Estanislau de Sena Filho
# Programa: Detecção Facial em imagens.
# '''

# import cv2

# face_classifier = cv2.CascadeClassifier("Classificador/haarcascade_frontalface_default.xml")

# image = cv2.imread("Imagens/scientists.jpg")

# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# faces_detect = face_classifier.detectMultiScale(image_gray, scaleFactor=1.2, minSize=(30,30), minNeighbors=4)

# while(True):
#     for(x, y, width, height) in faces_detect:
#         cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

#     cv2.imshow("Face Detectadas", image)
#     cv2.waitKey(1)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()

import cv2 image = cv2.imread ("./ put / do / image.extension") cv2.imshow ("Slika", slika) cv2.waitKey (0) cv2.destroyAllWindows ()