# select all not null row
age_is_null = pd.isnull(titanic_survival["age"])
good_ages = titanic_survival["age"][age_is_null == False]
bad_ages = titanic_survival["age"][age_is_null]
correct_mean_age = sum(good_ages) / len(good_ages)

# drop rows or columns if it contains null
drop_na_rows = titanic_survival.dropna(axis=0)
drop_na_columns = titanic_survival.dropna(axis=1)
new_titanic_survival = titanic_survival.dropna(axis=0,subset=["age", "sex"])

# calculate the null count for each column
def null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null]
    return len(null)

column_null_count = titanic_survival.apply(null_count)
