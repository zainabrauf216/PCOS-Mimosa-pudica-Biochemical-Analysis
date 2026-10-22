import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Group': ['Control', 'PCOS', 'PCOS+Mimosa 200mg', 'PCOS+Mimosa 400mg'],
    'Testosterone': [0.8, 2.5, 1.6, 1.1],
    'LH': [3.2, 8.5, 5.4, 4.1],
    'MDA': [1.2, 4.8, 2.9, 1.8],
    'SOD': [8.5, 3.2, 5.8, 7.6]
}
df = pd.DataFrame(data)
print(df)
print("Conclusion: Mimosa pudica restores hormonal and oxidative balance in PCOS")
