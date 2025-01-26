# Load required libraries
library(ggplot2)
library(tidyr)
library(dplyr)
library(readxl)
library(extrafont)
library(purrr)

# Main analysis function
run_analysis <- function(data_path = "repository/data/visualization") {
  # Initialize environment
  load_fonts <- function() {
    if (.Platform$OS.type == "windows") {
      tryCatch({
        loadfonts(device = "win")
      }, error = function(e) {
        message("Font loading failed: ", e$message)
      })
    }
  }
  
  # Define constants
  constants <- list(
    RATER_LEVELS = c("HR-1", "HR-2", "4o-Mini", "GPT-4o", "CL-3.5-H", "CL-3.5-S"),
    LABEL_LEVELS = c("Extreme", "Overfit", "Normal", "Underfit"),
    COLOR_LEVELS = c("black", "navy", "darkgreen", "darkred")
  )
  
  # Create common theme
  create_theme <- function() {
    theme_minimal() +
      theme(
        strip.text = element_text(size = 20, family = "Arial"),
        axis.text = element_text(size = 22, family = "Arial"), 
        axis.title = element_text(size = 24, family = "Arial"),
        legend.text = element_text(size = 20, family = "Arial"),
        legend.title = element_blank(),
        legend.position = "right",
        panel.spacing = unit(1, "lines")
      )
  }
  
  # Data processing pipeline
  process_data <- function(raw_data) {
    raw_data %>%
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
        label = factor(label, levels = constants$LABEL_LEVELS),
        color = factor(color, levels = constants$COLOR_LEVELS),
        Rater = factor(Rater, levels = constants$RATER_LEVELS)
      )
  }
  
  # Visualization generator
  generate_plots <- function(processed_data, plot_title = NULL) {
    plot_settings <- list(
      scale_fill_manual(values = setNames(constants$COLOR_LEVELS, constants$LABEL_LEVELS)),
      labs(x = "Category", y = "Category Percent %"),
      scale_y_continuous(limits = c(0, 85), breaks = seq(0, 100, by = 20)),
      create_theme()
    )
    
    # First group plot
    p1 <- processed_data %>%
      filter(Rater %in% constants$RATER_LEVELS[1:3]) %>%
      ggplot(aes(x = factor(Category), y = Category_Percent, fill = label)) +
      geom_bar(stat = "identity") +
      facet_wrap(~Rater, scales = "free_y") +
      plot_settings
    
    # Second group plot
    p2 <- processed_data %>%
      filter(Rater %in% constants$RATER_LEVELS[4:6]) %>%
      ggplot(aes(x = factor(Category), y = Category_Percent, fill = label)) +
      geom_bar(stat = "identity") +
      facet_wrap(~Rater, scales = "free_y") +
      plot_settings
    
    list(p1, p2)
  }
  
  # Main plot controller
  analyze_dataset <- function(set_number, dimensions = NULL) {
    data_files <- if(is.null(dimensions)) {
      sprintf("Set_#%d_Category_Percent.csv", set_number)
    } else {
      sprintf("Set_#%d_Category_Percent_%s.csv", set_number, dimensions)
    }
    
    for(file in data_files) {
      full_path <- file.path(data_path, file)
      if(!file.exists(full_path)) {
        message("File not found: ", full_path)
        next
      }
      
      raw_data <- read.csv(full_path)
      processed_data <- process_data(raw_data)
      plots <- generate_plots(processed_data)
      
      # Display plots
      walk(plots, print)
    }
  }
  
  # Execution flow
  load_fonts()
  
  message("Starting analysis...")
  analyze_dataset(1)
  analyze_dataset(2)
  analyze_dataset(3, dimensions = c("I&C", "Org", "V", "WC", "SF", "Con"))
  message("Analysis completed!")
}

# Execute analysis
run_analysis()