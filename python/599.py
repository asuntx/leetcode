from typing import Dict, List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set1, set2 = set(list1), set(list2)
        intersection = set1.intersection(set2)
        if len(intersection) == 1:
            return list(intersection)
        common: Dict[str, int] = {}
        for i in range(len(list1)):
            if list1[i] in intersection and list1[i] not in common:
                common[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in intersection:
                common[list2[j]] += j
        return [key for key in common.keys() if common[key] == min(common.values())]


sol = Solution()
print(
    sol.findRestaurant(
        list1=["happy", "sad", "good"],
        list2=["sad", "happy", "good"],
    )
)
