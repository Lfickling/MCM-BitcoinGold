library(ggplot2)
bitcoin_df <- read.csv("data_frames/bitcoin_df.csv")
gold_df <- read.csv("data_frames/gold_df.csv")

# ------------------[ LINE PLOTS ]----------------------
# -------[ BITCOIN PLOTS ]------------ 
# bitcoin log difference plot
ggplot2::ggplot() +
    geom_line(data = bitcoin_df, aes(x = as.Date(Date), y = log_differences)) +
    ylim(c(-0.3,0.2)) +
    scale_x_date(date_labels = "%d %b %Y") +
    labs(
        title = "Log Differences of Bitcoin Data Set Over Time") +
    ylab("Log Return") +
    theme(
        axis.title.x = element_blank()
    ) 

# bitcoin true difference plot
ggplot2::ggplot() +
    geom_line(data = bitcoin_df, aes(x = as.Date(Date), y = differences)) +
    ylim(c(-25,25)) +
    scale_x_date(date_labels = "%d %b %Y") +
    labs(
        title = "True Differences of Bitcoin Data Set Over Time") +
    ylab("Return (%)") +
    theme(
        axis.title.x = element_blank()
    )

# -------[GOLD PLOTS]-------
# gold log difference plot
ggplot2::ggplot() +
    geom_line(data = gold_df, aes(x = as.Date(Date), y = log_differences)) +
    ylim(c(-0.06,0.06)) +
    scale_x_date(date_labels = "%d %b %Y") +
    labs(
        title = "Log Differences of Gold Data Set Over Time") +
    ylab("Log Return") +
    theme(
        axis.title.x = element_blank()
    )

# gold true difference plot
ggplot2::ggplot() +
    geom_line(data = gold_df, aes(x = as.Date(Date), y = differences)) +
    #ylim(c(-0.06,0.06)) +
    scale_x_date(date_labels = "%d %b %Y") +
    labs(
        title = "True Differences of Gold Value Over Time"
    ) +
    ylab("Return (%)") +
    theme(
        axis.title.x = element_blank(),
    )

# --------------[ HISTOGRAMS ]-----------------------
# Bitcoin log return histogram
ggplot2::ggplot(data = bitcoin_df) +
    geom_histogram(aes(x = log_differences)) +
    labs(
        title = "Log Returns of Bitcoin"
    ) +
    xlab("Log Return") +
    ylab("Frequency") +
    theme_gray()

# Bitcoin true return histogram
ggplot2::ggplot(data = bitcoin_df) +
    geom_histogram(aes(x = differences)) +
    labs(
        title = "True Returns of Bitcoin"
    ) +
    xlab("Return (%)") +
    ylab("Frequency") +
    theme_gray()

# Gold log return histogram
ggplot2::ggplot(data = gold_df) +
    geom_histogram(aes(x = log_differences)) +
    labs(
        title = "Log Returns of Gold"
    ) +
    xlab("Log Return") +
    ylab("Frequency") +
    theme_gray()

# Gold true return histogram
ggplot2::ggplot(data = gold_df) +
    geom_histogram(aes(x = differences)) +
    labs(
        title = "True Returns of Bitcoin"
    ) +
    xlab("Return (%)") +
    ylab("Frequency") +
    theme_gray()

# --------------[ DENSITY PLOT ]-----------------------

# Bitcoin Density plot -----
ggplot2::ggplot(data = bitcoin_df, mapping = aes(x = differences)) +
    ggplot2::geom_density() +
    xlab("Returns (%)") +
    labs(title = "Probability Distribution of Bitcoin Returns") +
    scale_x_continuous(
        limits = c(-13,13),
        breaks = c(-3:3 * sd(bitcoin_df$differences, na.rm = TRUE) + mean(bitcoin_df$differences, na.rm = TRUE)),
        labels = c("\u03BC - 3\u03C3", "\u03BC - 2\u03C3", "\u03BC - \u03C3", "\u03BC", "\u03BC + \u03C3", "\u03BC + 2\u03C3", "\u03BC + 3\u03C3")
    ) +
    theme(axis.text.x = element_text(size=12),
          axis.title.y = element_blank())

# Gold Density plot -----
ggplot2::ggplot(data = gold_df, mapping = aes(x = differences)) +
    ggplot2::geom_density() +
    xlab("Returns (%)") +
    labs(title = "Probability Distribution of Gold Returns") +
    scale_x_continuous(
        limits = c(-2.5,2.5),
        breaks = c(-3:3 * sd(gold_df$differences, na.rm = TRUE) + mean(gold_df$differences, na.rm = TRUE)),
        labels = c("\u03BC - 3\u03C3", "\u03BC - 2\u03C3", "\u03BC - \u03C3", "\u03BC", "\u03BC + \u03C3", "\u03BC + 2\u03C3", "\u03BC + 3\u03C3")
    ) +
    theme(axis.text.x = element_text(size=12),
          axis.title.y = element_blank())
