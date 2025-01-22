```python
import numpy as np  
import matplotlib.pyplot as plt  

# Define levels
level1 = 200
level2 = 0
level3 = 600
level4 = 1200

# Create message
message = []
for w in range(2000):
    if w < 401:
        message.append(level1)
    elif 400 < w < 801:
        message.append(level2)
    elif 800 < w < 1201:
        message.append(level3)
    elif 1200 < w < 1601:
        message.append(level1)
    elif 1600 < w < 2001:
        message.append(level4)

# Create x values
x = np.arange(-100, 100, 0.1)

# Create modulated signal
m = []
f1 = np.sin(x * 0.8) * 1200
f2 = np.sin(x * 0.2) * 1200
f3 = np.sin(x * 1.5) * 1200
f4 = np.sin(x * 2.5) * 1200

i = 0
for w in message:
    if w == level1:
        v = f1[i]
    elif w == level2:
        v = f2[i]
    elif w == level3:
        v = f3[i]
    else:
        v = f4[i]
    m.append(v)
    i += 1

# Plot
plt.figure(figsize=(7.0, 5.0))
plt.scatter(x, message, label="Message", color='r')
plt.plot(x, m, label="Modulated Signal")
plt.legend()
plt.title('MFSK')
plt.xlabel('Time')
plt.ylabel('Modulated Signal')
plt.show()
```