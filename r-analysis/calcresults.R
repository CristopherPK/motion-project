calcResults <- function(data = mcData){
    massFore <- mcData$massScapula + mcData$massBrachium + mcData$massAntBrach + mcData$massMetacps + mcData$massDigitF
    massHind <- mcData$massThigh + mcData$massCrus + mcData$massMetatrs + mcData$massDigitH
    
    xfCM <- (mcData$xScapula*mcData$massScapula + mcData$xBrachium*mcData$massBrachium + mcData$xAntBrach*mcData$massAntBrach + mcData$xMetacarpus*mcData$massMetacps + mcData$xDigitF*mcData$massDigitF)/massFore
    yfCM <- (mcData$yScapula*mcData$massScapula + mcData$yBrachium*mcData$massBrachium + mcData$yAntBrach*mcData$massAntBrach + mcData$yMetacarpus*mcData$massMetacps + mcData$yDigitF*mcData$massDigitF)/massFore
    
    xhCM <- (mcData$xThigh*mcData$massThigh + mcData$xCrus*mcData$massCrus + mcData$xMetatrs*mcData$massMetatrs + mcData$xDigitH*mcData$massDigitH)/massHind
    yhCM <- (mcData$yThigh*mcData$massThigh + mcData$yCrus*mcData$massCrus + mcData$yMetatrs*mcData$massMetatrs + mcData$yDigitH*mcData$massDigitH)/massHind
    
    
}