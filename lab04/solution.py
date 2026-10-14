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
    index = list(range(len(names)))
    index.sort(key=lambda i: scores[i], reverse=True)
    return [names[i] for i in index]

def above_average(names: list[str], scores: list[float]) -> list[str]:
    bolwe = average(scores)
    result = []
    for i in range(len(names)):
        if scores[i] > bolwe:
            result.append(names[i])    
    return result

