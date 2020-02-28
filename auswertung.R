library("dplyr")

# Datensatz aus der csv-Datei importieren
harzer_wasserstaende <- read.csv2("harzsperren_wasserstaende.csv")

# Datensatz um Doubletten bereinigen
harzer_wasserstaende_clean <- distinct(harzer_wasserstaende)

# Datumsvariable zu einer Datums-Klasse umwandeln
harzer_wasserstaende_clean$datum <- as.Date(harzer_wasserstaende_clean$datum, "%d.%m.%Y")

# 6 Datensätze nach 
oder <- harzer_wasserstaende_clean[ which(harzer_wasserstaende_clean$talsperre=="Oder"), ]
soese <- harzer_wasserstaende_clean[ which(harzer_wasserstaende_clean$talsperre=="Söse"), ]
ecker <- harzer_wasserstaende_clean[ which(harzer_wasserstaende_clean$talsperre=="Ecker"), ]
oker <- harzer_wasserstaende_clean[ which(harzer_wasserstaende_clean$talsperre=="Oker"), ]
grane <- harzer_wasserstaende_clean[ which(harzer_wasserstaende_clean$talsperre=="Grane"), ]
innerste <- harzer_wasserstaende_clean[ which(harzer_wasserstaende_clean$talsperre=="Innerste"), ]

jpeg("oder_plot.jpg")
plot(oder$datum, oder$stauinhaltfuellungsgrad, type="l", main = "Stauinhaltfüllungsgrad der Talsperre 'Oder'", xlab="Datum", ylab="Prozent (%)", ylim=c(0,100), col="blue", lwd=3)
dev.off()

jpeg("soese_plot.jpg")
plot(soese$datum, soese$stauinhaltfuellungsgrad, type="l", main = "Stauinhaltfüllungsgrad der Talsperre 'Söse'", xlab="Datum", ylab="Prozent (%)", ylim=c(0,100), col="blue", lwd=3)
dev.off()

jpeg("ecker_plot.jpg")
plot(ecker$datum, ecker$stauinhaltfuellungsgrad, type="l", main = "Stauinhaltfüllungsgrad der Talsperre 'Ecker'", xlab="Datum", ylab="Prozent (%)", ylim=c(0,100), col="blue", lwd=3)
dev.off()

jpeg("oker_plot.jpg")
plot(oker$datum, oker$stauinhaltfuellungsgrad, type="l", main = "Stauinhaltfüllungsgrad der Talsperre 'Oker'", xlab="Datum", ylab="Prozent (%)", ylim=c(0,100), col="blue", lwd=3)
dev.off()

jpeg("grane_plot.jpg")
plot(grane$datum, grane$stauinhaltfuellungsgrad, type="l", main = "Stauinhaltfüllungsgrad der Talsperre 'Grane'", xlab="Datum", ylab="Prozent (%)", ylim=c(0,100), col="blue", lwd=3)
dev.off()

jpeg("innerste_plot.jpg")
plot(innerste$datum, innerste$stauinhaltfuellungsgrad, type="l", main = "Stauinhaltfüllungsgrad der Talsperre 'Innerste'", xlab="Datum", ylab="Prozent (%)", ylim=c(0,100), col="blue", lwd=3)
dev.off()
