def winner(names: list[str], scores: list[float]) -> str:
    if not names or not scores:
        return ""
    max_score = max(scores)
    best_index = scores.index(max_score)
    return names[best_index]

def average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    res = sum(scores) / len(scores)
    return round(res, 2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    indices = list(range(len(names)))
    indices.sort(key=lambda i: scores[i], reverse=True)
    return [names[i] for i in indices]

def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg_score = average(scores)
    result = []
    for i in range(len(names)):
        if scores[i] > avg_score:
            result.append(names[i])    
    return result

