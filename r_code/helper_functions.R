# Helper functions
# Calculate volatility --------------------------------------------------------
calc_vol <- function(df, log = FALSE, gold = FALSE) {
    ret_val <- c()
    
    # Gold data set version
    if (gold) {
        weekend <- df$weekend
        
        if (log == FALSE) {
            diff_vec <- df$differences
            
            for (i in 1:nrow(df)) {
                if ( i > 1 && !is.na(df$USD..PM.[i]) && weekend[i] == FALSE && weekend[i-1] == TRUE ) {
                    #print("Today is monday")
                    
                    new_val <- c(sd(c(diff_vec[i], diff_vec[i-3])))
                    ret_val <- c(ret_val, new_val)
                }
                
                else {
                    new_val <- c(sd(c(diff_vec[i], diff_vec[i-1])))
                    ret_val <- c(ret_val, new_val)
                }
            }
        }
        
        else {
            log_diff_vec <- df$log_differences
            
            for (i in 1:nrow(df)) {
                if ( i > 1 && weekend[i] == FALSE && weekend[i-1] == TRUE ) {
                    #print("Today is monday")
                    
                    m <- 3
                    while (is.na(log_diff_vec[i-m])) {
                        m <- m+1
                    }
                    
                    new_val <- c(sd(c(log_diff_vec[i], log_diff_vec[i-m])))
                    ret_val <- c(ret_val, new_val)
                }
                
                else{
                    new_val <- c(sd(c(log_diff_vec[i], log_diff_vec[i-1])))
                    ret_val <- c(ret_val, new_val)
                }
            }
        }
        
        return(ret_val)
    }
    # btc data set version
    else{
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
    }
    ret_val
}

#-----
calc_mu_and_sigma <- function(vector) {
    mu_vec <- c()
    sigma_vec <- c()
    
    for (i in 1:length(vector)) {
        new_mu_value <- mean(vector[1:i], na.rm = TRUE)
        mu_vec <- c(mu_vec, new_mu_value)
        
        new_sigma_value <- sd(vector[1:i], na.rm = TRUE)
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
