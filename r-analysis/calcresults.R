calcResults <- function(data = mcData){
    library(ggplot2)
  
    mcData = read.csv(file = "results.csv")
    write.csv(x = mcData, file = "results.csv")
  
    massFore <- mcData$massScapula + mcData$massBrachium + mcData$massAntBrach + mcData$massMetacps + mcData$massDigitF
    massHind <- mcData$massThigh + mcData$massCrus + mcData$massMetatrs + mcData$massDigitH
    
    xfCM <- (mcData$xScapula*mcData$massScapula + mcData$xBrachium*mcData$massBrachium + mcData$xAntBrach*mcData$massAntBrach + mcData$xMetacarpus*mcData$massMetacps + mcData$xDigitF*mcData$massDigitF)/massFore
    yfCM <- (mcData$yScapula*mcData$massScapula + mcData$yBrachium*mcData$massBrachium + mcData$yAntBrach*mcData$massAntBrach + mcData$yMetacarpus*mcData$massMetacps + mcData$yDigitF*mcData$massDigitF)/massFore
    
    xhCM <- (mcData$xThigh*mcData$massThigh + mcData$xCrus*mcData$massCrus + mcData$xMetatrs*mcData$massMetatrs + mcData$xDigitH*mcData$massDigitH)/massHind
    yhCM <- (mcData$yThigh*mcData$massThigh + mcData$yCrus*mcData$massCrus + mcData$yMetatrs*mcData$massMetatrs + mcData$yDigitH*mcData$massDigitH)/massHind
    
    qplot(main = "Forelimb", x = xfCM, y = yfCM, geom='smooth', span = 0.1, xlim = c(4,-4), ylim = c(-0.5,0.5), xlab = "Horizontal Movement", ylab = "Vertical Movement")
    qplot(main = "Hindlimb", x = xhCM, y = yhCM, geom='smooth', span = 0.1, xlim = c(4,-4), ylim = c(-0.5,0.5), xlab = "Horizontal Movement", ylab = "Vertical Movement")
    qplot(main = "Mass Centre", x = mcData$xBCM, y = mcData$yBCM, geom='smooth', span = 0.1, xlim = c(4,-4), ylim = c(1.5, 2.5), xlab = "Horizontal Movement", ylab = "Vertical Movement")
    #qplot(x = mcData$xBCM, y = mcData$yBCM, geom='smooth', span = 0.05)
}