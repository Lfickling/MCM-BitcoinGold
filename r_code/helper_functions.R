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

calculate_sigma_hat <- function(vec) {
    ret_vec <- c()
    
    for (i in 1:length(vec)) {
        new_value <- sqrt(c((1 / (i - 1)) * (vec[i])))
        ret_vec <- c(ret_vec, new_value)
    }
    ret_vec
}
