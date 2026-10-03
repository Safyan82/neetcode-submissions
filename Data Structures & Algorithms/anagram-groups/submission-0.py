class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = Counter(s)
            # frozenset of (char, count) pairs is hashable and order-independent
            key = frozenset(count.items())
            groups[key].append(s)

        return list(groups.values())
        