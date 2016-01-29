library(ggplot2)

#Read in number data; expecting one number per row currently
number_csv_data <- read.csv("numbers_col.csv", header=TRUE)

#Code for working with a csv file with the numbers in one row
#number_vec <- as.vector(number_csv_data, "numeric")
#number_data <- as.data.frame(number_vec)

full_hist <- ggplot(data=number_csv_data, aes(x=Number)) + geom_histogram(bins=1000)
ggsave("full_hist.pdf", width = 5, height = 5)

xlim_hist <- ggplot(data=number_csv_data, aes(x=Number)) + geom_histogram(bins=100) + xlim(0,100)
ggsave("xlim_hist.pdf", width = 5, height = 5)
