import cv2
import numpy as np
import requests

class YoloDetector:
    def __init__(self, model_path, conf_threshold=0.5):
        self.net = cv2.dnn.readNet(model_path)
        self.conf_threshold = conf_threshold
        self.classes = ['weed', 'intruder']  # Example classes; adjust accordingly

    def process_image(self, image_url):
        # Download the image
        response = requests.get(image_url)
        image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
        return image

    def detect(self, image_url):
        image = self.process_image(image_url)
        height, width = image.shape[:2]

        # Prepare the image for detection
        blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        layer_names = self.net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        outputs = self.net.forward(output_layers)

        detections = []
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > self.conf_threshold:
                    detections.append((self.classes[class_id], confidence))

        return detections

    def count_detections(self, image_url):
        detections = self.detect(image_url)
        count = {cls: 0 for cls in self.classes}
        for detection in detections:
            count[detection[0]] += 1

        return count

# Example usage:
# detector = YoloDetector('yolov8.weights')
# counts = detector.count_detections('http://example.com/image.jpg')
# print(counts)