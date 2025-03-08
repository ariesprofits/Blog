import numpy as np
import pandas as pd

def parabolic_sar(high, low, acceleration_factor=0.02, max_acceleration=0.2):
    sar = np.zeros(len(high))
    af = acceleration_factor
    ep = high[0]
    trend = 1 if high[1] > high[0] else -1
    sar[0] = low[0] if trend == 1 else high[0]

    for i in range(1, len(high)):
        sar[i] = sar[i - 1] + af * (ep - sar[i - 1])

        if trend == 1:
            if high[i] > ep:
                ep = high[i]
                af = min(af + acceleration_factor, max_acceleration)
            if sar[i] > low[i]:
                trend = -1
                sar[i] = ep
                ep = low[i]
                af = acceleration_factor
        else:
            if low[i] < ep:
                ep = low[i]
                af = min(af + acceleration_factor, max_acceleration)
            if sar[i] < high[i]:
                trend = 1
                sar[i] = ep
                ep = high[i]
                af = acceleration_factor

    return sar


data = {
    "High": [10, 11, 12, 11, 13, 14, 13, 15, 16, 17],
    "Low": [8, 9, 9.5, 9, 10, 11, 10.5, 12, 13, 14]
}
df = pd.DataFrame(data)
df["PSAR"] = parabolic_sar(df["High"].values, df["Low"].values)
print(df)