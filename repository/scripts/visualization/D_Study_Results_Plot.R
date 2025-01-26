# Load required libraries
library(ggplot2)
library(dplyr)
library(extrafont)
library(patchwork)

# Main analysis function
run_analysis <- function(data_dir = "repository/data/visualization") {
  # Load fonts (Windows only)
  load_fonts <- function() {
    if (.Platform$OS.type == "windows") {
      tryCatch({
        loadfonts(device = "win")
      }, error = function(e) {
        message("Font loading failed: ", e$message)
      })
    }
  }
  
  # Data processing function
  process_dataset <- function(set_number) {
    file_path <- file.path(data_dir, sprintf("Set_#%d_D_Study_Results.csv", set_number))
    
    if (!file.exists(file_path)) {
      stop("Data file not found: ", file_path)
    }
    
    data <- read.csv(file_path)
    data$Rater_Type <- factor(data$Rater_Type, 
                              levels = c("HR", "GPT", "Claude"))
    return(data)
  }
  
  # Create unified theme
  create_common_theme <- function() {
    theme_minimal() +
      theme(
        plot.title = element_blank(),
        axis.title = element_text(size = 26, family = "Arial"),
        axis.text = element_text(size = 24, family = "Arial"),
        legend.title = element_blank(),
        legend.text = element_text(size = 20, family = "Arial"),
        legend.box = "vertical"
      )
  }
  
  # Shared plot settings
  common_plot_settings <- list(
    scale_color_manual(
      values = c('#E64B35', '#008000', '#3C5488'),
      labels = c("HR", "GPT", "Claude")
    ),
    scale_y_continuous(limits = c(0.5, 1), breaks = seq(0.5, 1, by = 0.1)),
    scale_x_continuous(breaks = seq(2, 12, by = 2))
  )
  
  # G-coefficient plot generator
  create_g_plot <- function(data) {
    ggplot(data, aes(x = Rater_Numbers, y = G.Coefficient, 
                     color = Rater_Type, group = Rater_Type)) +
      geom_line(linewidth = 1) +
      geom_point(size = 3) +
      labs(x = "Rater Numbers", y = "G Coefficient") +
      geom_hline(yintercept = 0.8, linetype = "dashed", 
                 color = "grey", linewidth = 0.8) +
      create_common_theme() +
      common_plot_settings
  }
  
  # Phi-coefficient plot generator
  create_phi_plot <- function(data) {
    ggplot(data, aes(x = Rater_Numbers, y = Phi.Coefficient,
                     color = Rater_Type, group = Rater_Type)) +
      geom_line(linewidth = 1) +
      geom_point(size = 3) +
      labs(x = "Rater Numbers", y = expression(paste(phi, " Coefficient"))) +
      geom_hline(yintercept = 0.8, linetype = "dashed",
                 color = "grey", linewidth = 0.8) +
      create_common_theme() +
      common_plot_settings +
      theme(legend.position = "none")
  }
  
  # Main execution flow
  load_fonts()
  
  # Generate plots for all datasets
  plot_list <- lapply(1:3, function(set_number) {
    dataset <- process_dataset(set_number)
    g_plot <- create_g_plot(dataset)
    phi_plot <- create_phi_plot(dataset)
    
    (g_plot / phi_plot) + 
      plot_layout(guides = 'collect') +
      plot_annotation(theme = theme(legend.position = "right"))
  })
  
  # Display results
  message("Displaying analysis results...")
  for(plot in plot_list) {
    print(plot)
  }
}

# Execute analysis
run_analysis()