import cv2

# Haarcascade dosyasının yolu 
#  Githubdan indirip aynı dizine koymanız gerekir 
# Github Link: https://github.com/opencv/opencv/tree/master/data/haarcascades
haar_file = 'haarcascade_frontalface_default.xml'  

# Haarcascade modelini yükleme
face_cascade = cv2.CascadeClassifier(haar_file)

# Eğer model yüklenmezse hata mesajı ver
if face_cascade.empty():
    print("Error: Haarcascade file not loaded properly!")
    exit()

# Kamerayı başlat (0 = Varsayılan Kamera)
cap = cv2.VideoCapture(0)


# Sonsuz döngü ile sürekli kareleri işle
while True:
    # Kameradan kare oku
    ret, frame = cap.read()
    
    # Eğer kare okunamazsa döngüyü bitir
    if not ret:
        print("Error: Couldn't capture frame.")
        break

    # Görüntüyü griye çevir (daha iyi yüz algılama için)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri algıla
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Algılanan yüzler için dikdörtgen çiz
    i = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        i = i+1
  
        # Display the box and faces 
        cv2.putText(frame, 'face num'+str(i), (x-10, y-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2) 


        # Konsola yazdır
        print(f'Face {i}: x={x}, y={y}, w={w}, h={h}')

    # Yüz tespiti olan görüntüyü göster
    cv2.imshow('Detected Faces (Press Q to Exit)', frame)

    # 'q' tuşuna basılırsa çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
