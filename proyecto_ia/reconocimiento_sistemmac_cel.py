import cv2
import mediapipe as mp
import subprocess
import time

# --- CONFIGURACIÓN DE RED ---
# Reemplaza con la IP que aparece en la pantalla de tu Honor
URL_CELULAR = "http://192.168.0.149:8080/video" 

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Optimizamos para que no se trabe por el Wi-Fi
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7, # Un poco menos para ganar velocidad
    min_tracking_confidence=0.6
)

APPS = {1: "Notes", 2: "Calculator", 3: "Google Chrome", 4: "Spotify", 5: "Finder"}

# Variables de estado
x_previa = 0
umbral_swipe = 0.12 # Más sensible para compensar el Wi-Fi
contador_frames = 0
ultimo_conteo = 0
ultimo_lado = ""
REQ_FRAMES = 8 # Menos frames para que se sienta más rápido

def obtener_conteo_limpio(hand_landmarks, label_mp):
    dedos = []
    p4, p2 = hand_landmarks.landmark[4], hand_landmarks.landmark[2]
    # Invertimos la lógica del pulgar porque la cámara IP a veces no viene espejada
    if label_mp == "Left": 
        dedos.append(1 if p4.x < p2.x - 0.01 else 0)
    else:
        dedos.append(1 if p4.x > p2.x + 0.01 else 0)

    tips, bases = [8, 12, 16, 20], [5, 9, 13, 17]
    for t, b in zip(tips, bases):
        if hand_landmarks.landmark[t].y < (hand_landmarks.landmark[b].y - 0.03):
            dedos.append(1)
        else:
            dedos.append(0)
    return sum(dedos)

# Conectando al Honor Magic 7 Lite
cap = cv2.VideoCapture(URL_CELULAR)

print(f"Conectado a la cámara del Honor en: {URL_CELULAR}")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Buscando señal del celular...")
        continue

    # Redimensionamos el frame para que el M4 lo procese volando
    frame = cv2.resize(frame, (640, 480))
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    lado_actual = ""
    conteo_actual = 0

    if result.multi_hand_landmarks:
        for hand_landmarks, hand_info in zip(result.multi_hand_landmarks, result.multi_handedness):
            label_mp = hand_info.classification[0].label
            lado_actual = "Derecha" if label_mp == "Left" else "Izquierda"
            conteo_actual = obtener_conteo_limpio(hand_landmarks, label_mp)
            
            x_actual = hand_landmarks.landmark[9].x
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Lógica de SWIPE para Spotify (Mano Derecha con 4 dedos)
            if lado_actual == "Derecha" and conteo_actual == 4:
                desplazamiento = x_actual - x_previa
                if desplazamiento > umbral_swipe:
                    subprocess.run(["osascript", "-e", 'tell application "Spotify" to play'])
                elif desplazamiento < -umbral_swipe:
                    subprocess.run(["osascript", "-e", 'tell application "Spotify" to pause'])
            
            x_previa = x_actual

            # Lógica de Abrir/Cerrar
            if conteo_actual > 0:
                if conteo_actual == ultimo_conteo and lado_actual == ultimo_lado:
                    contador_frames += 1
                else:
                    ultimo_conteo, ultimo_lado, contador_frames = conteo_actual, lado_actual, 1
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

    cv2.imshow("CONTROL GESTUAL DE MI PORTATIL MAC CEL CAM", frame)
    if cv2.waitKey(1) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()