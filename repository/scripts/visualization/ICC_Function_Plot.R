# Load required libraries
library(readxl)
library(ggplot2)
library(dplyr)
library(tidyr)
library(extrafont)

# Main analysis function
run_icc_analysis <- function(data_path = "repository/data/visualization") {
  # Set base path
  base_path <- data_path
  
  # Define visual constants
  rater_colors <- c(
    "HR-1"      = '#E64B35',
    "HR-2"      = '#F39B7F', 
    "4o-Mini"   = '#00A087',
    "GPT-4o"    = '#4DBBD5',
    "CL-3.5-H"  = '#3C5488',
    "CL-3.5-S"  = '#FF1493'
  )
  
  rater_labels <- c("HR-1", "HR-2", "4o-Mini", "GPT-4o", "CL-3.5-H", "CL-3.5-S")
  
  # Create common theme
  common_theme <- theme_minimal() +
    theme(
      plot.title = element_blank(),
      axis.title = element_text(size = 24, family = "Arial"),
      axis.text = element_text(size = 24, family = "Arial"),
      legend.title = element_text(size = 24, family = "Arial"),
      legend.text = element_text(size = 20, family = "Arial")
    )
  
  # Plot ICC for Essay Set 1
  plot_set1 <- function() {
    data_file <- file.path(base_path, "Set_#1_Expected_ICC_plot.csv")
    if (!file.exists(data_file)) stop("Set 1 data not found: ", data_file)
    
    data <- read.csv(data_file) %>% 
      setNames(c("Rater", "Theta", "Score", "Expected_Zones", "Half_Threshold")) %>%
      mutate(Rater = factor(Rater, levels = rater_labels))
    
    ggplot(data, aes(x = Theta, y = Score, color = Rater, group = Rater)) +
      geom_line(linewidth = 0.75) +
      labs(x = "Measure relative to item difficulty", y = "Score on Item") +
      geom_hline(yintercept = c(0.5, 1.5, 2.5, 3.5, 4.5, 5.5), 
                 linetype = "dashed", color = "grey", linewidth = 1) +
      common_theme +
      coord_cartesian(xlim = c(-25, 25), ylim = c(1, 6)) +
      scale_y_continuous(breaks = 1:6) +
      scale_color_manual(values = rater_colors, labels = rater_labels) +
      guides(color = guide_legend(title = "Rater"))
  }
  
  # Plot ICC for Essay Set 2
  plot_set2 <- function() {
    data_file <- file.path(base_path, "Set_#2_Expected_ICC_plot.csv")
    if (!file.exists(data_file)) stop("Set 2 data not found: ", data_file)
    
    data <- read.csv(data_file) %>% 
      setNames(c("Rater", "Theta", "Score", "Expected_Zones", "Half_Threshold")) %>%
      mutate(Rater = factor(Rater, levels = rater_labels))
    
    ggplot(data, aes(x = Theta, y = Score, color = Rater, group = Rater)) +
      geom_line(linewidth = 0.75) +
      labs(x = "Measure relative to item difficulty", y = "Score on Item") +
      geom_hline(yintercept = c(0.5, 1.5, 2.5, 3.5), 
                 linetype = "dashed", color = "grey", linewidth = 1) +
      common_theme +
      coord_cartesian(xlim = c(-25, 25), ylim = c(0, 4)) +
      scale_y_continuous(breaks = 0:4) +
      scale_color_manual(values = rater_colors, labels = rater_labels) +
      guides(color = guide_legend(title = "Rater"))
  }
  
  # Plot ICC for Essay Set 3
  plot_set3 <- function() {
    data_file <- file.path(base_path, "Set_#3_Expected_ICC_plot.xlsx")
    if (!file.exists(data_file)) stop("Set 3 data not found: ", data_file)
    
    sheet_names <- c("I&C", "Org", "V", "WC", "SF", "Con")
    
    # 使用 lapply + bind_rows 替代 map_dfr
    combined_data <- lapply(sheet_names, function(sheet) {
      read_excel(data_file, sheet = sheet) %>% 
        setNames(c("Rater", "Theta", "Score", "Expected_Zones", "Half_Threshold")) %>%
        mutate(
          Sheet = sheet,
          Rater = factor(Rater, levels = rater_labels),
          across(c(Theta, Score, Expected_Zones, Half_Threshold), as.numeric)
        )
    }) %>% 
      bind_rows() %>% 
      mutate(Sheet = factor(Sheet, levels = sheet_names))
    
    # 绘图代码保持不变
    ggplot(combined_data, aes(x = Theta, y = Score, color = Rater, group = Rater)) +
      geom_line(linewidth = 0.75) +
      labs(x = "Measure relative to item difficulty", y = "Score on Item") +
      geom_hline(yintercept = c(1.5, 2.5, 3.5, 4.5, 5.5), 
                 linetype = "dashed", color = "grey", linewidth = 0.5) +
      common_theme +
      theme(
        strip.text = element_text(size = 16, family = "Arial")
      ) +
      coord_cartesian(xlim = c(-12, 12), ylim = c(1, 6)) +
      scale_color_manual(values = rater_colors) +
      guides(color = guide_legend(title = "Rater")) +
      facet_grid(rows = vars(Sheet), scales = "free_y", switch = "y")
  }
  
  # Generate and display plots
  message("Generating ICC plots...")
  print(plot_set1())
  print(plot_set2())
  print(plot_set3())
}

# Execute analysis
run_icc_analysis()