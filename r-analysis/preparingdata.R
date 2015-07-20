preparingData <- function(path = "tracks"){
    tracksFile <- list.files(path = path, full.names = TRUE)
    
    xs <- NULL
    ys <- NULL
    
    for (t in tracksFile){
        dt <- read.table(file = t, dec=",")
        if(is.null(xs)){
            xs <- data.frame(dt$V2)
            ys <- data.frame(dt$V3)
        } else {
            xs <- cbind(xs, dt$V2[1:nrow(xs)])
            ys <- cbind(ys, dt$V3[1:nrow(ys)])
        }
    }
    
    names(xs) <- c(1:16)
    names(ys) <- c(1:16)
    
    tracks <- list(xs, ys)
    tracks
}