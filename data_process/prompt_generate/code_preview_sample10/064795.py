```python
import matplotlib.pyplot as plt  
import numpy as np  
from scipy.sparse import csr_matrix  

# Sample data  
in_shape = np.array((4, 5), dtype=np.int64)  
kernel_shape = np.array((3, 3), dtype=np.int64)  
strides = np.array((2, 2), dtype=np.int64)  
padding = np.array((1, 1), dtype=np.int64)  

# Create a sparse matrix  
indices = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  
splits = np.array([0, 3, 6, 9, 10])  
values = np.ones_like(indices)  
mat = csr_matrix((values, indices, splits))  

# Plot the sparse matrix  
plt.figure(figsize=(6.0, 4.0))  
plt.spy(mat)  
plt.show()
```