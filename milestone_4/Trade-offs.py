def find_sum(target: int, li: list[int]) -> tuple[int, int]:
    # Time complexity: O(n^2) because we use two nested loops
    # Space complexity: O(1) because we do not use any extra space
    n = len(li)
    for i in range(n):
        for j in range(i + 1, n):
            if li[i] + li[j] == target:
                return (i, j)


assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}


def find_sum_fast(target: int, li: list[int]) -> tuple[int, int]:
    # Optimized approach: Use a dictionary to find complement
    # Time complexity: O(n) because we only traverse the list once
    # Space complexity: O(n) because we use extra space to store elements
    seen = {}
    for i, num in enumerate(li):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i


assert find_sum_fast(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}
