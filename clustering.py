# package init
def group_documents(similarity_matrix, threshold=0.8):
    N = len(similarity_matrix)
    visited = [False] * N
    groups = []

    def dfs(idx, group):
        visited[idx] = True
        group.append(idx)
        for j in range(N):
            if not visited[j] and similarity_matrix[idx][j] >= threshold:
                dfs(j, group)

    for i in range(N):
        if not visited[i]:
            group = []
            dfs(i, group)
            groups.append(group)

    return groups
