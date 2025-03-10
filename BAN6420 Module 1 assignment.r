# Load required library
library(dplyr)

# Generate a list of workers dynamically
set.seed(123)  # For reproducibility
num_workers <- 451
workers <- data.frame(
  name = paste0("Staff_102", 1:num_workers),
  salary = sample(5000:35000, num_workers, replace = TRUE),
  gender = sample(c("Male", "Female"), num_workers, replace = TRUE)
)

# Function to generate payment slips
generate_payment_slips <- function(workers) {
  workers <- workers %>%
    mutate(employee_level = case_when(
      salary > 10000 & salary < 20000 ~ "A1",
      salary > 7500 & salary < 30000 & gender == "Female" ~ "A5-F",
      TRUE ~ ""
    ))
  return(workers)
}

# Generate payment slips for all workers
payment_slips <- generate_payment_slips(workers)

# Print a few example payment slips
print(paste("Generating Payslips...", nrow(payment_slips), "payment slips"))
print("Done!\n")

# Function to print specific number of payment slips based on user input
print_payment_slips <- function(payment_slips) {
  numpaymentslips <- NA
  while(is.na(numpaymentslips) || numpaymentslips <= 0 || numpaymentslips > nrow(payment_slips)) {
    numpaymentslips <- as.numeric(readline(paste("How many payment slips do you want? (1 -", nrow(payment_slips), "): ")))
    if (is.na(numpaymentslips) || numpaymentslips <= 0 || numpaymentslips > nrow(payment_slips)) {
      cat("Please enter a number between 1 and", nrow(payment_slips), "\n")
    }
  }
  print(head(payment_slips, numpaymentslips))
}

# Ask user for the number of payment slips to print
print_payment_slips(payment_slips)
