import pandas as pd
# Create a DataFrame from List
student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
data = pd.DataFrame(student_data, columns=["student_id", "age"], index=None)
print(data)

# -------------------------------------------------------
# Size of the Dataframe
print(data.shape)

# -------------------------------------------------------
# Select Data from dataframe

students.loc[students["student_id"] == 101, ['name', 'age']]
# name and age columns specifically and filtering on student_id

# -------------------------------------------------------
# Display first 3 head
employees.head(3)

# -------------------------------------------------------
# Create a new column
employees['bonus'] = employees['salary'] * 2

# -------------------------------------------------------
# Remove duplicates
students.dropna(subset=["name"], inplace=True) # looking for NA only in the name column

# -------------------------------------------------------
# Change data type
students['grade'] = students['grade'].astype('int')

# -------------------------------------------------------
# Renaming columns
students.rename(columns = {
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    }, inplace=True)

# -------------------------------------------------------
# Drop missing data
students.dropna(subset=["name"], inplace=True)

# -------------------------------------------------------
# Fill missing data
values = {"quantity": 0} # 0 when quantity is None
products.fillna(value = values, inplace=True)

# -------------------------------------------------------
# Concat two dataframes end to end
pd.concat([df1, df2])

# -------------------------------------------------------
# Pivot table
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html
# pivot the data so that each row represents temperatures for a specific month, and each city is a separate column.
data = weather.pivot(index='month', columns='city', values='temperature')

# Melt dataframe
data = report.melt(
            id_vars=['product'], 
            value_vars=[
                    'quarter_1', 
                    'quarter_2', 
                    'quarter_3', 
                    'quarter_4'],
            var_name='quarter',
            value_name='sales'
            )







