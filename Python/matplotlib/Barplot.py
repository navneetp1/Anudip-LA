# import numpy as np
# import matplotlib.pyplot as plt


# data = np.genfromtxt(r'C:\Python Programs\matplotlib\sales_data.xlsx', dtype=[("Empid", 'i4'), ('Empname', 'U50'), ('salary', 'i4')], encoding=None)

# print(data)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



data = pd.read_excel(r'C:\Python Programs\matplotlib\sales_data.xlsx')
colors = ["red","blue","green","yellow","orange"]

empid = data['Empid']
emparray = np.array(empid)

empname = data['Empname']
empnamearray = np.array(empname)

salary = data['salary']
empsalaryarray = np.array(salary)

barplot = plt.bar(empnamearray, empsalaryarray, color=colors)
plt.bar_label(barplot, labels=empsalaryarray, label_type="center")
plt.xlabel('Names')
plt.ylabel('Salary')
plt.title("Employee statistics")
plt.show()



