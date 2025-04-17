import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Görüntü alınamadı.")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # BEYAZ RENK için HSV aralığı (AirPods gibi nesneler)
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 40, 255])


    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Gürültü temizliği
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)
        M = cv2.moments(largest_contour)

        if M["m00"] > 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            if radius > 10:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
                cv2.circle(frame, center, 5, (255, 0, 0), -1)
                cv2.putText(frame, f"Konum: {center}", (center[0]+10, center[1]),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("AirPods Takibi", frame)
    cv2.imshow("Maske", mask)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
