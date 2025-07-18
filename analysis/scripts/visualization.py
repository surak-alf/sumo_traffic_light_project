import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def plot_metrics(df, scenario_name: str, output_dir: Path):
    """Generate visualization plots for simulation metrics"""
    plt.figure(figsize=(18, 10))
    
    plots = [
        ('duration', 'Travel Time Distribution', 'Time (seconds)'),
        ('waiting_time', 'Waiting Time at Intersection', 'Seconds'),
        ('speed', 'Vehicle Speed Distribution', 'Speed (m/s)')
    ]
    
    for i, (col, title, xlabel) in enumerate(plots, 1):
        plt.subplot(2, 3, i)
        sns.histplot(df[col], bins=30, kde=True)
        plt.title(f'{title}\n({scenario_name})')
        plt.xlabel(xlabel)
    
    # Time Series Analysis
    plt.subplot(2, 3, 4)
    df['depart_hour'] = df['depart'] / 3600
    sns.scatterplot(data=df, x='depart_hour', y='duration', alpha=0.5)
    plt.title('Travel Time vs Departure Time')
    
    # Save figure
    plt.tight_layout()
    plt.savefig(output_dir / f'metrics_{scenario_name.lower()}.png', dpi=300)
    plt.close()

def compare_scenarios(scenario_dfs: dict, output_dir: Path):
    """Generate comparison visualizations"""
    comparison = pd.concat([
        df.assign(scenario=name) 
        for name, df in scenario_dfs.items()
    ])
    
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=comparison, x='scenario', y='duration')
    plt.title('Travel Time Comparison Across Scenarios')
    plt.savefig(output_dir / 'scenario_comparison.png')
    
    return comparison.groupby('scenario').mean()