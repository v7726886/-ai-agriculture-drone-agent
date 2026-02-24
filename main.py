from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import supabase

app = FastAPI()

# Supabase client initialization (replace with your url and key)
SUPABASE_URL = "https://your-supabase-url.supabase.co"
SUPABASE_KEY = "your-supabase-key"
client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

# Pydantic model for the drone data
class DroneData(BaseModel):
    mission_id: str
    altitude: float
    latitude: float
    longitude: float
    command_goal: str

@app.post("/analyze-drone-data")
async def analyze_drone_data(data: DroneData):
    # Implement goal-based logic for drone commands
    if data.command_goal == "land":
        # Logic for landing the drone
        command_response = "Drone is landing..."
    elif data.command_goal == "hover":
        # Logic for hovering
        command_response = "Drone is hovering..."
    else:
        raise HTTPException(status_code=400, detail="Invalid command goal")

    # Save mission data to Supabase
    mission_data = {
        "mission_id": data.mission_id,
        "altitude": data.altitude,
        "latitude": data.latitude,
        "longitude": data.longitude,
        "command_goal": data.command_goal
    }
    response = client.from_('missions').insert(mission_data).execute()

    return {"status": "success", "message": command_response, "supabase_response": response}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)