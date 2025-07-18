from pathlib import Path
import xml.etree.ElementTree as ET
import pandas as pd

def load_tripinfo_data(file_path: Path) -> pd.DataFrame:
    """Load SUMO tripinfo XML file into DataFrame"""
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    data = []
    for trip in root.findall('tripinfo'):
        record = {
            'id': trip.get('id'),
            'depart': float(trip.get('depart')),
            'arrival': float(trip.get('arrival')),
            'duration': float(trip.get('duration')),
            'waiting_time': float(trip.get('waitingTime', 0)),
            'route_length': float(trip.get('routeLength')),
            'speed': float(trip.get('routeLength')) / float(trip.get('duration')),
            'depart_lane': trip.get('departLane'),
            'arrival_lane': trip.get('arrivalLane')
        }
        data.append(record)
    
    return pd.DataFrame(data)