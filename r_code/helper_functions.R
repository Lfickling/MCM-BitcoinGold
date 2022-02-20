# Helper functions
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

#-----
calc_mu_and_sigma <- function(vector) {
    mu_vec <- c()
    sigma_vec <- c()
    
    for (i in 1:length(vector$Value)) {
        new_mu_value <- mean(vector$Value[1:i])
        mu_vec <- c(mu_vec, new_mu_value)
        
        new_sigma_value <- sd(vector$Value[1:i])
        sigma_vec <- c(sigma_vec, new_sigma_value)
    }
    ret_table <- data.table::data.table(
        mu_vec = mu_vec,
        sigma_vec = sigma_vec
    )
    
    ret_table
}

#-----

calculate_sigma_hat <- function(vec) {
    ret_vec <- c()
    
    for (i in 1:length(vec)) {
        new_value <- sqrt(c((1 / (i - 1)) * (vec[i])))
        ret_vec <- c(ret_vec, new_value)
    }
    ret_vec
}
