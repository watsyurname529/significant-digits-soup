library(ggplot2)
library(ggthemes)

#Read in number data; expecting one number per row currently
number_csv_data <- read.csv("../data/numbers.csv", header=TRUE)

#Code for working with a csv file with the numbers in one row
#number_vec <- as.vector(number_csv_data, "numeric")
#number_data <- as.data.frame(number_vec)

full_hist <- ggplot(data=number_csv_data, aes(x=Number)) + geom_histogram(bins=1000) + labs(title = "Significant Digits Numbers", y = "Counts", x = "Number") + theme_fivethirtyeight()
ggsave("full_hist.pdf", width = 5, height = 5)

xlim_hist <- ggplot(data=number_csv_data, aes(x=Number)) + geom_histogram(bins=100) + labs(title = "Frequency of Significant Digits", y = "Counts", x = "Number") + xlim(0,100) + theme_fivethirtyeight()
ggsave("xlim_hist.pdf", width = 5, height = 5)
