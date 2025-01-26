import numpy as np
import pandas as pd

def process_information_data(file_path):
    # 读取数据
    rater_info_data = pd.read_csv(file_path, encoding='UTF-8')
    
    # 重新排序数据
    desired_order = ["HR-1", "HR-2", "4o-Mini", "GPT-4o", "CL-3.5-H", "CL-3.5-S"]
    rater_info_data["Rater"] = pd.Categorical(
        rater_info_data["Rater"],
        categories=desired_order,
        ordered=True
    )
    
    # 分组数据
    grouped_data = rater_info_data.groupby('Rater')
    
    # 创建结果字典
    results = {
        'Rater': [],
        'AUC': [],
        'Effective_AUC': [],
        'Peak_Theta': [],
        'Peak_Info': [],
        'CV': [],
        'PCC with HR-1': []  # 新增列
    }
    
    # 计算各项指标
    for rater, group in grouped_data:
        theta = group['Theta']
        info_data = group['info_data_rater']
        
        # 计算AUC
        auc = np.trapz(info_data, theta)
        
        # 计算有效AUC
        filtered_group = group[group['info_data_rater'] >= 0.25]
        if len(filtered_group) > 1:
            theta_filtered = filtered_group['Theta']
            info_data_filtered = filtered_group['info_data_rater'] - 0.25
            effective_auc = np.trapz(info_data_filtered, theta_filtered)
        else:
            effective_auc = 0
        
        # 计算峰值
        max_index = group['info_data_rater'].idxmax()
        peak_theta = group.loc[max_index, 'Theta']
        peak_info = group.loc[max_index, 'info_data_rater']
        
        # 计算CV
        mean_value = info_data.mean()
        std_dev = info_data.std()
        cv = std_dev / mean_value if mean_value != 0 else np.nan
        
        # 存储结果
        results['Rater'].append(rater)
        results['AUC'].append(round(auc, 2))
        results['Effective_AUC'].append(round(effective_auc, 2))
        results['Peak_Theta'].append(round(peak_theta, 2))
        results['Peak_Info'].append(round(peak_info, 2))
        results['CV'].append(round(cv, 4))
        
        # 计算与HR-1的相关系数
        if rater == 'HR-1':
            correlation = 1
        else:
            hr1_group = grouped_data.get_group('HR-1')
            # 计算相关系数
            correlation = np.corrcoef(hr1_group['info_data_rater'], group['info_data_rater'])[0, 1]
        
        results['PCC with HR-1'].append(round(correlation, 4))
    
    return pd.DataFrame(results)

# 处理三个数据集
file_paths = [
    "repository/data/visualization/Set_#1_Information.csv",
    "repository/data/visualization/Set_#2_Information.csv",
    "repository/data/visualization/Set_#3_Information.csv"
]

# 处理并保存结果
for i, file_path in enumerate(file_paths, 1):
    results_df = process_information_data(file_path)
    
    # 保存指标结果
    results_df.to_csv(file_path.replace('.csv', '_Metrics.csv'), index=False)
    
    # 打印结果
    print(f"\nEssay Set #{i} Results:")
    print(results_df)
