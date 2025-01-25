# 加载必要的库
library(readxl)
library(ggplot2)
library(dplyr)
library(tidyr)
library(extrafont)

# 设置基础路径
BASE_PATH <- "repository/data/visualization"

# 定义通用的颜色和标签
RATER_COLORS <- c(
  "HR-1"      = '#E64B35',
  "HR-2"      = '#F39B7F', 
  "4o-Mini"   = '#00A087',
  "GPT-4o"    = '#4DBBD5',
  "CL-3.5-H"  = '#3C5488',
  "CL-3.5-S"  = '#FF1493'
)

RATER_LABELS <- c("HR-1", "HR-2", "4o-Mini", "GPT-4o", "CL-3.5-H", "CL-3.5-S")

# 通用绘图主题
common_theme <- theme_minimal() +
  theme(
    plot.title = element_blank(),
    axis.title.y = element_text(size = 24, family = "Arial"),
    axis.title.x = element_text(size = 24, family = "Arial"),
    axis.text.x = element_text(size = 24, family = "Arial"),
    axis.text.y = element_text(size = 24, family = "Arial"),
    legend.title = element_text(size = 24, family = "Arial"),
    legend.text = element_text(size = 20, family = "Arial")
  )

# 绘制Essay Set #1的ICC曲线
plot_essay_set_1 <- function() {
  data <- read.csv(file.path(BASE_PATH, "Set_#1_Expected_ICC_plot.csv"))
  colnames(data) <- c("Rater", "Theta", "Score", "Expected_Zones", "Half_Threshold")
  data$Rater <- factor(data$Rater, levels = RATER_LABELS)
  
  p <- ggplot(data, aes(x = Theta, y = Score, color = Rater, group = Rater)) +
    geom_line(size = 0.75) +
    labs(x = "Measure relative to item difficulty", y = "Score on Item") +
    geom_hline(yintercept = c(0.5, 1.5, 2.5, 3.5, 4.5, 5.5), linetype = "dashed", color = "grey", size = 1) +
    common_theme +
    coord_cartesian(xlim = c(-25, 25), ylim = c(1, 6)) +
    scale_y_continuous(breaks = 1:6) +
    scale_color_manual(values = RATER_COLORS, labels = RATER_LABELS) +
    guides(color = guide_legend(title = "Rater"))
  
  print(p)
}

# 绘制Essay Set #2的ICC曲线
plot_essay_set_2 <- function() {
  data <- read.csv(file.path(BASE_PATH, "Set_#2_Expected_ICC_plot.csv"))
  colnames(data) <- c("Rater", "Theta", "Score", "Expected_Zones", "Half_Threshold")
  data$Rater <- factor(data$Rater, levels = RATER_LABELS)
  
  p <- ggplot(data, aes(x = Theta, y = Score, color = Rater, group = Rater)) +
    geom_line(size = 0.75) +
    labs(x = "Measure relative to item difficulty", y = "Score on Item") +
    geom_hline(yintercept = c(0.5, 1.5, 2.5, 3.5), linetype = "dashed", color = "grey", size = 1) +
    common_theme +
    coord_cartesian(xlim = c(-25, 25), ylim = c(0, 4)) +
    scale_y_continuous(breaks = 0:4) +
    scale_color_manual(values = RATER_COLORS, labels = RATER_LABELS) +
    guides(color = guide_legend(title = "Rater"))
  
  print(p)
}

# 绘制Essay Set #3的ICC曲线
plot_essay_set_3 <- function() {
  sheet_names <- c("I&C", "Org", "V", "WC", "SF", "Con")
  data_list <- lapply(sheet_names, function(sheet) {
    data <- read_excel(
      file.path(BASE_PATH, "Set_#3_Expected_ICC_plot.xlsx"), 
      sheet = sheet,
      col_names = TRUE
    )
    
    
    data$Sheet <- sheet
    # 检查并设置列名
    if (ncol(data) >= 5) {
      colnames(data)[1:5] <- c("Rater", "Theta", "Score", "Expected_Zones", "Half_Threshold")
    }
    
    # 数据类型转换
    data$Rater <- factor(data$Rater, levels = c("HR-1", "HR-2", "4o-Mini", "GPT-4o", "CL-3.5-H", "CL-3.5-S"))
    data$Theta <- as.numeric(data$Theta)
    data$Score <- as.numeric(data$Score)
    data$Expected_Zones <- as.numeric(data$Expected_Zones)
    data$Half_Threshold <- as.numeric(data$Half_Threshold)
    
    return(data)
  })
  
  combined_data <- bind_rows(data_list)
  combined_data$Sheet <- factor(combined_data$Sheet, levels = sheet_names)
  
  # 绘图
  p <- ggplot(combined_data, aes(x = Theta, y = Score, color = Rater, group = Rater)) +
    geom_line(size = 0.75) +
    labs(x = "Measure relative to item difficulty", y = "Score on Item") +
    geom_hline(yintercept = c(1.5, 2.5, 3.5, 4.5, 5.5), 
               linetype = "dashed", 
               color = "grey", 
               size = 0.5) +
    common_theme +
    theme(
      strip.text.x = element_text(size = 16, family = "Arial"),
      strip.text.y = element_text(size = 16, family = "Arial")
    ) +
    coord_cartesian(xlim = c(-12, 12), ylim = c(1, 6)) +
    scale_color_manual(values = RATER_COLORS) +
    guides(color = guide_legend(title = "Rater")) +
    facet_grid(rows = vars(Sheet), scales = "free_y", switch = "y")
  
  print(p)
}

# 执行绘图
plot_essay_set_1()
plot_essay_set_2()
plot_essay_set_3()