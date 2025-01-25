# 1. 整理库的导入
library(ggplot2)
library(dplyr)
library(extrafont)
library(patchwork)

# 加载字体
loadfonts(device = "win")

# 2. 数据准备和处理函数
process_dataset <- function(set_number) {
  # 构建文件路径
  file_path <- sprintf("repository/data/visualization/Set_#%d_D_Study_Results.csv", set_number)
  
  # 读取数据
  data <- read.csv(file_path)
  rater_order <- c("HR", "GPT", "Claude")
  data$Rater_Type <- factor(data$Rater_Type, levels = rater_order)
  
  return(data)
}

# 3. 通用主题设置
create_common_theme <- function() {
  theme_minimal() +
    theme(
      plot.title = element_blank(),
      axis.title.y = element_text(size = 24, family = "Arial"),
      axis.title.x = element_text(size = 24, family = "Arial"),
      axis.text.x = element_text(size = 22, family = "Arial"),
      axis.text.y = element_text(size = 22, family = "Arial"),
      legend.title = element_blank(),
      legend.text = element_text(size = 20, family = "Arial"),
      legend.box = "vertical"
    )
}

# 4. 通用图形设置
common_plot_settings <- list(
  scale_color_manual(
    values = c('#E64B35', '#008000', '#3C5488'),
    labels = c("HR", "GPT", "Claude")
  ),
  scale_y_continuous(limits = c(0.5, 1), breaks = seq(0.5, 1, by = 0.1)),
  scale_x_continuous(breaks = seq(2, 12, by = 2))
)

# 1. 整理库的导入
library(ggplot2)
library(dplyr)
library(extrafont)
library(patchwork)

# 加载字体
loadfonts(device = "win")

# 2. 数据准备和处理函数
process_dataset <- function(set_number) {
  # 构建文件路径
  file_path <- sprintf("repository/data/visualization/Set_#%d_D_Study_Results.csv", set_number)
  
  # 读取数据
  data <- read.csv(file_path)
  rater_order <- c("HR", "GPT", "Claude")
  data$Rater_Type <- factor(data$Rater_Type, levels = rater_order)
  
  return(data)
}

# 3. 通用主题设置
create_common_theme <- function() {
  theme_minimal() +
    theme(
      plot.title = element_blank(),
      axis.title.y = element_text(size = 26, family = "Arial"),
      axis.title.x = element_text(size = 26, family = "Arial"),
      axis.text.x = element_text(size = 24, family = "Arial"),
      axis.text.y = element_text(size = 24, family = "Arial"),
      legend.title = element_blank(),
      legend.text = element_text(size = 20, family = "Arial"),
      legend.box = "vertical"
    )
}

# 4. 通用图形设置
common_plot_settings <- list(
  scale_color_manual(
    values = c('#E64B35', '#008000', '#3C5488'),
    labels = c("HR", "GPT", "Claude")
  ),
  scale_y_continuous(limits = c(0.5, 1), breaks = seq(0.5, 1, by = 0.1)),
  scale_x_continuous(breaks = seq(2, 12, by = 2))
)

# 5. 创建G系数图
create_g_coefficient_plot <- function(data, set_number) {
  ggplot(data, aes(x = Rater_Numbers, y = G.Coefficient, color = factor(Rater_Type), group = Rater_Type)) +
    geom_line() +
    geom_point() +
    labs(
      x = "Rater Numbers", 
      y = "G Coefficient"
    ) +
    geom_hline(yintercept = 0.8, linetype = "dashed", color = "grey", linewidth = 0.8) +
    create_common_theme() +
    common_plot_settings +
    theme(legend.position = "right")
}

# 6. 创建Phi系数图
create_phi_coefficient_plot <- function(data, set_number) {
  ggplot(data, aes(x = Rater_Numbers, y = Phi.Coefficient, color = factor(Rater_Type), group = Rater_Type)) +
    geom_line() +
    geom_point() +
    labs(
      x = "Rater Numbers", 
      y = expression(paste(phi, " Coefficient"))
    ) +
    geom_hline(yintercept = 0.8, linetype = "dashed", color = "grey", linewidth = 0.8) +
    create_common_theme() +
    common_plot_settings +
    theme(legend.position = "none")
}

# 7. 处理所有数据集并生成图形
# 创建空列表存储所有图形
plot_list <- list()

# 处理每个数据集
for(set_number in 1:3) {
  # 读取数据
  data <- process_dataset(set_number)
  
  # 创建单独的图形
  g_plot <- create_g_coefficient_plot(data, set_number)
  phi_plot <- create_phi_coefficient_plot(data, set_number)
  
  # 使用 plot_layout 来控制图例位置
  combined <- g_plot / phi_plot + 
    plot_layout(guides = "collect") +  # 收集并统一图例
    plot_annotation(theme = theme(legend.position = "right"))  # 将图例放在右侧居中
    
  plot_list[[set_number]] <- combined
}

# 8. 展示所有图形
# 水平排列所有数据集的图形
print(plot_list[[1]])
print(plot_list[[2]])
print(plot_list[[3]])


# 7. 处理所有数据集并生成图形
# 创建空列表存储所有图形
plot_list <- list()

# 处理每个数据集
for(set_number in 1:3) {
  # 读取数据
  data <- process_dataset(set_number)
  
  # 创建单独的图形
  g_plot <- create_g_coefficient_plot(data, set_number)
  phi_plot <- create_phi_coefficient_plot(data, set_number)
  
  # 使用 plot_layout 来控制图例位置
  combined <- g_plot / phi_plot + 
    plot_layout(guides = "collect") +  # 收集并统一图例
    plot_annotation(theme = theme(legend.position = "right"))  # 将图例放在右侧居中
    
  plot_list[[set_number]] <- combined
}

# 8. 展示所有图形
# 水平排列所有数据集的图形
print(plot_list[[1]])
print(plot_list[[2]])
print(plot_list[[3]])
