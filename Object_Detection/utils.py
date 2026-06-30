from ultralytics import YOLO
from PIL import Image
import tempfile
import cv2

# Load YOLOv8 model (downloads automatically if not available)
model = YOLO("yolov8x.pt")


def detect_objects(image, confidence):

    # Save image temporarily
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp:

        image.save(temp.name)

        results = model.predict(
            source=temp.name,
            conf=confidence,
            verbose=False
        )

    result = results[0]

    # Draw bounding boxes
    annotated_image = result.plot()

    # Convert OpenCV (BGR) to RGB
    annotated_image = cv2.cvtColor(
        annotated_image,
        cv2.COLOR_BGR2RGB
    )

    detected_image = Image.fromarray(annotated_image)

    # Count detected objects
    counts = {}

    for box in result.boxes:

        class_id = int(box.cls[0])

        class_name = model.names[class_id]

        counts[class_name] = counts.get(class_name, 0) + 1

    return detected_image, counts