#bitcoin_df <- read.csv("Downloads/2022_MCM_ICM_Problems/BCHAIN-MKPRU.csv")
#gold_df <- read.csv("Downloads/2022_MCM_ICM_Problems/LBMA-GOLD.csv")

library(dplyr)
library(ggplot2)
library(data.table)

# -----------[ DATA PREPPING ]------------------
# Using mutate to add differences and log differences
# in both the bitcoin and gold data frames
bitcoin_df %>%
    dplyr::mutate(
        differences = (Value - shift(Value, n = 1)) / Value * 100,
        log_differences = log(Value / shift(Value, n = 1))
    ) %>%
    write.csv(file = "bitcoin_df")
    #View()

gold_df %>%
    dplyr::mutate(
        differences = (USD..PM. - shift(USD..PM., n = 1)) / USD..PM. * 100,
        log_differences = log(USD..PM. / shift(USD..PM., n = 1))
    ) %>%
    write.csv(file = "gold_df")
    #View()

# load in new updated data frames
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
