import cv2

for i in range(5):
    cap = cv2.VideoCapture(i)

    if cap.isOpened():
        print(f"Index {i}: TERBUKA")

        ok, frame = cap.read()

        if ok:
            cv2.imshow(f"Kamera index {i}", frame)
            cv2.waitKey(2000)

        cap.release()
        cv2.destroyAllWindows()

    else:
        print(f"Index {i}: tidak tersedia")