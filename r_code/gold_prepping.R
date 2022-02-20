# Mutate Gold Data set
library(dplyr)
library(data.table)
library(lubridate)


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
# Calculate mu and sigma
gold_mu_sigma_df <- calc_mu_and_sigma(gold_df$USD..PM.)

gold_df <- gold_df %>%
    dplyr::mutate(
        # Adds volatility and log_volatility columns
        volatility = gold_vol,
        log_volatility = gold_log_vol,
        # Adds Mu column
        mu = gold_mu_sigma_df$mu_vec,
        sigma = gold_mu_sigma_df$sigma_vec
        )

# Complete adds in NA values for all missing dates.
gold_df <- gold_df %>%
    tidyr::complete(
        Date = seq.Date(
            min(Date), 
            max(Date), 
            by = "day"
        )
    ) %>%
    dplyr::mutate(
        weekend = format(Date, "%u") %in% c(6,7)
    )

# Variables -------
cumulative_mu <- cumsum(tidyr::replace_na(gold_df$mu, replace = 0))
sum_of_mu_squared_diff <- cumsum(
    tidyr::replace_na(
        data = (gold_df$mu - cumulative_mu)^2,
        replace = 0 )
)
gold_sigma_hat <- calculate_sigma_hat(sum_of_mu_squared_diff)

gold_df <- gold_df %>%
    dplyr::mutate(
        cumulative_mu = cumulative_mu,
        sigma_hat = gold_sigma_hat
    )

sync_day <- data.frame(
    Date = lubridate::ymd("2016-09-11"), 
    USD..PM. = NA, 
    differences = NA, 
    log_differences = NA, 
    volatility = NA, 
    log_volatility = NA, 
    mu = NA, 
    sigma = NA, 
    weekend = TRUE, 
    cumulative_mu = NA, 
    sigma_hat = NA)

gold_data <- rbind(sync_day, gold_df)

gold_data %>% 
    dplyr::relocate(
        weekend, .after = dplyr::last_col()
    ) %>%
    #View()
    write.csv(file = "gold_df.csv")

# Don't re-run -----------------------------------------
# Remove and isolate NA values in gold dataset
# gold_df %>%
#     dplyr:::filter(is.na(USD..PM.)) %>%
#     write.csv(file = "gold_na_df.csv")