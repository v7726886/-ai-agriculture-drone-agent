import requests
from PIL import Image
from io import BytesIO
from ultralytics import YOLO


class YOLOv8Detector:
    def __init__(self, model_path: str = "yolov8n.pt"):
        """Initialize YOLOv8 detector with specified model."""
        self.model = YOLO(model_path)

    def detect_from_url(self, image_url: str, confidence_threshold: float = 0.5):
        """
        Detect weeds and intruders in an image from URL.
        
        Args:
            image_url: URL of the image to analyze
            confidence_threshold: Minimum confidence score (0-1)
        
        Returns:
            dict: Contains weed_count, intruder_count, and confidence levels
        """
        try:
            # Fetch image from URL
            response = requests.get(image_url, timeout=10)
            img = Image.open(BytesIO(response.content))
            
            # Run inference
            results = self.model(img)
            
            weed_count = 0
            intruder_count = 0
            weed_confidences = []
            intruder_confidences = []
            
            # Parse results
            for result in results:
                for box in result.boxes:
                    label = self.model.model.names[int(box.cls)]
                    conf = float(box.conf)
                    
                    if conf >= confidence_threshold:
                        if label.lower() in ["weed", "weeds"]:
                            weed_count += 1
                            weed_confidences.append(conf)
                        elif label.lower() in ["intruder", "intruders"]:
                            intruder_count += 1
                            intruder_confidences.append(conf)
            
            return {
                "weed_count": weed_count,
                "weed_confidences": weed_confidences,
                "intruder_count": intruder_count,
                "intruder_confidences": intruder_confidences,
                "total_detections": weed_count + intruder_count,
                "status": "success"
            }
        except Exception as e:
            return {
                "error": str(e),
                "status": "failed"
            }

    def detect_from_file(self, file_path: str, confidence_threshold: float = 0.5):
        """
        Detect weeds and intruders in a local image file.
        
        Args:
            file_path: Path to the image file
            confidence_threshold: Minimum confidence score (0-1)
        
        Returns:
            dict: Contains detection results
        """
        try:
            img = Image.open(file_path)
            
            # Run inference
            results = self.model(img)
            
            weed_count = 0
            intruder_count = 0
            weed_confidences = []
            intruder_confidences = []
            
            # Parse results
            for result in results:
                for box in result.boxes:
                    label = self.model.model.names[int(box.cls)]
                    conf = float(box.conf)
                    
                    if conf >= confidence_threshold:
                        if label.lower() in ["weed", "weeds"]:
                            weed_count += 1
                            weed_confidences.append(conf)
                        elif label.lower() in ["intruder", "intruders"]:
                            intruder_count += 1
                            intruder_confidences.append(conf)
            
            return {
                "weed_count": weed_count,
                "weed_confidences": weed_confidences,
                "intruder_count": intruder_count,
                "intruder_confidences": intruder_confidences,
                "total_detections": weed_count + intruder_count,
                "status": "success"
            }
        except Exception as e:
            return {
                "error": str(e),
                "status": "failed"
            }