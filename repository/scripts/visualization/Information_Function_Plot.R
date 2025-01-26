run_analysis <- function(data_dir = "repository/data/visualization") {
  # Load required libraries
  require(ggplot2)
  require(dplyr)
  require(extrafont)
  require(patchwork)
  
  # Load fonts (Windows systems only)
  if (.Platform$OS.type == "windows") {
    tryCatch({
      loadfonts(device = "win")
    }, error = function(e) {
      message("Font loading failed, using system default: ", e$message)
    })
  }
  
  # Data processing and plotting function
  process_and_plot <- function(set_number) {
    # Construct file path
    file_path <- file.path(data_dir, sprintf("Set_#%d_Information.csv", set_number))
    
    if (!file.exists(file_path)) {
      stop("File not found: ", file_path)
    }
    
    data <- read.csv(file_path)
    
    # Re-factor Rater column
    data$Rater <- factor(data$Rater, 
                         levels = c("HR-1", "HR-2", "4o-Mini", "GPT-4o", "CL-3.5-H", "CL-3.5-S"))
    
    # Process Trait column for third dataset
    if(set_number == 3) {
      data$Trait <- factor(data$Trait, 
                           levels = c("I&C", "Org", "V", "WC", "SF", "Con"))
    }
    
    # Plot parameters
    colors <- c('#E64B35', '#F39B7F', '#00A087', '#4DBBD5', '#3C5488', '#FF1493')
    new_labels <- c("HR-1", "HR-2", "4o-Mini", "GPT-4o", "CL-3.5-H", "CL-3.5-S")
    
    # Create base plot
    p <- ggplot(data, aes(x = Theta, y = info_data_rater, color = Rater)) +
      geom_line(linewidth = 1.5) +
      scale_color_manual(values = colors, labels = new_labels, drop = FALSE) +
      labs(x = expression(theta), y = "Information") +
      geom_hline(yintercept = 0.25, linetype = "dashed", color = "grey", linewidth = 1) +
      theme_minimal() +
      coord_cartesian(xlim = c(-20, 20), ylim = c(0, 0.75)) +
      scale_y_continuous(breaks = seq(0, 0.75, by = 0.25))
    
    # Set theme elements
    base_theme <- theme(
      axis.title = element_text(size = 24, family = "Arial"),
      axis.text = element_text(size = 24, family = "Arial"),
      legend.title = element_blank(),
      legend.text = element_text(size = 20, family = "Arial"),
      legend.position = "right"
    )
    
    # Add facet settings (third dataset only)
    if(set_number == 3) {
      p <- p + 
        facet_wrap(~ Trait, ncol = 2) +
        theme(
          strip.text = element_text(size = 20, family = "Arial"),
          panel.spacing = unit(2, "lines")
        )
    }
    
    p + base_theme
  }
  
  # Generate all plots
  message("Generating plots...")
  plots <- lapply(1:3, process_and_plot)
  
  # Combine plots
  combined_12 <- plots[[1]] / plots[[2]]
  final_plot <- combined_12 | plots[[3]]
  
  # Display plots
  print(final_plot + plot_layout(widths = c(1, 2)))
}

# Usage example (adjust path as needed):
run_analysis()  # Use default path