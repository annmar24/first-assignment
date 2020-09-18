import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open('survey_results_public.csv', 'rb') as f:
    data1 = pd.read_csv(f, usecols=['Respondent', 'Hobbyist', 'YearsCodePro', 'WorkWeekHrs'], index_col='Respondent')

    #zad.4

    #delete rows with NaN values
    data1.dropna(inplace=True)
    print(data1.dtypes)
    column_values = data1[['YearsCodePro']].values.ravel()
    # Get unique values of 'YearsOfCode' column
    unique_values = pd.unique(column_values)
    print(unique_values)
    # Replace values which are not number
    data1.replace(to_replace={'Less than 1 year': '0', 'More than 50 years': '51'}, inplace=True)

    column_values = data1[['WorkWeekHrs']].values.ravel()
    # Get unique values of 'WorkWeekHrs' column
    unique_values = pd.unique(column_values)
    print(unique_values)

    # Convert values of columns YearsCodePro and WorkWeekHrs to int64 type
    data1 = data1.astype({'YearsCodePro': 'int64', 'WorkWeekHrs': 'int64'}, copy=False)

    print(data1.dtypes)

    #zad.5
    plt.plot(data1['YearsCodePro'], data1['WorkWeekHrs'], 'o', markersize=0.3)
    plt.xlabel('YearsCodePro')
    plt.ylabel('WorkWeekHrs')
    plt.show()

    column_values = data1[['Hobbyist']].values.ravel()
    unique_values = pd.unique(column_values)
    print(unique_values)

    first_group = data1[(data1['Hobbyist'] == 'Yes')]

    plt.plot(first_group['YearsCodePro'], first_group['WorkWeekHrs'], 'ro', markersize=0.3)
    plt.xlabel('YearsCodePro')
    plt.ylabel('WorkWeekHrs')
    plt.suptitle('Group - I code as a hobby ', fontsize=20)
    plt.show()

    second_group = data1[(data1['Hobbyist'] == 'No')]

    plt.plot(second_group['YearsCodePro'], second_group['WorkWeekHrs'], 'ko', markersize=0.3)
    plt.xlabel('YearsCodePro')
    plt.ylabel('WorkWeekHrs')
    plt.suptitle('Group - I don\'t code as a hobby', fontsize=20)
    plt.show()

