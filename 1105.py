import numpy as np

# 定義需要積分的函數
def integrand(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

# 1. 使用黎曼積分法
def riemann_sum_integral(N):
    dx = 1.0 / N
    dy = 1.0 / N
    dz = 1.0 / N
    result = 0.0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                x = (i + 0.5) * dx
                y = (j + 0.5) * dy
                z = (k + 0.5) * dz
                result += integrand(x, y, z) * dx * dy * dz
    return result

# 2. 使用蒙地卡羅法
def monte_carlo_integral(N):
    x_samples = np.random.uniform(0, 1, N)
    y_samples = np.random.uniform(0, 1, N)
    z_samples = np.random.uniform(0, 1, N)
    function_values = integrand(x_samples, y_samples, z_samples)
    volume = 1  # 單位立方體的體積
    return np.mean(function_values) * volume

# 設定樣本數與區間數
N_riemann = 100  # 黎曼法區間數
N_monte_carlo = 1000  # 蒙地卡羅法樣本數

# 計算積分
riemann_result = riemann_sum_integral(N_riemann)
monte_carlo_result = monte_carlo_integral(N_monte_carlo)

# 輸出結果
print(f"黎曼積分法結果 (N={N_riemann}): {riemann_result}")
print(f"蒙地卡羅法結果 (N={N_monte_carlo}): {monte_carlo_result}")
