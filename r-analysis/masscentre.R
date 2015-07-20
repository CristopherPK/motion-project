massCentre <- function(tracks, massExpected){
    #This function calculates the Body Centre of Mass in according to Buchner, 1997 method.
    #16 Segments are used.
    xs <- tracks[[1]]
    ys <- tracks[[2]]
    massCentreData <- NULL
    head <- NULL
    neck <- NULL
    trunk <- NULL
    tail <- NULL
    scapula <- NULL
    brachium <- NULL
    antebrachium <- NULL
    metacarpus <- NULL
    digitf <- NULL
    thigh <- NULL
    crus <- NULL
    metatarsus <- NULL
    digith <- NULL
        
    for (i in 1:nrow(xs)){
        ## Head (2-1)
        lHead = 0.27
        lHeadPxs = sqrt((xs[,2][i] - xs[,1][i])^2 + (ys[,2][i] - ys[,1][i])^2)
        t = lHead/lHeadPxs
        massHead = 0.637/(0.226*(lHead)^2)
        xHead = xs[,1][i]*t + (-0.09)*lHead
        yHead = ys[,1][i]*t + 0.73*lHead
        if(is.null(head)){
            head <- data.frame(lHead = lHead, massHead = massHead, xHead = xHead, yHead = yHead)
        } else {
            head[i,] <- c(lHead, massHead, xHead, yHead)
        }
        
        ## Neck (3-2)
        lNeck = 0.46
        lNeckPxs = sqrt((xs[,3][i] - xs[,2][i])^2 + (ys[,3][i] - ys[,2][i])^2)
        t = lNeck/lNeckPxs
        #massNeck = 26.8
        massNeck = (26.8*lNeck)/0.54
        xNeck = xs[,2][i]*t + 0.11*lNeck
        yNeck = ys[,2][i]*t + 0.46*lNeck
        if(is.null(neck)){
            neck <- data.frame(lNeck = lNeck, massNeck = massNeck, xNeck = xNeck, yNeck = yNeck)
        } else {
            neck[i,] <- c(lNeck, massNeck, xNeck, yNeck)
        }
        
        ## Trunk (4-3)
        lTrunk = 1.23
        lTrunkPxs = sqrt((xs[,4][i] - xs[,3][i])^2 + (ys[,4][i] - ys[,3][i])^2)
        t = lTrunk/lTrunkPxs
        massTrunk = 58.24/(0.0676*(lTrunk)^2)
        xTrunk = xs[,4][i]*t + (-0.103)*lTrunk
        yTrunk = ys[,4][i]*t + (0.469)*lTrunk
        if(is.null(trunk)){
            trunk <- data.frame(lTrunk = lTrunk, massTrunk = massTrunk, xTrunk = xTrunk, yTrunk = yTrunk)
        } else {
            trunk[i,] <- c(lTrunk, massTrunk, xTrunk, yTrunk)
        }
        
        ## Tail (4-5)
        lTail = 0.62
        lTailPxs = sqrt((xs[,4][i] - xs[,5][i])^2 + (ys[,4][i] - ys[,5][i])^2)
        t = lTail/lTailPxs 
        massTail = 10.646*lTail - 3.824
        xTail = xs[,4][i] + (0.03)*lTail
        yTail = ys[,4][i] + (0.73)*lTail
        if(is.null(tail)){
            tail <- data.frame(lTail = lTail, massTail = massTail, xTail = xTail, yTail = yTail)
        } else {
            tail[i,] <- c(lTail, massTail, xTail, yTail)
        }
        
        ## Scapula (6-7)
        lScapula = 0.28
        lScapulaPxs = sqrt((xs[,7][i] - xs[,6][i])^2 + (ys[,7][i] - ys[,6][i])^2)
        t = lScapula/lScapulaPxs
        massScapula = 41.83*lScapula + 0.047
        xScapula = xs[,6][i]*t + (-0.12)*lScapula
        yScapula = ys[,6][i]*t + (0.27)*lScapula
        if(is.null(scapula)){
            scapula <- data.frame(lScapula = lScapula, massScapula = massScapula, xScapula = xScapula, yScapula = yScapula)
        } else {
            scapula[i,] <- c(lScapula, massScapula, xScapula, yScapula)
        }
        
        ## Brachium (7-8)
        lBrachium = 0.24
        lBrachiumPxs = sqrt((xs[,8][i] - xs[,7][i])^2 + (ys[,8][i] - ys[,7][i])^2)
        massBrachium = 0.183/(0.076*(lBrachium)^2)
        t = lBrachium/lBrachiumPxs
        xBrachium = xs[,7][i]*t + (-0.05)*lBrachium
        yBrachium = ys[,7][i]*t + (0.51)*lBrachium
        if(is.null(brachium)){
            brachium <- data.frame(lBrachium = lBrachium, massBrachium = massBrachium, xBrachium = xBrachium, yBrachium = yBrachium)
        } else {
            brachium[i,] <- c(lBrachium, massBrachium, xBrachium, yBrachium)
        }
        
        ## Antebrachium(8-9)
        lAntBrach = 0.40
        lAntBrachPxs = sqrt((xs[,9][i] - xs[,8][i])^2 + (ys[,9][i] - ys[,8][i])^2)
        t = lAntBrach/lAntBrachPxs
        massAntBrach = 17.76*lAntBrach - 1.017
        xAntBrach = xs[,8][i]*t + (-0.021)*lAntBrach
        yAntBrach = ys[,8][i]*t + (0.35)*lAntBrach
        if(is.null(antebrachium)){
            antebrachium <- data.frame(lAntebrachium = lAntBrach, massAntBrach = massAntBrach, xAntBrach = xAntBrach, yAntBrach = yAntBrach)
        } else {
            antebrachium[i,] <- c(lAntBrach, massAntBrach, xAntBrach, yAntBrach)
        }
        
        ## Metacarpus (9-10)
        lMetacarpus = 0.27
        lMetacarpusPxs = sqrt((xs[,10][i] - xs[,9][i])^2 + (ys[,10][i] - ys[,9][i])^2)
        t = lMetacarpus/lMetacarpusPxs
        massMetacps = 0.01195/(0.0913*(lMetacarpus)^2)
        xMetacarpus = xs[,9][i]*t + (-0.01)*lMetacarpus
        yMetacarpus = ys[,9][i]*t + (0.44)*lMetacarpus
        if(is.null(metacarpus)){
            metacarpus <- data.frame(lMetacarpus = lMetacarpus, massMetacps = massMetacps, xMetacarpus = xMetacarpus, yMetacarpus = yMetacarpus)
        } else {
            metacarpus[i,] <- c(lMetacarpus, massMetacps, xMetacarpus, yMetacarpus)
        }
        
        ## Digit Forelimb (10-11)
        lDigitF = 0.15
        lDigitFPxs = sqrt((xs[,11][i] - xs[,10][i])^2 + (ys[,11][i] - ys[,10][i])^2)
        t = lDigitF/lDigitFPxs
        massDigitF = 0.0096/(0.307*(lDigitF)^2)
        xDigitF = xs[,10][i]*t + (-0.18)*lDigitF
        yDigitF = ys[,10][i]*t + (0.92)*lDigitF
        if(is.null(digitf)){
            digitf <- data.frame(lDigitF = lDigitF, massDigitF = massDigitF, xDigitF = xDigitF, yDigitF = yDigitF)
        } else {
            digitf[i,] <- c(lDigitF, massDigitF, xDigitF, yDigitF)
        }
        
        ## Thigh (13-14)
        lThigh = 0.30
        lThighPxs = sqrt((xs[,13][i] - xs[,12][i])^2 + (ys[,13][i] - ys[,12][i])^2)
        t = lThigh/lThighPxs        
        massThigh = 18.6*(lThigh/0.36) ## lThigh is not in meters!
        xThigh = xs[,12][i]*t + (-0.12)*lThigh
        yThigh = ys[,12][i]*t + (0.59)*lThigh
        if(is.null(thigh)){
            thigh <- data.frame(lThigh = lThigh, massThigh = massThigh, xThigh = xThigh, yThigh = yThigh)
        } else {
            thigh[i,] <- c(lThigh, massThigh, xThigh, yThigh)
        }
        
        ## Crus (14-15)
        lCrus = 0.54
        lCrusPxs = sqrt((xs[,14][i] - xs[,13][i])^2 + (ys[,14][i] - ys[,13][i])^2)
        t = lCrus/lCrusPxs
        massCrus = 18.53*lCrus + 0.242
        xCrus = xs[,13][i]*t + (-0.084)*lCrus
        yCrus = ys[,13][i]*t + (0.379)*lCrus
        if(is.null(crus)){
            crus <- data.frame(lCrus = lCrus, massCrus = massCrus, xCrus = xCrus, yCrus = yCrus)
        } else {
            crus[i,] <- c(lCrus, massCrus, xCrus, yCrus)
        }
        
        ## Metatarsus (15-16)
        lMetatarsus = 0.37
        lMetatarsusPxs = sqrt((xs[,15][i] - xs[,14][i])^2 + (ys[,15][i] - ys[,14][i])^2)
        t = lMetatarsus/lMetatarsusPxs
        massMetatrs = 5.753*lMetatarsus + 0.812
        xMetatrs = xs[,14][i]*t + (-0.067)*lMetatarsus
        yMetatrs = ys[,14][i]*t + (0.32)*lMetatarsus
        if(is.null(metatarsus)){
            metatarsus <- data.frame(lMetatarsus = lMetatarsus, massMetatrs = massMetatrs, xMetatrs = xMetatrs, yMetatrs = yMetatrs)
        } else {
            metatarsus[i,] <- c(lMetatarsus, massMetatrs, xMetatrs, yMetatrs)
        }
        
        ## Digit Hindlimb (16-17)
        lDigitH = 0.17
        lDigitHPxs = sqrt((xs[,16][i] - xs[,15][i])^2 + (ys[,16][i] - ys[,15][i])^2)
        t = lDigitH/lDigitHPxs
        #massDigitH = 0.00254*massExpected + 0.504
        massDigitH = (1.87*lDigitH)/0.135
        xDigitH = xs[,15][i]*t + 0.92*lDigitH
        yDigitH = ys[,15][i]*t + (-0.18)*lDigitH
        if(is.null(digith)){
            digith <- data.frame(lDigitH = lDigitH, massDigitH = massDigitH, xDigitH = xDigitH, yDigitH = yDigitH)
        } else {
            digith[i,] <- c(lDigitH, massDigitH, xDigitH, yDigitH)
        }
        
        massTotal = massHead + massTail + massTrunk + massNeck + massScapula + massBrachium + massAntBrach + massMetacps + massDigitF + massThigh + massCrus + massMetatrs + massDigitH
        
        xBCM = (xHead*massHead + xTail*massTail + xTrunk*massTrunk + xNeck*massNeck + xScapula*massScapula + xBrachium*massBrachium + xAntBrach*massAntBrach + xMetacarpus*massMetacps + xDigitF*massDigitF + xThigh*massThigh + xCrus*massCrus + xMetatrs*massMetatrs + xDigitH*massDigitH)/massTotal
        
        yBCM = (yHead*massHead + yTail*massTail + yTrunk*massTrunk + yNeck*massNeck + yScapula*massScapula + yBrachium*massBrachium + yAntBrach*massAntBrach + yMetacarpus*massMetacps + yDigitF*massDigitF + yThigh*massThigh + yCrus*massCrus + yMetatrs*massMetatrs + yDigitH*massDigitH)/massTotal
        
        massError = massExpected - massTotal
        
        if(is.null(massCentreData)){
            massCentreData <- data.frame(xBCM = xBCM, yBCM = yBCM, massTotal = massTotal, massError = massError)
        } else {
            massCentreData[i,] <- c(xBCM, yBCM, massTotal, massError)
        }
    }
    massCentreData <- cbind(massCentreData, head, neck, trunk, tail, scapula, brachium, antebrachium, metacarpus, digitf, thigh, crus, metatarsus, digith)
    
    massCentreData 
}

plot(lowess(x = mcData$xBCM,y = mcData$yBCM,f = 0.05),type = 'l',ylim = c(0,8))

plot(x = mcData$xBCM, y = mcData$yBCM, ylim = c(0,8))

plot(x = mcData$xBCM, y = mcData$yBCM)