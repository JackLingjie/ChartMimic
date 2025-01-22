```python
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for demonstration
student_data = {
    'famrel': [1, 2, 3, 4, 5],
    'absences': [10, 8, 6, 4, 2]
}

# Create a point plot of family relationship vs. absences with caps and no lines joining points
sns.catplot(x="famrel", y="absences",
            data=student_data,
            kind="point",
            capsize=0.2,
            join=False)

# Set the figure size explicitly (not necessary here as `catplot` manages it internally)
plt.gcf().set_size_inches(6.0, 4.0)

# Show plot
plt.show()
```