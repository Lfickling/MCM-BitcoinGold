bitcoin_df <- read.csv("bitcoin_df")
gold_df <- read.csv("gold_df")

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
