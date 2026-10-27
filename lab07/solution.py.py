import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    kolv = np.asarray(values, dtype=float)
    if width <= 0 or kolv.size % width != 0:
        return []
    return kolv.reshape(-1, width).tolist()

def block(matrix: list[list[float]],rows: list[int],columns: list[int]) -> list[list[float]]:
    kolv = np.asarray(matrix, dtype=float)
    if kolv.size == 0:
        return []
    return kolv[np.ix_(rows, columns)].tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    kolv = np.asarray(matrix, dtype=float)
    if kolv.size == 0:
        return []
    return np.round(kolv.mean(axis=0), 6).tolist()

def column_range(matrix: list[list[float]], column: int) -> float:
    kolv = np.asarray(matrix, dtype=float)
    if kolv.size == 0:
        return 0.0
    return round(float(np.ptp(kolv[:, column])), 6)

