title: Experimenting with maps in R
category: post
date:   2016-04-07 04:47:56
tags: java, processing, maps, mapzen, vertor-tiles
slug:maps-with-r
status:published


I guess you all know [Processing](http://processing.org/) and what it can do. Recently i came across with the [phd thesis](http://benfry.com/phd/) of one of its creators and i saw this picture on page 34, “Psychology of Pereception” chapter.

![france]({filename}/images/france.jpg )

combined with these words:

> Reading the left-hand image requires the viewer to search the image for the lowest and highest values, and the short-term memorization of the general layout of the numbers. On the right, a qualitative > > understanding of the image is immediately conveyed—that something is important in the Northwest corner, and to a lesser extent in a small region on the
Eastern edge. This information is conveyed without any active viewing, meaning that it is “pre-attentive.” The term is assigned to objects that are processed faster than 10 milliseconds; as compared to non-pre-attentive features requiring 40 milliseconds or more [Triesman, 1988 via Ware, 2000]


Very interesting but how do i do something like this? First step just find some data and experiment. At first i wanted to try with processing but then i thought that R might be more appropriate since i can handle shapefiles (.shp) easier with R rather in Java. I do not know how this map was created or which is the correct way to do it so i had to figure something out. Morever, i wanted to experiment with an area that i am familiar with, so i went for these two datasets, Polygons and Points that are available for free (this is a small area from Thessaloniki,Greece). I used the shp format.

Just plotting these two together with the [maptools](https://cran.r-project.org/web/packages/maptools/index.html) library you get something like this

![ok]({filename}/images/first.png)


and if i zoom in

![zoomed]( {filename}/images/firstzoomed.png )

that looks great! Exactly what i wanted. The polygons are the building and the red dots indicate how may entrances the buildings have, let`s say they are large building blocks with adjacent buildings building and more dots mean that more people live there. So i will try to visualize this.

My first thought was:”Just fill this plot with dots (create a grid) and then if any of these dots are inside the polygons,plot them.”

So i create the grid and plot it over the polygons while leaving the Points shapefile out just for now

    #!R
    #first get the bounding box
    bbox<-(expand.grid(as.vector(polygons@bbox[1,]),as.vector(polygons@bbox[2,])))
    bottom.left<-c(bbox$Var1[1],bbox$Var2[1])
    bottom.right<-c(bbox$Var1[2],bbox$Var2[2])
    top.left<-c(bbox$Var1[3],bbox$Var2[3])
    top.right<-c(bbox$Var1[4],bbox$Var2[4])
    total.number.of.points<-110
    xx.horizontal<-seq(bottom.left[1],bottom.right[1],length.out=total.number.of.points)
    xx.vertical<-seq(bottom.left[2],bottom.right[2],length.out=total.number.of.points)
    yy.horizontal<-seq(bottom.left[1],top.left[1],by=abs(xx.horizontal[1]-xx.horizontal[2]))
    yy.vertical<-seq(bottom.left[2],top.left[2],by=abs(xx.horizontal[1]-xx.horizontal[2]))
    final.grid<-(expand.grid(xx.horizontal,yy.vertical))



i know, really bad names but you get the point.

![firstwithgrid]({filename}/images/firstwithgrid.png)

Next keep only the points that are inside any polygon. This one is a bit tricky since SpatialDataFrame does not allow you to create a new column, so i copy it to apply the over() function and create the new column to the original final.grid data frame.

    #!R
    #create SpatialDataFrame to apply over() function
    names(final.grid)<-c("longitude","latitude")
    temp<-final.grid
    coordinates(temp)<-c("longitude","latitude")
    final.grid$polygon<-over(temp,polygons)$AROT
    final.grid<-final.grid[which(!is.na(final.grid$polygon)),]


After that, we have to count how many points (addresses) each polygon has, so we have to use the over() function again and assign the count to cex paramater on the final plot.

    #!R
    ad.points<-as.data.frame(coordinates(addresses))
    names(ad.points)<-c("longitude","latitude")
    coordinates(ad.points)<-c("longitude","latitude")
    ad.per.polygon<-as.data.frame(table(over(ad.points,polygons)))
    names(ad.per.polygon)<-c("polygon","count")
    mapValues<-function(value,istart,istop,ostart,ostop){
    return (ostart + (ostop - ostart) * ((value - istart) / (istop - istart)))

    }

    #match
    m<-match(final.grid$polygon,ad.per.polygon$polygon)
    final.grid$counts<-ad.per.polygon$count[m]
    final.grid$cex<-mapValues(final.grid$counts,min(final.grid$counts),max(final.grid$counts),.2,.7)
    brks<-cut(final.grid$counts,breaks=c(-1,2,15,41))
    final.grid$brks<-as.numeric(brks)

    plot.polygons<-function(){
    X11()
    plot(polygons,border=F,bg="#4F4F4F")
    points(final.grid$longitude,final.grid$latitude,cex=mapValues(final.grid$brks,1,3,.2,.7),pch=19,col="orange")
    }

    plot.polygons()

If you ever used processing then you are probably familiar with the [map()](https://processing.org/reference/map_.html) function which simply re-maps a number from one range to another, i.e. we need to map the number of points on each polygon between (0,1) for cex.

The final output looks something like this.I edited a bit in Inkscape,scaled down the size of the circles and removed the stroke on the exported pdf.


<img src="https://github.com/dimr/densityPolygons/raw/master/result.png?raw=true" width="760">

<!-- That looks pretty good (at least for me) having in mind that i was just experimenting. I guess there are better ways to do this and the code can be optimized but this can offer a start. I wonder how much better can it be with the ggplot2 package but i still haven`t dived into it yet. -->
That looks pretty good!

After achieving the visual result and making a lot of R scripts to break shapefiles according to attribute names the generated PDFs
where inserted to [inkscape](https://inkscape.org/en/) to create the final two page layout.


<img src="https://github.com/dimr/densityPolygons/raw/master/Kalamaria1.png" width="760">


<img src="https://github.com/dimr/densityPolygons/raw/master/Kalamaria2.png" width="760">
