class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l1 = []
        l2 = []
        for i in arr2:
            for j in arr1:
                if j == i:
                    l1.append(j)
        for i in arr1:
            if i not in arr2:
                l2.append(i)
        l2 = sorted(l2)
        return l1 + l2
