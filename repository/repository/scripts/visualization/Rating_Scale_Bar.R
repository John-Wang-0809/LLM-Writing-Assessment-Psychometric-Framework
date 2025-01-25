# 加载必要的库
library(ggplot2)
library(tidyr)
library(dplyr)
library(ggsci)
library(readxl)
library(extrafont)

# 加载字体和设置基础路径
loadfonts(device = "win")
BASE_PATH <- "repository/data/visualization"

# 定义常量
RATER_LEVELS <- c("HR-1", "HR-2", "4o-Mini", "GPT-4o", "CL-3.5-H", "CL-3.5-S")
LABEL_LEVELS <- c("Extreme", "Overfit", "Normal", "Underfit")
COLOR_LEVELS <- c("black", "navy", "darkgreen", "darkred")

# 通用绘图主题和参数
common_theme <- theme_minimal() +
  theme(
    strip.text = element_text(size = 20, family = "Arial"),
    axis.text = element_text(size = 22, family = "Arial"), 
    axis.title = element_text(size = 24, family = "Arial"),
    legend.text = element_text(size = 20, family = "Arial"),
    legend.title = element_blank(),
    legend.position = "right",
    panel.spacing = unit(1, "lines")
  )

plot_params <- list(
  scale_fill_manual(values = setNames(COLOR_LEVELS, LABEL_LEVELS)),
  labs(x = "Category", y = "Category Percent %"),
  scale_y_continuous(limits = c(0, 85), breaks = seq(0, 100, by = 20)),
  common_theme
)

# 数据处理函数
process_data <- function(data) {
  data %>%
    mutate(
      color = case_when(
        Category_Outfit < 0.84 ~ "navy",
        Category_Outfit > 998 ~ "black",
        Category_Outfit > 1.16 ~ "darkred",
        TRUE ~ "darkgreen"
      ),
      label = case_when(
        Category_Outfit < 0.84 ~ "Overfit",
        Category_Outfit > 998 ~ "Extreme",
        Category_Outfit > 1.16 ~ "Underfit",
        TRUE ~ "Normal"
      ),
      label = factor(label, levels = LABEL_LEVELS),
      color = factor(color, levels = COLOR_LEVELS),
      Rater = factor(Rater, levels = RATER_LEVELS)
    )
}

# 绘图函数
plot_rater_groups <- function(data, title = NULL) {
  # 前三位评分者
  p1 <- data %>%
    filter(Rater %in% RATER_LEVELS[1:3]) %>%
    ggplot(aes(x = factor(Category), y = Category_Percent, fill = label)) +
    geom_bar(stat = "identity") +
    facet_wrap(~Rater, scales = "free_y") +
    plot_params +
    if(!is.null(title)) ggtitle(title)
  
  # 后三位评分者  
  p2 <- data %>%
    filter(Rater %in% RATER_LEVELS[4:6]) %>%
    ggplot(aes(x = factor(Category), y = Category_Percent, fill = label)) +
    geom_bar(stat = "identity") +
    facet_wrap(~Rater, scales = "free_y") +
    plot_params +
    if(!is.null(title)) ggtitle(title)
    
  print(p1)
  print(p2)
}

# 主要绘图函数
plot_essay_set <- function(set_num, dimensions = NULL) {
  if(is.null(dimensions)) {
    data <- read.csv(file.path(BASE_PATH, sprintf("Set_#%d_Category_Percent.csv", set_num)))
    plot_rater_groups(process_data(data))
  } else {
    for(dim in dimensions) {
      data <- read.csv(file.path(BASE_PATH, sprintf("Set_#%d_Category_Percent_%s.csv", set_num, dim)))
      plot_rater_groups(process_data(data), dim)
    }
  }
}

# 执行绘图
plot_essay_set(1)
plot_essay_set(2)
plot_essay_set(3, dimensions = c("I&C", "Org", "V", "WC", "SF", "Con"))
