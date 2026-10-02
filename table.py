import matplotlib.pyplot as plt

subjects = ["Math", "English", "Science", "ICT"]
marks = [75, 82, 68, 90]

data = list(zip(subjects, marks))

fig, ax = plt.subplots()

ax.table(
    cellText=data,
    colLabels=["Subject", "Marks"],
    loc="center"
)

ax.axis("off")
ax.set_title("Student Marks")

plt.show()