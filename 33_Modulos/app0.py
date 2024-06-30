import cv2 # type: ignore
imagen = cv2.imread('gato.jpg')
#cv2.imshow('gato',imagen)
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagen en escala grises',gris)
cv2.waitKey(0)