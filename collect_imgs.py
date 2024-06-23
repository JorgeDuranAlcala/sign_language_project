import os
import cv2
import time

DATA_DIR = "./data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 6
dataset_size = 100

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print("Collecting data for class {}".format(j))

    done = False
    while not done:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting...")
            break

        cv2.putText(
            frame,
            'LISTO? Presiona la tecla "Q"! :)',
            (100, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            3,
            cv2.LINE_AA,
        )
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("q"):
            done = True

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting...")
            break

        cv2.imshow("frame", frame)
        cv2.waitKey(1)
        cv2.imwrite(os.path.join(class_dir, "{}.jpg".format(counter)), frame)

        counter += 1
        time.sleep(0.1)  # adjust the frame rate

cap.release()
cv2.destroyAllWindows()
