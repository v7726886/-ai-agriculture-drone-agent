import os
import supabase

class SupabaseHelper:
    def __init__(self):
        self.client = supabase.create_client(
            os.environ['SUPABASE_URL'],
            os.environ['SUPABASE_KEY']
        )

    def upsert_drone_telemetry(self, telemetry_data):
        """Upserts telemetry data into the drone_status table."""
        response = self.client.table('drone_status').upsert(telemetry_data).execute()
        return response

    def upsert_mission_data(self, mission_data):
        """Upserts mission data into the missions table."""
        response = self.client.table('missions').upsert(mission_data).execute()
        return response
