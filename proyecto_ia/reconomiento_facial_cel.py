import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import os
from scipy.spatial import distance

# --- CONFIGURACIÓN ---
URL_ANDROID = "http://192.168.0.149:8080/video" # Ajusta tu IP
MODEL_PATH = 'face_detector.tflite'
FOTOS_PATH = 'fotos'
UMBRAL_PRECISION = 0.15 

# 1. Configuración del Detector
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
    
    if not os.path.exists(FOTOS_PATH):
        print(f"Error: No existe la carpeta {FOTOS_PATH}")
        return [], []

    print("--- Cargando Base de Datos (Múltiples ángulos por persona) ---")
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
                y, x, h, w = int(bbox.origin_y), int(bbox.origin_x), int(bbox.height), int(bbox.width)
                face_crop = img_rgb[max(0,y):y+h, max(0,x):x+w]
                
                if face_crop.size > 0:
                    vector = procesar_rostro(face_crop)
                    known_faces.append(vector)
                    
                    # --- LÓGICA DE NOMBRE LIMPIO ---
                    # Si el archivo es "Ronald_1.jpg", esto extrae solo "Ronald"
                    nombre_sucio = os.path.splitext(archivo)[0]
                    nombre_limpio = nombre_sucio.split('_')[0] 
                    known_names.append(nombre_limpio)
                    
                    print(f"[OK] {archivo} cargado como: {nombre_limpio}")
    return known_faces, known_names

rostros_db, nombres_db = registrar_personas()
cap = cv2.VideoCapture(URL_ANDROID)

while cap.isOpened():
    success, frame = cap.read()
    if not success: continue

    frame = cv2.resize(frame, (854, 480))
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
    results = detector.detect(mp_image)

    if results.detections:
        for detection in results.detections:
            bbox = detection.bounding_box
            x, y, w, h = int(bbox.origin_x), int(bbox.origin_y), int(bbox.width), int(bbox.height)
            face_crop = frame_rgb[max(0,y):y+h, max(0,x):x+w]
            
            nombre = "Desconocido"
            color = (0, 0, 255)

            if face_crop.size > 0:
                vector_actual = procesar_rostro(face_crop)
                distancias = [distance.cosine(vector_actual, v_db) for v_db in rostros_db]
                
                if distancias and min(distancias) < UMBRAL_PRECISION:
                    indice = np.argmin(distancias)
                    nombre = nombres_db[indice]
                    color = (0, 255, 0)

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, nombre.upper(), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.imshow('Feria IA - Honor Magic 7 Lite', frame)
    if cv2.waitKey(1) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()