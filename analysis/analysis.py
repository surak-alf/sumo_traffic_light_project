# analysis/analyze.py
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pathlib import Path

# Configuration
OUTPUT_DIR = Path("output")
IMAGES_DIR = Path("images")
IMAGES_DIR.mkdir(exist_ok=True)

def parse_tripinfo(file_path):
    """Parse SUMO tripinfo XML file into a pandas DataFrame"""
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    data = []
    for trip in root.findall('tripinfo'):
        data.append({
            'id': trip.get('id'),
            'depart': float(trip.get('depart')),
            'arrival': float(trip.get('arrival')),
            'duration': float(trip.get('duration')),
            'waiting_time': float(trip.get('waitingTime', 0)),
            'route_length': float(trip.get('routeLength')),
            'speed': float(trip.get('routeLength')) / float(trip.get('duration')),
            'depart_lane': trip.get('departLane'),
            'arrival_lane': trip.get('arrivalLane')
        })
    
    return pd.DataFrame(data)

def plot_metrics(df, scenario_name):
    """Generate visualization plots for simulation metrics"""
    plt.figure(figsize=(18, 10))
    
    # Travel Time Distribution
    plt.subplot(2, 3, 1)
    sns.histplot(df['duration'], bins=30, kde=True)
    plt.title(f'Travel Time Distribution\n({scenario_name})')
    plt.xlabel('Time (seconds)')
    
    # Waiting Time Analysis
    plt.subplot(2, 3, 2)
    sns.boxplot(x=df['waiting_time'])
    plt.title('Waiting Time at Intersection')
    plt.xlabel('Seconds')
    
    # Speed Distribution
    plt.subplot(2, 3, 3)
    sns.histplot(df['speed'], bins=30, kde=True)
    plt.title('Vehicle Speed Distribution')
    plt.xlabel('Speed (m/s)')
    
    # Time Series Analysis
    plt.subplot(2, 3, 4)
    df['depart_hour'] = df['depart'] / 3600
    sns.scatterplot(data=df, x='depart_hour', y='duration', alpha=0.5)
    plt.title('Travel Time vs Departure Time')
    plt.xlabel('Departure Time (hours)')
    plt.ylabel('Travel Time (seconds)')
    
    # Route Efficiency
    plt.subplot(2, 3, 5)
    theoretical_time = df['route_length'] / 13.89  # 50 km/h in m/s
    efficiency = theoretical_time / df['duration']
    sns.histplot(efficiency, bins=30, kde=True)
    plt.title('Route Efficiency Ratio\n(theoretical_time / actual_time)')
    plt.xlabel('Efficiency')
    
    # Waiting vs Total Time
    plt.subplot(2, 3, 6)
    sns.scatterplot(data=df, x='duration', y='waiting_time', alpha=0.5)
    plt.title('Waiting Time vs Total Travel Time')
    plt.xlabel('Total Travel Time (s)')
    plt.ylabel('Waiting Time (s)')
    
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / f'metrics_{scenario_name.lower()}.png', dpi=300)
    plt.close()

def generate_comparison_report(scenarios):
    """Compare multiple simulation scenarios"""
    comparison_data = []
    
    for name, path in scenarios.items():
        df = parse_tripinfo(path)
        metrics = {
            'Scenario': name,
            'Avg Travel Time': df['duration'].mean(),
            'Median Travel Time': df['duration'].median(),
            'Avg Waiting Time': df['waiting_time'].mean(),
            'Max Waiting Time': df['waiting_time'].max(),
            'Avg Speed': df['speed'].mean(),
            'Vehicles per Hour': len(df) / (df['depart'].max() / 3600),
            'Route Efficiency': (df['route_length'] / 13.89 / df['duration']).mean()
        }
        comparison_data.append(metrics)
        
        # Generate individual plots
        plot_metrics(df, name)
    
    # Create comparison table
    comparison_df = pd.DataFrame(comparison_data)
    
    # Save comparison results
    comparison_df.to_csv(OUTPUT_DIR / 'comparison_results.csv', index=False)
    
    # Plot comparison metrics
    plt.figure(figsize=(12, 8))
    metrics_to_compare = ['Avg Travel Time', 'Avg Waiting Time', 'Route Efficiency']
    
    for i, metric in enumerate(metrics_to_compare, 1):
        plt.subplot(2, 2, i)
        sns.barplot(data=comparison_df, x='Scenario', y=metric)
        plt.title(metric)
        plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / 'scenario_comparison.png', dpi=300)
    plt.close()
    
    return comparison_df

if __name__ == "__main__":
    # Define your simulation scenarios
    scenarios = {
        "Base Case": OUTPUT_DIR / "tripinfo_base.xml",
        "Optimized Lights": OUTPUT_DIR / "tripinfo_optimized.xml",
        "No Traffic Lights": OUTPUT_DIR / "tripinfo_no_tls.xml"
    }
    
    # Generate comparison report
    report = generate_comparison_report(scenarios)
    
    # Print key findings
    print("\n=== Simulation Analysis Report ===")
    print(report[['Scenario', 'Avg Travel Time', 'Avg Waiting Time', 'Route Efficiency']])
    print(f"\nReports saved to {IMAGES_DIR} and {OUTPUT_DIR}")