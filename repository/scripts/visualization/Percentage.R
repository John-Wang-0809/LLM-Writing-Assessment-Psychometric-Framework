# Load required libraries
library(ggplot2)
library(dplyr)
library(gridExtra)
library(extrafont)
library(grid)

# Main analysis function
run_score_analysis <- function(
    base_path = "repository/data/processed", 
    colors = c("darkred", "darkblue", "darkgreen")
) {
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
  process_dataset <- function(file_path, set_number) {
    if (!file.exists(file_path)) {
      stop("Data file not found: ", file_path)
    }
    
    data <- read.csv(file_path, encoding = 'UTF-8')
    
    data %>%
      group_by(Scores) %>%
      summarise(Frequency = n(), .groups = 'drop') %>%
      mutate(Frequency_Percentage = Frequency / sum(Frequency) * 100,
             Set = factor(paste("Set #", set_number)))
  }
  
  # Visualization generator
  create_plot <- function(data, color) {
    ggplot(data, aes(x = factor(Scores), y = Frequency_Percentage)) +
      geom_bar(stat = "identity", fill = color, width = 0.7) +
      labs(x = "Score", y = "Frequency Percentage (%)") +
      theme_minimal() +
      theme(
        plot.title = element_text(size = 18, family = "Arial", hjust = 0.5),
        axis.title = element_text(size = 20, family = "Arial"),
        axis.text = element_text(size = 18, family = "Arial"),
        panel.grid.major.x = element_blank(),
        panel.grid.minor.y = element_blank()
      )
  }
  
  # Main execution flow
  load_fonts()
  
  # Generate file paths
  data_files <- file.path(
    base_path,
    paste0("Essay_Set_#", 1:3),
    paste0("rater_data_", 1:3, "_for_MFRM.csv")
  )
  
  # Process all datasets
  plot_data <- lapply(1:3, function(i) {
    process_dataset(data_files[i], i)
  })
  
  # Create plots
  plots <- lapply(1:3, function(i) {
    create_plot(plot_data[[i]], colors[i]) +
      ggtitle(paste("Essay Set", i))
  })
  
  # Combine and display plots
  combined_plot <- grid.arrange(
    grobs = plots,
    ncol = 3,
    top = textGrob("Score Distribution Analysis", 
                  gp = gpar(fontsize = 22, fontfamily = "Arial"))
  )
  
  # Return combined plot object
  invisible(combined_plot)
}

# Execute analysis
run_score_analysis()

# To save output: 
# ggsave("combined_plot.png", plot = combined_plot, width = 16, height = 8)