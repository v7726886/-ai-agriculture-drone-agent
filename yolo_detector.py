import cv2
import torch

class YoloDetector:
    def __init__(self, model_path):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)

    def detect(self, image_path):
        img = cv2.imread(image_path)
        results = self.model(img)
        results.show()  # or results.save() to save outputs
        return results

if __name__ == '__main__':
    detector = YoloDetector('yolov8_weights.pt')  # Update with your YOLOv8 weights
    results = detector.detect('path_to_image.jpg')  # Update with the path to your image