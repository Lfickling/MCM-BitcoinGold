# load in new updated data frames
bitcoin_df <- read.csv("data_frames/bitcoin_df")
gold_df <- read.csv("data_frames/gold_df")

library(dplyr)
library(ggplot2)
library(data.table)

# Calculate volatility
calc_vol <- function(df, log = FALSE) {
    value_vec <- df$differences
    ret_val <- c()
    
    if (log == FALSE) {
        value_vec <- df$differences
        
        for (i in 1:length(value_vec)) {
            new_val <- c(sd(c(value_vec[i+1], value_vec[i])))
            ret_val <- c(ret_val, new_val)
        }
    }
    else {
        value_vec <- df$log_differences
        for (i in 1:length(value_vec)) {
            new_val <- c(sd(c(value_vec[i+1], value_vec[i])))
            ret_val <- c(ret_val, new_val)
        }
    }
    ret_val
}

# -----------[ DATA PREPPING ]------------------
# Using mutate to add differences and log differences
# in both the bitcoin and gold data frames

# Calculate vol for bitcoin
btc_vol <- calc_vol(bitcoin_df)
btc_log_vol <- calc_vol(bitcoin_df, log = TRUE)

bitcoin_df %>%
    dplyr::mutate(
        differences = (Value - shift(Value, n = 1)) / Value * 100,
        log_differences = log(Value / shift(Value, n = 1)),
        volatility = btc_vol,
        log_volatility = btc_log_vol
    ) %>%
    #write.csv(file = "bitcoin_df")
    View()

# Calculate vol for gold
gold_vol <- calc_vol(gold_df)
gold_log_vol <- calc_vol(gold_df, log = TRUE)

# Modify data frame
gold_df %>%
    dplyr::mutate(
        differences = (USD..PM. - shift(USD..PM., n = 1)) / USD..PM. * 100,
        log_differences = log(USD..PM. / shift(USD..PM., n = 1)),
        voltaility = gold_vol,
        log_volatility = gold_log_vol
    ) %>%
    #write.csv(file = "gold_df")
    View()
