# Load the necessary modules
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataframe
crashes = sns.load_dataset("car_crashes")
df = crashes.loc[range(5)]

# Intialize figure
f, ax = plt.subplots()

# Plot total crashes
sns.set_color_codes("pastel")
sns.barplot(x="total", y="abbrev", data=df,
            label="Total", color="b")

# Plot crashes related to speeding
sns.set_color_codes("muted")
sns.barplot(x="speeding", y="abbrev", data=df,
            label="Speeding-related", color="b")
# Set title
plt.title('Speeding-related automobile collisions', fontsize=20)

# Set legend
ax.legend(ncol=1, loc="lower right")
ax.set(xlim=(0, 28), ylabel="State",
       xlabel="Automobile collisions (per billion miles)")

# Save the image
# plt.savefig("stacked.png")

# Show the image
plt.show()