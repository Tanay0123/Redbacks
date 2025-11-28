# volumeList = list of 36 monthly volumes, including
# last 12 months prior to generic entry, and
# 24 months including and following generic entry. 
def AvgPrior(volumeList) : 
    for i in range(12) : 
        sumMonthsPrior += volumeList[i]
    return sumMonthsPrior / 12

def VolNorm(volumeList, monthNum) : 
    return volumeList[monthNum] / AvgPrior(volumeList)

def MeanGenericErosion(volumeList) :    
    # 13-36 to represent 24 months following generic entry.
    # 12 represents month of generic entry.
    for i in range (13, 36) : 
        GESum += VolNorm(volumeList, i)
    MGE = GESum / 24
    return MGE