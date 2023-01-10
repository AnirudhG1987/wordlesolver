def maximumScore( scores, edges) -> int:
    def helper(x):
        return x[0]

    scores_edge = sorted([(x, i) for i, x in enumerate(l)], reverse=True, key=helper)
    best_path = {}
    for val, index in scores_edge:
        pass
    return 0

scores = [5, 2, 9, 8, 4]
edges = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
scores_path ={}
for item in edges:
    val1=scores[item[0]]
    val2=scores[item[1]]
    scores_path[val1]=scores_path.get(val1,[])
    scores_path[val1].append(val2)
    scores_path[val2] = scores_path.get(val2, [])
    scores_path[val2].append(val1)
max_value =-1
for key in scores_path.keys():
    x,y = get_max(scores_path[key])
    local_max_value=key+get_sum(scores_path[key])
    if local_max_value>max_value:
        max_value=local_max_value
print(scores_path)
print(max_value)

#maximumScore(scores,edges)