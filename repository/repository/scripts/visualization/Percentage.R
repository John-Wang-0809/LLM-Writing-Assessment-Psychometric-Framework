# 加载必要的库
library(ggplot2)
library(dplyr)
library(extrafont)
library(gridExtra)

# 定义基础路径和文件名
base_path <- "repository/data/processed"
essay_sets <- c("Essay_Set_#1", "Essay_Set_#2", "Essay_Set_#3")
data_files <- paste0("rater_data_", 1:3, "_for_MFRM.csv")

# 定义颜色
plot_colors <- c("darkred", "darkblue", "darkgreen")

# 创建绘图函数
create_score_plot <- function(data, color, title) {
  # 计算频率百分比
  frequency_data <- data %>%
    group_by(Scores) %>%
    summarise(Frequency = n(), .groups = 'drop') %>%
    mutate(Frequency_Percentage = Frequency / sum(Frequency) * 100)
  
  # 创建图形
  plot <- ggplot(frequency_data, aes(x = factor(Scores), y = Frequency_Percentage)) +
    geom_bar(stat = "identity", fill = color) +
    labs(x = "Score", y = "Frequency Percentage (%)", title = title) +
    theme_minimal() +
    theme(
      plot.title = element_text(size = 18, family = "Arial", hjust = 0.5),
      strip.text.x = element_text(size = 16, family = "Arial"),
      strip.text.y = element_text(size = 16, family = "Arial"), 
      axis.title = element_text(size = 20, family = "Arial"),
      axis.text = element_text(size = 18, family = "Arial")
    )
  
  return(plot)
}

# 创建一个列表存储所有图形
plot_list <- list()

# 读取并处理每个数据集
for(i in 1:3) {
  file_path <- file.path(base_path, essay_sets[i], data_files[i])
  data <- read.csv(file_path, encoding = 'UTF-8')
  plot_list[[i]] <- create_score_plot(data, plot_colors[i], paste("Set #", i))
}

# 将所有图形组合在一起
combined_plot <- grid.arrange(grobs = plot_list, ncol = 3)
