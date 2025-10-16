class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output =  [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            for i in range(3, numRows + 1):
                current = [0]*i
                current[0] = 1
                current[-1] = 1
                j = 1
                while current[j] != 1:
                    current[j] = output[i-2][j-1] + output[i-2][j]
                    j += 1
                output.append(current)
        return output
            
