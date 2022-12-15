import collections
def longestPath(parent: list[int], s: str):
    graph = collections.defaultdict(list)
    for i, par in enumerate(parent):
        graph[par].append(i)

    ans = 1
    def dfs(node):
        nonlocal ans
        longest = second_longest = 0

        for child in graph[node]:
            path_len = dfs(child)

            if s[child] != s[node]:
                if path_len > longest:
                    second_longest = longest
                    longest = path_len
                elif path_len > second_longest:
                    second_longest = path_len

        ans = max(ans, longest+second_longest+1)

        return longest + 1

    dfs(0)
    return ans