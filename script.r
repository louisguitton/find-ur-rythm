source("http://bioconductor.org/biocLite.R")
biocLite("rhdf5")
library(rhdf5)
library(ggplot2)

project.folder = "..."
setwd(project.folder)

mydata <- h5read("Enregistrements EEG/Test_Charles_droite_Test_Charles_droite_04-mars2016.h5", "signal_0/sig")


mydata
dim(mydata)
plot(mydata[1:1000], pch = 20)

df = data.frame(mydata[1:50000])

g = ggplot(data = df, aes(x = c(1:50000), y = mydata.1.50000.))
g + geom_line()
