# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# Configuration parameters
CONFIG = {
    'figure': {
        'subplot_figsize': (24, 6),
        'line_width': 2.5,
        'font_family': 'Arial',
        'title_fontsize': 28,
        'subtitle_fontsize': 24,
        'label_fontsize': 20,
        'tick_fontsize': 18,
        'legend_fontsize': 20
    },
    'plot': {
        'theta_range': (-15, 15),
        'prob_range': (0, 1)
    }
}

# Update dataset configurations
DATA_CONFIG = {
    'base_path': r"repository\data\visualization",
    'datasets': {
        'set1': {
            'file': 'Set_#1_Category_Prob.xlsx',
            'prefix': 'Set #1',
            'categories': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
            'colors': ['#E64B35', '#F39B7F', '#00A087', '#4DBBD5', '#3C5488', '#FF1493']
        },
        'set2': {
            'file': 'Set_#2_Category_Prob.xlsx',
            'prefix': 'Set #2',
            'categories': ['C0', 'C1', 'C2', 'C3', 'C4'],
            'colors': ['#E64B35', '#F39B7F', '#00A087', '#4DBBD5', '#3C5488']
        },
        'set3_con': {
            'file': 'Set_#3_Category_Prob_Con.xlsx',
            'prefix': 'Set #3 Con',
            'categories': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
            'colors': ['#E64B35', '#F39B7F', '#00A087', '#4DBBD5', '#3C5488', '#FF1493']
        },
        'set3_ic': {
            'file': 'Set_#3_Category_Prob_I&C.xlsx',
            'prefix': 'Set #3 I&C',
            'categories': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
            'colors': ['#E64B35', '#F39B7F', '#00A087', '#4DBBD5', '#3C5488', '#FF1493']
        },
        'set3_org': {
            'file': 'Set_#3_Category_Prob_Org.xlsx',
            'prefix': 'Set #3 Org',
            'categories': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
            'colors': ['#E64B35', '#F39B7F', '#00A087', '#4DBBD5', '#3C5488', '#FF1493']
        },
        'set3_sf': {
            'file': 'Set_#3_Category_Prob_SF.xlsx',
            'prefix': 'Set #3 SF',
            'categories': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
            'colors': ['#E64B35', '#F39B7F', '#00A087', '#4DBBD5', '#3C5488', '#FF1493']
        },
        'set3_v': {
            'file': 'Set_#3_Category_Prob_V.xlsx',
            'prefix': 'Set #3 V',
            'categories': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
            'colors': ['#E64B35', '#F39B7F', '#00A087', '#4DBBD5', '#3C5488', '#FF1493']
        },
        'set3_wc': {
            'file': 'Set_#3_Category_Prob_WC.xlsx',
            'prefix': 'Set #3 WC',
            'categories': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
            'colors': ['#E64B35', '#F39B7F', '#00A087', '#4DBBD5', '#3C5488', '#FF1493']
        }
    }
}

def load_and_preprocess_data(dataset_key):
    """
    Load and preprocess data for the specified dataset
    
    Args:
        dataset_key: Key name in dataset configuration (e.g., 'set1', 'set2', 'set3')
    """
    dataset = DATA_CONFIG['datasets'][dataset_key]
    file_path = os.path.join(DATA_CONFIG['base_path'], dataset['file'])
    
    # Choose reading method based on file extension
    if file_path.endswith('.csv'):
        df_rater = pd.read_csv(file_path)
    else:
        df_rater = pd.read_excel(file_path)
        
    # Add prefix
    df_rater['Rater'] = df_rater['Rater'].apply(lambda x: f'{dataset["prefix"]} {x}')
    return df_rater

def setup_subplot(ax, rater, cfg):
    """Set basic properties for subplot"""
    ax.set_title(rater, fontname=cfg['figure']['font_family'], 
                fontsize=cfg['figure']['subtitle_fontsize'])
    ax.set_xlabel(r'$\Theta$', fontname=cfg['figure']['font_family'], 
                 fontsize=cfg['figure']['label_fontsize'])
    ax.set_ylabel('Probability', fontname=cfg['figure']['font_family'], 
                 fontsize=cfg['figure']['label_fontsize'])
    ax.set_xlim(cfg['plot']['theta_range'])
    ax.set_ylim(cfg['plot']['prob_range'])
    ax.grid(True)
    
    # Set tick font
    ax.tick_params(axis='both', labelsize=cfg['figure']['tick_fontsize'])
    for tick in ax.get_xticklabels() + ax.get_yticklabels():
        tick.set_fontname(cfg['figure']['font_family'])

def plot_rater_curves(df_rater, raters_subset, title_suffix, cfg, dataset):
    """Plot probability curves for raters"""
    categories = dataset['categories']
    colors = dataset['colors']
    
    # Create subplot layout
    fig, axes = plt.subplots(1, len(raters_subset), figsize=cfg['figure']['subplot_figsize'])
    if len(raters_subset) == 1:
        axes = [axes]
        
    for idx, rater in enumerate(raters_subset):
        ax = axes[idx]
        df_filtered = df_rater[df_rater['Rater'] == rater]
        theta = df_filtered['Theta']
        
        # Plot probability curves for each category
        for i, category in enumerate(categories):
            ax.plot(theta, df_filtered[category],
                   label=f'Point.{i+1}',
                   color=colors[i],
                   linewidth=cfg['figure']['line_width'])
        
        setup_subplot(ax, rater, cfg)
    
    # Handle legend
    handles, labels = axes[0].get_legend_handles_labels()
    for ax in axes:
        ax.legend().remove()
    
    # Add global legend and title
    fig.legend(handles, labels, loc='center right', 
              bbox_to_anchor=(0.95, 0.5), frameon=False,
              prop={'family': cfg['figure']['font_family'], 
                    'size': cfg['figure']['legend_fontsize']})
    
    fig.suptitle(f'Raters {title_suffix}', 
                fontname=cfg['figure']['font_family'], 
                fontsize=cfg['figure']['title_fontsize'])
    
    # Adjust layout
    plt.tight_layout(rect=[0, 0, 0.85, 0.95], pad=4.0)
    plt.show()

def process_dataset(dataset_key):
    """Process a single dataset"""
    dataset = DATA_CONFIG['datasets'][dataset_key]
    df_rater = load_and_preprocess_data(dataset_key)
    
    # Get all raters and group them
    raters = df_rater['Rater'].unique()
    num_raters = len(raters)
    mid_point = num_raters // 2
    raters_first_half = raters[:mid_point]
    raters_second_half = raters[mid_point:]
    
    # Plot charts
    plot_rater_curves(df_rater, raters_first_half, f"{dataset_key}-1", CONFIG, dataset)
    plot_rater_curves(df_rater, raters_second_half, f"{dataset_key}-2", CONFIG, dataset)

def main():
    """Main function"""
    # Process by dataset groups
    dataset_groups = {
        'set1': ['set1'],
        'set2': ['set2'],
        'set3': ['set3_ic','set3_org','set3_v','set3_wc','set3_sf','set3_con']
    }
    
    # Choose dataset group to process
    group_to_process = 'set2'  # Can be changed to 'set1' or 'set2'
    
    print(f"Processing {group_to_process} datasets...")
    for dataset_key in dataset_groups[group_to_process]:
        print(f"\nProcessing dimension: {dataset_key}")
        process_dataset(dataset_key)
    
if __name__ == "__main__":
    main()