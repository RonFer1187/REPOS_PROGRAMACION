import cv2
import mediapipe as mp
import numpy as np
import subprocess

# --- CONFIGURACIÓN ---
INDICE_CAMARA = 0 
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.7)

# Diccionario actualizado: Spotify ahora es el 4
APPS = {1: "Notes", 2: "Calculator", 3: "Google Chrome", 4: "Spotify", 5: "Finder"}

# Variables para lógica de movimiento (Swipe)
x_previa = 0
umbral_swipe = 0.15 # Qué tan rápido debe ser el movimiento

# Variables de control
contador_frames = 0
ultimo_conteo = 0
ultimo_lado = ""
REQ_FRAMES = 12

def obtener_conteo_limpio(hand_landmarks, label_mp):
    dedos = []
    # Pulgar
    p4, p2 = hand_landmarks.landmark[4], hand_landmarks.landmark[2]
    if label_mp == "Left": # Derecha
        dedos.append(1 if p4.x < p2.x - 0.01 else 0)
    else: # Izquierda
        dedos.append(1 if p4.x > p2.x + 0.01 else 0)

    # Otros 4 dedos (Referencia nudillos palma 5,9,13,17)
    tips, bases = [8, 12, 16, 20], [5, 9, 13, 17]
    for t, b in zip(tips, bases):
        if hand_landmarks.landmark[t].y < (hand_landmarks.landmark[b].y - 0.03):
            dedos.append(1)
        else:
            dedos.append(0)
    return sum(dedos)

cap = cv2.VideoCapture(INDICE_CAMARA)

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    lado_actual = ""
    conteo_actual = 0

    if result.multi_hand_landmarks:
        for hand_landmarks, hand_info in zip(result.multi_hand_landmarks, result.multi_handedness):
            label_mp = hand_info.classification[0].label
            lado_actual = "Derecha" if label_mp == "Left" else "Izquierda"
            conteo_actual = obtener_conteo_limpio(hand_landmarks, label_mp)
            
            # Punto de referencia para el movimiento (el centro de la palma)
            x_actual = hand_landmarks.landmark[9].x 
            
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # --- LÓGICA DE SWIPE (Solo si Spotify está en uso o detectado) ---
            if conteo_actual == 4:
                # Calculamos el desplazamiento
                desplazamiento = x_actual - x_previa
                
                # De Izquierda a Derecha (X aumenta) -> PLAY
                if desplazamiento > umbral_swipe:
                    subprocess.run(["osascript", "-e", 'tell application "Spotify" to play'])
                    cv2.putText(frame, "MOVIMIENTO: PLAY", (400, 300), 1, 2, (0, 255, 0), 3)
                
                # De Derecha a Izquierda (X disminuye) -> PAUSE
                elif desplazamiento < -umbral_swipe:
                    subprocess.run(["osascript", "-e", 'tell application "Spotify" to pause'])
                    cv2.putText(frame, "MOVIMIENTO: PAUSA", (400, 300), 1, 2, (0, 0, 255), 3)
            
            x_previa = x_actual # Actualizamos para el siguiente frame

            # --- LÓGICA DE ABRIR/CERRAR (Igual que antes) ---
            if conteo_actual > 0:
                if conteo_actual == ultimo_conteo and lado_actual == ultimo_lado:
                    contador_frames += 1
                else:
                    ultimo_conteo = conteo_actual
                    ultimo_lado = lado_actual
                    contador_frames = 1
            else:
                contador_frames = 0

            if contador_frames >= REQ_FRAMES:
                if conteo_actual in APPS:
                    nombre_app = APPS[conteo_actual]
                    if lado_actual == "Derecha":
                        subprocess.Popen(["open", "-a", nombre_app])
                    elif lado_actual == "Izquierda":
                        subprocess.run(["osascript", "-e", f'quit app "{nombre_app}"'])
                contador_frames = 0

    # Interfaz
    if lado_actual != "":
        color = (0, 255, 0) if lado_actual == "Derecha" else (0, 0, 255)
        cv2.putText(frame, f"{lado_actual}: {conteo_actual}", (40, 60), 1, 2, color, 2)

    cv2.imshow("Control Gestual de mi portatil Macbook", frame)
    if cv2.waitKey(1) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()