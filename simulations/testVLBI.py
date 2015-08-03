import numpy, pylab

a=numpy.random.normal(1,1,100000)
b=a[50000:51000]
c=a[0000:1000]


accumulationLength=1000

nAccumulations = len(a)/(accumulationLength)-1
detectorVals=numpy.zeros(nAccumulations)

for i in range(0,nAccumulations):
	indexStart = i*accumulationLength	
	indexEnd = i*accumulationLength + accumulationLength
	c=a[indexStart:indexEnd]
	dd=b*c
	detectorVals[i]=numpy.mean(dd)	


pylab.plot(detectorVals)

