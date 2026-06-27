class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_data = {"".join(sorted(key)): [] for key in strs}
        for str in strs:
            grouped_data["".join(sorted(str))].append(str)
        return list(grouped_data.values())