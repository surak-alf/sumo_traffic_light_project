import pandas as pd

def calculate_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate derived metrics"""
    df = df.copy()
    
    # Basic metrics
    df['theoretical_time'] = df['route_length'] / 13.89  # 50 km/h in m/s
    df['efficiency'] = df['theoretical_time'] / df['duration']
    
    # Time-based features
    df['hour'] = df['depart'] // 3600
    df['minute'] = (df['depart'] % 3600) // 60
    
    return df