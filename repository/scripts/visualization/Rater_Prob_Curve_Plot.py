# 导入必要的库
import pandas as pd
import matplotlib.pyplot as plt
import os

# 配置参数
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

# 更新数据集配置
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
    加载并预处理指定数据集的数据
    
    Args:
        dataset_key: 数据集配置中的键名（如'set1', 'set2', 'set3'）
    """
    dataset = DATA_CONFIG['datasets'][dataset_key]
    file_path = os.path.join(DATA_CONFIG['base_path'], dataset['file'])
    
    # 根据文件扩展名选择读取方法
    if file_path.endswith('.csv'):
        df_rater = pd.read_csv(file_path)
    else:
        df_rater = pd.read_excel(file_path)
        
    # 添加前缀
    df_rater['Rater'] = df_rater['Rater'].apply(lambda x: f'{dataset["prefix"]} {x}')
    return df_rater

def setup_subplot(ax, rater, cfg):
    """设置子图的基本属性"""
    ax.set_title(rater, fontname=cfg['figure']['font_family'], 
                fontsize=cfg['figure']['subtitle_fontsize'])
    ax.set_xlabel(r'$\Theta$', fontname=cfg['figure']['font_family'], 
                 fontsize=cfg['figure']['label_fontsize'])
    ax.set_ylabel('Probability', fontname=cfg['figure']['font_family'], 
                 fontsize=cfg['figure']['label_fontsize'])
    ax.set_xlim(cfg['plot']['theta_range'])
    ax.set_ylim(cfg['plot']['prob_range'])
    ax.grid(True)
    
    # 设置刻度字体
    ax.tick_params(axis='both', labelsize=cfg['figure']['tick_fontsize'])
    for tick in ax.get_xticklabels() + ax.get_yticklabels():
        tick.set_fontname(cfg['figure']['font_family'])

def plot_rater_curves(df_rater, raters_subset, title_suffix, cfg, dataset):
    """绘制评分者概率曲线"""
    categories = dataset['categories']
    colors = dataset['colors']
    
    # 创建子图布局
    fig, axes = plt.subplots(1, len(raters_subset), figsize=cfg['figure']['subplot_figsize'])
    if len(raters_subset) == 1:
        axes = [axes]
        
    for idx, rater in enumerate(raters_subset):
        ax = axes[idx]
        df_filtered = df_rater[df_rater['Rater'] == rater]
        theta = df_filtered['Theta']
        
        # 绘制每个类别的概率曲线
        for i, category in enumerate(categories):
            ax.plot(theta, df_filtered[category],
                   label=f'Point.{i+1}',
                   color=colors[i],
                   linewidth=cfg['figure']['line_width'])
        
        setup_subplot(ax, rater, cfg)
    
    # 处理图例
    handles, labels = axes[0].get_legend_handles_labels()
    for ax in axes:
        ax.legend().remove()
    
    # 添加全局图例和标题
    fig.legend(handles, labels, loc='center right', 
              bbox_to_anchor=(0.95, 0.5), frameon=False,
              prop={'family': cfg['figure']['font_family'], 
                    'size': cfg['figure']['legend_fontsize']})
    
    fig.suptitle(f'Raters {title_suffix}', 
                fontname=cfg['figure']['font_family'], 
                fontsize=cfg['figure']['title_fontsize'])
    
    # 调整布局
    plt.tight_layout(rect=[0, 0, 0.85, 0.95], pad=4.0)
    plt.show()

def process_dataset(dataset_key):
    """处理单个数据集"""
    dataset = DATA_CONFIG['datasets'][dataset_key]
    df_rater = load_and_preprocess_data(dataset_key)
    
    # 获取所有评分者并分组
    raters = df_rater['Rater'].unique()
    num_raters = len(raters)
    mid_point = num_raters // 2
    raters_first_half = raters[:mid_point]
    raters_second_half = raters[mid_point:]
    
    # 绘制图表
    plot_rater_curves(df_rater, raters_first_half, f"{dataset_key}-1", CONFIG, dataset)
    plot_rater_curves(df_rater, raters_second_half, f"{dataset_key}-2", CONFIG, dataset)

def main():
    """主函数"""
    # 按数据集组处理
    dataset_groups = {
        'set1': ['set1'],
        'set2': ['set2'],
        'set3': ['set3_ic','set3_org','set3_v','set3_wc','set3_sf','set3_con']
    }
    
    # 选择要处理的数据集组
    group_to_process = 'set2'  # 可以改为 'set1' 或 'set2'
    
    print(f"Processing {group_to_process} datasets...")
    for dataset_key in dataset_groups[group_to_process]:
        print(f"\nProcessing dimension: {dataset_key}")
        process_dataset(dataset_key)
    
if __name__ == "__main__":
    main()