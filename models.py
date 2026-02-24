from pydantic import BaseModel


class SensorData(BaseModel):
    temperature: float
    humidity: float
    pressure: float
    light_intensity: float
    battery_level: float


class DroneStatus(BaseModel):
    is_flying: bool
    current_location: str
    battery_status: float
    signal_strength: float


class Mission(BaseModel):
    mission_id: str
    start_time: str  # ISO 8601 format
    end_time: str  # ISO 8601 format
    status: str  # e.g. 'pending', 'in_progress', 'completed'
    destination: str


class DetectionResponse(BaseModel):
    detected_objects: list[str]
    confidence_scores: list[float]
    timestamp: str  # ISO 8601 format
