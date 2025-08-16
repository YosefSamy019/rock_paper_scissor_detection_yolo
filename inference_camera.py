from ultralytics import YOLO
import cv2
import time

model = YOLO("run-yolov8-training/exp1/weights/best.pt")
class_names = model.model.names

video_path = 0  # webcam
cap = cv2.VideoCapture(video_path)

# For FPS calculation
prev_time = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Start time
    start_time = time.time()

    # Mirror
    frame = cv2.flip(frame, 1)

    # Run YOLO prediction
    results = model(frame)

    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls = class_names[int(box.cls[0])]
        conf = float(box.conf[0])

        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(frame, f"{cls} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # FPS calculation
    end_time = time.time()
    fps = 1 / (end_time - start_time)

    # Draw FPS
    cv2.putText(frame, f"FPS: {fps:.2f}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('YOLO', frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
