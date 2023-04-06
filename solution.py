import pandas as pd
import numpy as np


chat_id = 465374385 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    total_count = np.sum(x)
    
    # Вычисляем оценку параметра lambda
    res = total_count / (56 * n)
    return res # Ваш ответ
