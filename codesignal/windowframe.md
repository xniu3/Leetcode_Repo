4:
Given two integers maxRequests and windowFrame, and an array of integers requestTimestamps representing timestamps when requests arrive to a server, your task is to implement a simple request rate limiter.
When each request arrives, the request rate limiter will reject the request if the number of prior requests have already reached the maxRequests limit during the last windowFrame seconds, otherwise it will accept the request. Return an array of booleans to specify whether each request from requestTimestamps has been accepted true or rejected (false
All timestamps in the requestTimestamps array are given in seconds, and the array is sorted in ascending order.
Example

For maxRequests = 3, windowFrame = 5, and request ramestamps = [1, 2, 2, 2, 6, 12, 32, 33, 34, 37] , the output should be solution
the output should be solution 
(maxRequests, windowFrame,requestTimestamps) = [true, true, true, false, false, true, true, true, true, true]