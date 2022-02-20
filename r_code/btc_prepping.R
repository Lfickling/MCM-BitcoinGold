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
        Date = lubridate::mdy(Date),
        weekend = format(Date, "%u") %in% c(6,7)
    )

# Calculate volatility using difference columns -----   
btc_vol <- calc_vol(bitcoin_df)
btc_log_vol <- calc_vol(bitcoin_df, log = TRUE)

# Calculate mu and sigma ----
mu_sigma_df <- calc_mu_and_sigma(bitcoin_df$Value)

bitcoin_df <- bitcoin_df %>%
    dplyr::mutate(
        volatility = btc_vol,
        log_volatility = btc_log_vol,
        mu = mu_sigma_df$mu_vec,
        sigma = mu_sigma_df$sigma_vec
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
    dplyr::relocate(
        weekend, .after = dplyr::last_col()
    ) %>%
    write.csv(file = "bitcoin_df.csv")
    #View()
