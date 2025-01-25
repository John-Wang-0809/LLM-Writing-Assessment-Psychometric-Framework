# 1. 加载必要的库
library(ggplot2)
library(dplyr)
library(extrafont)
library(patchwork)

# 加载字体
loadfonts(device = "win")

# 2. 数据处理和绘图函数
process_and_plot <- function(set_number) {
  # 构建文件路径
  file_path <- sprintf("repository/data/visualization/Set_#%d_Information.csv", set_number)
  
  data <- read.csv(file_path)
  
  # 将Rater列重新因子化
  data$Rater <- factor(data$Rater, 
                       levels = c("HR-1", "HR-2", "4o-Mini", "GPT-4o", "CL-3.5-H", "CL-3.5-S"))
  
  # 对于第三个数据集，处理Trait列
  if(set_number == 3) {
    data$Trait <- factor(data$Trait, 
                         levels = c("I&C", "Org", "V", "WC", "SF", "Con"))
  }
  
  # 绘图
  colors <- c('#E64B35', '#F39B7F', '#00A087', '#4DBBD5', '#3C5488', '#FF1493')
  new_Rater_labels <- c("HR-1", "HR-2", "4o-Mini", "GPT-4o", "CL-3.5-H", "CL-3.5-S")
  
  p <- ggplot(data, aes(x = Theta, y = info_data_rater, color = Rater)) +
    geom_line(size = 1.5) +
    scale_color_manual(values = colors, labels = new_Rater_labels, drop = FALSE) +
    labs(x = expression(theta), y = "Information") +
    geom_hline(yintercept = 0.25, linetype = "dashed", color = "grey", size = 1) +
    theme_minimal() +
    xlim(-20, 20) + 
    scale_y_continuous(limits = c(0, 0.75), breaks = seq(0, 0.75, by = 0.25))
  
  # 根据数据集编号调整图形布局和样式
  if(set_number == 3) {
    p <- p +
      facet_wrap(~ Trait, ncol = 2) +
      theme(
        strip.text = element_text(size = 20, family = "Arial"),
        axis.title.y = element_text(size = 24, family = "Arial"),
        axis.title.x = element_text(size = 24, family = "Arial"),
        axis.text.x = element_text(size = 24, family = "Arial"),
        axis.text.y = element_text(size = 24, family = "Arial"),
        legend.title = element_blank(),
        legend.text = element_text(size = 20, family = "Arial"),
        legend.position = "right"
      )
  } else {
    p <- p +
      theme(
        axis.title.y = element_text(size = 24, family = "Arial"),
        axis.title.x = element_text(size = 24, family = "Arial"),
        axis.text.x = element_text(size = 24, family = "Arial"),
        axis.text.y = element_text(size = 24, family = "Arial"),
        legend.title = element_blank(),
        legend.text = element_text(size = 20, family = "Arial"),
        legend.position = "right"
      )
  }
  
  return(p)
}

# 3. 处理并绘制所有数据集
plots <- lapply(1:3, process_and_plot)

# 4. 组合并显示图形
combined_12 <- plots[[1]] / plots[[2]]

# 显示图形
print(combined_12)
print(plots[[3]])


