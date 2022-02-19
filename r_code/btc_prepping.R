library(dplyr)
library(data.table)
library(lubridate)

# -----------[ DATA PREPPING ]------------------
# Using mutate to add differences and log differences
# in both the bitcoin and gold data frames

# load in CSV files
bitcoin_df <- read.csv("BCHAIN-MKPRU.csv") %>%
    as_tibble()

# Mutate bitcoin df ----------------------------
bitcoin_df <- bitcoin_df %>%
    dplyr::mutate(
        differences = (Value - shift(Value, n = 1)) / Value * 100,
        log_differences = log(Value / shift(Value, n = 1)),
    )

# Calculate volatility using difference columns    
btc_vol <- calc_vol(bitcoin_df)
btc_log_vol <- calc_vol(bitcoin_df, log = TRUE)

bitcoin_df <- bitcoin_df %>%
    dplyr::mutate(
        volatility = btc_vol,
        log_volatility = btc_log_vol,
        mu = (
            (Value - data.table::shift(Value, n = 1)) / 
                data.table::shift(Value, n = 1)
        )
    ) 

cumulative_mu <- cumsum(tidyr::replace_na(bitcoin_df$mu, replace = 0))

sum_of_mu_squared_diff <- cumsum(
    tidyr::replace_na(
        data = (bitcoin_df$mu - cumulative_mu)^2,
        replace = 0 )
    )

btc_sigma_hat <- calculate_sigma_hat(sum_of_mu_squared_diff)

bitcoin_df %>%
    dplyr::mutate(
        cumulative_mu = cumulative_mu,
        sigma_hat = btc_sigma_hat
    ) %>%
    write.csv(file = "bitcoin_df.csv")
    #View()
