import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("students.csv")
data["Average"]=data[["Python","Java","C","Cyber security","Fronthend","Backend","Database"]].mean(axis=1)
top_student=data.loc[data["Average"].idxmax()]
print("------Top student-------\n")
print(top_student)
print(data)
data["Result"]=data["Average"].apply(lambda x: "Pass" if x>=60 else "Fail")

subjects=["Python","Java","C","Cyber security","Fronthend","Backend","Database"]
subject_average=data[subjects].mean()
print(subject_average)
plt.bar(subjects,subject_average)
plt.xlabel("Subjects")
plt.ylabel("Average")
plt.title("Subject-wise average")
plt.xticks(rotation=45)
plt.show()