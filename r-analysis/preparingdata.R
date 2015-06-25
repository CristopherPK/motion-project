preparingData <- function(path = "tracks"){
    tracksFile <- list.files(path = path, full.names = TRUE)
    
    xs <- NULL
    ys <- NULL
    
    #Pixels to meters.
    pxtomts <- 0.0038143092291382
    
    for (t in tracksFile){
        dt <- read.table(file = t, dec=",")
        if(is.null(xs)){
            xs <- data.frame(dt$V2*pxtomts)
            ys <- data.frame(dt$V3*pxtomts)
        } else {
            xs <- cbind(xs, dt$V2*pxtomts)
            ys <- cbind(ys, dt$V3*pxtomts)
        }
    }
    
    names(xs) <- c(1:16)
    names(ys) <- c(1:16)
    
    tracks <- list(xs, ys)
    tracks
}