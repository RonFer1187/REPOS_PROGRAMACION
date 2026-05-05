import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import os
from scipy.spatial import distance

# --- CONFIGURACIÓN MAC ---
MODEL_PATH = 'face_detector.tflite'
FOTOS_PATH = 'fotos'
UMBRAL_PRECISION = 0.15 

base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.FaceDetectorOptions(base_options=base_options)
detector = vision.FaceDetector.create_from_options(options)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

def procesar_rostro(face_roi):
    gray = cv2.cvtColor(face_roi, cv2.COLOR_RGB2GRAY)
    normalized = clahe.apply(gray)
    resized = cv2.resize(normalized, (64, 64))
    return resized.flatten().astype(np.float32)

def registrar_personas():
    known_faces = []
    known_names = []
    print("--- Registrando Base de Datos ---")
    for archivo in os.listdir(FOTOS_PATH):
        if archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            path = os.path.join(FOTOS_PATH, archivo)
            img = cv2.imread(path)
            if img is None: continue
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            mp_img = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)
            res = detector.detect(mp_img)
            if res.detections:
                bbox = res.detections[0].bounding_box
                face_crop = img_rgb[int(bbox.origin_y):int(bbox.origin_y+bbox.height), 
                                   int(bbox.origin_x):int(bbox.origin_x+bbox.width)]
                if face_crop.size > 0:
                    known_faces.append(procesar_rostro(face_crop))
                    # Lógica: Ronald_1 -> Ronald
                    known_names.append(os.path.splitext(archivo)[0].split('_')[0])
    return known_faces, known_names

rostros_db, nombres_db = registrar_personas()
cap = cv2.VideoCapture(0) # Para usar camara canon probar con 1 o 2 hasta que abra la Canon

while cap.isOpened():
    success, frame = cap.read()
    if not success: break
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
    results = detector.detect(mp_image)

    if results.detections:
        for detection in results.detections:
            bbox = detection.bounding_box
            x, y, w, h = int(bbox.origin_x), int(bbox.origin_y), int(bbox.width), int(bbox.height)
            x_inv = frame.shape[1] - x - w
            face_crop = frame_rgb[max(0,y):y+h, max(0,x):x+w]
            nombre = "Desconocido"
            color = (0, 0, 255)
            if face_crop.size > 0:
                vector_actual = procesar_rostro(face_crop)
                distancias = [distance.cosine(vector_actual, v_db) for v_db in rostros_db]
                if distancias and min(distancias) < UMBRAL_PRECISION:
                    nombre = nombres_db[np.argmin(distancias)]
                    color = (0, 255, 0)
            cv2.rectangle(frame, (x_inv, y), (x_inv + w, y + h), color, 2)
            cv2.putText(frame, nombre.upper(), (x_inv, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.imshow('Feria Stand - MacBook M4', frame)
    if cv2.waitKey(1) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()