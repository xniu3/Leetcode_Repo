A user is uploading a big file to your server. The upload is done by sending file chunks of consecutive byte ranges, and the byte ranges for all chunks are represented as a two-dimensional array chunks. For each chunk chunks[i], the byte range is stored in an array of two 64-bit integers: chunks[i][0] is the index of the leftmost byte in the ith chunk, and chunks[i][1] is the index of the rightmost byte in the ith chunk (both indices are inclusive, 1-based).
Your task is to determine the total number of bytes (of the overall file) received after each file chunk is received. Note that chunks may intersect or even fully replicate the previous ones - i.e., sending the same data twice.
Example
For chunks = [[1, 1], [2, 2], [3, 3]], the output should be solution(chunks) = [1, 2, 3].
The first chunk only contains the byte 1, so the total number of bytes received becomes 1 after this chunk.
The second chunk only contains the byte 2, so the total number of bytes received becomes 2 after this chunk.
The third chunk only contains the byte 3, so the total number of bytes received becomes 3 after this chunk.
Expand to see the example video.
For chunks = [[1, 1], [2, 2], [3, 5]], the output should be solution(chunks) = [1, 2, 5].
The first chunk only contains the byte 1, so the total number of bytes received becomes 1 after this chunk.
The second chunk only contains the byte 2, so the total number of bytes received becomes 2 after think chunk.
The third chunk contains bytes from 3 to 5, so the total number of bytes received becomes 5 after this chunk (from 1 to 5).
Expand to see the example video.
For chunks = [[1, 9], [1, 3], [8, 15], [6, 9], [2, 5]], the output should be solution(chunks) = [9, 9, 15, 15, 15].
The first chunk contains bytes from 1 to 9, so the total number of bytes received becomes 9.
The second chunk does not add new data, so the total number of bytes received does not change after this chunk.
The third chunk contains bytes from 8 to 15, so the total number of bytes received becomes 15 after this chunk (from 1 to 15).
The rest of the chunks contain bytes that were already received, so none of them change the total number of bytes received.
Expand to see the example video.
For chunks = [[7, 9], [1, 3], [8, 15], [6, 9], [2, 4]], the output should be solution(chunks) = [3, 6, 12, 13, 14].
Expand to see the example video.
Input/Output
[execution time limit] 0.5 seconds (cpp)
[input] array.array.integer64 chunks
An array of arrays, each of which represents the indices of the leftmost and rightmost bytes contained in each file chunk.
Guaranteed constraints:
1 ≤ chunks.length ≤ 1000,
chunks[i].length = 2,
1 ≤ chunks[i][0] ≤ chunks[i][1] ≤ 1012.
[output] array.integer64
An array of integers, each of which represents the cumulative total number of bytes received after each file chunk.