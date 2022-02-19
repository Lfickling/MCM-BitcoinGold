bitcoin_df <- read.csv("Downloads/2022_MCM_ICM_Problems/BCHAIN-MKPRU.csv")
gold_df <- read.csv("Downloads/2022_MCM_ICM_Problems/LBMA-GOLD.csv")

bitcoin_dt <- as.data.table(bitcoin_df)

library(dplyr)
library(ggplot2)
library(data.table)

# Creates new column with differences
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
