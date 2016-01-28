library(ggplot2)

list_of_counts <- read.csv("../data/counts.csv", header=TRUE)
print(list_of_counts)

list_of_counts$DigitOrder <- factor(list_of_counts$Digit, levels=c("Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"))

plot_of_counts <- ggplot(list_of_counts, aes(x=DigitOrder, y=Counts)) + geom_bar(stat="identity")

plot_of_counts <- plot_of_counts + geom_text(aes(label = Counts, ymax=0), position=position_dodge(width = 0.9), vjust=-1, size=3)
plot_of_counts <- plot_of_counts + labs(title = "Frequency of Digits in Significant Digits", y = "Num. of Occurances", x = "Digit")

plot_of_counts <- plot_of_counts + theme(plot.title = element_text(vjust=2))
plot_of_counts <- plot_of_counts + theme(axis.title.x = element_text(vjust=-0.35))
plot_of_counts <- plot_of_counts + theme(axis.title.y = element_text(vjust=0.45))

ggsave("count_of_digits.png", width = 5, height = 5)
ggsave("count_of_digits.pdf", width = 5, height = 5)
