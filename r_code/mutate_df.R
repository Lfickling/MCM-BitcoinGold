# load in CSV files
bitcoin_df <- read.csv("BCHAIN-MKPRU.csv") %>%
    as_tibble()


library(dplyr)
library(ggplot2)
library(data.table)
library(lubridate)

# Calculate volatility
calc_vol <- function(df, log = FALSE) {
    value_vec <- df$differences
    ret_val <- c()
    
    if (log == FALSE) {
        diff_vec <- df$differences
        
        for (i in 1:length(value_vec)) {
            new_val <- c(sd(c(diff_vec[i], diff_vec[i-1])))
            ret_val <- c(ret_val, new_val)
        }
    }
    else {
        log_diff_vec <- df$log_differences
        for (i in 1:length(log_diff_vec)) {
            new_val <- c(sd(c(log_diff_vec[i], log_diff_vec[i-1])))
            ret_val <- c(ret_val, new_val)
        }
    }
    ret_val
}

# -----------[ DATA PREPPING ]------------------
# Using mutate to add differences and log differences
# in both the bitcoin and gold data frames

# Mutate bitcoin df ----------------------------
bitcoin_df <- bitcoin_df %>%
    dplyr::mutate(
        differences = (Value - shift(Value, n = 1)) / Value * 100,
        log_differences = log(Value / shift(Value, n = 1)),
    )

# Calculate volatility using difference columns    
btc_vol <- calc_vol(bitcoin_df)
btc_log_vol <- calc_vol(bitcoin_df, log = TRUE)

bitcoin_df %>%
    dplyr::mutate(
        volatility = btc_vol,
        log_volatility = btc_log_vol
    ) %>%
    write.csv(file = "bitcoin_df")
    #View()

# GOLD MUTATING ----------------------------------

# Load in Gold CSV
gold_df <- read.csv("LBMA-GOLD.csv") %>%
    as_tibble()

# Mutate gold df -------------------------------
gold_df <- gold_df %>%
    dplyr::filter(!is.na(USD..PM.)) %>%
    dplyr::mutate(
        differences = (USD..PM. - shift(USD..PM., n = 1)) / USD..PM. * 100,
        log_differences = log(USD..PM. / shift(USD..PM., n = 1)),
        Date = lubridate::mdy(Date)
    )

# Calculate volatility using difference columns
gold_vol <- calc_vol(gold_df)
gold_log_vol <- calc_vol(gold_df, log = TRUE)

gold_df <- gold_df %>%
    dplyr::mutate(
        # Adds volatility and log_volatility columns
        volatility = gold_vol,
        log_volatility = gold_log_vol
    ) %>%
    # Complete adds in NA values for all missing dates.
    tidyr::complete(
        Date = seq.Date(
            min(Date), 
            max(Date), 
            by = "day"
        )
    ) %>%
    write.csv(file = "gold_df")

# Remove and isolate NA values in gold dataset
gold_df %>%
    dplyr:::filter(is.na(USD..PM.)) %>%
    write.csv(file = "gold_na_df")

# 