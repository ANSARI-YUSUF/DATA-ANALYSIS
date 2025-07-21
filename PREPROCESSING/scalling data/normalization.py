from sklearn.preprocessing import Normalizer
import numpy as np

data = np.array([
    [4, 1, 2],
    [1, 3, 9],
    [2, 6, 1]
])

normalizer = Normalizer(norm='l2')  # 'l1' and 'max' norms also available
normalized_data = normalizer.fit_transform(data)

print(normalized_data)
