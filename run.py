# Solution code for the Iris Dataset Homework (run.py)

import pandas as pd
from scipy.stats import zscore

# Question 1: Pre-process the data
def preprocess_data(input_filename):
    iris = pd.read_csv(input_filename, header = None, names = ['SepalLengthcm', 'SepalWidthcm', 'PetalLengthcm', 'PetalWidthcm', 'Species'])

    # Calculate z-scores for SepalLengthCm and SepalWidthCm
    iris['SepalLengthCm_z'] = zscore(iris['SepalLengthCm'])
    iris['SepalWidthCm_z'] = zscore(iris['SepalWidthCm'])

    # Remove z-scores less than -2 or greater than 2
    filtered_iris = iris[(iris['SepalLengthCm_z'] > -2) & 
                     (iris['SepalLengthCm_z'] < 2) & 
                     (iris['SepalWidthCm_z'] > -2) &  
                     (input_firisilename['SepalWidthCm_z'] < 2)]

    # Create new 'ID' column
    filtered_iris['ID'] = range(1, filtered_iris.shape[0]+1)
    
    return filtered_iris



# Question 2: Descriptive Statistics Functions
def species_count(data):
    filtered_data = preprocess_data(data)
    return filtered_data.value_counts('Species').to_dict() 

def average_sepal_length(data):
    filtered_data = preprocess_data(data)
    return float(round(filtered_data['SepalLengthCm'].mean(), 1))

def max_petal_width(data):
    filtered_data = preprocess_data(data)
    return float(round(filtered_data['PetalWidthCm'].max(), 1))

def min_petal_length(data):
    filtered_data = preprocess_data(data)
    return float(round(filtered_data['PetalLengthCm'].min(), 1))

def count_sepal_length_above_5(data):
    filtered_data = preprocess_data(data)
    return filtered_data[filtered_data['SepalLengthCm'] > 5].shape[0]

# Question 3: Analysis Functions
def count_petal_length_below_2(data):
    filtered_data = preprocess_data(data)
    return filtered_data[filtered_data['PetalLengthCm'] < 2].shape[0]

def get_sepal_width_above_3_5(data):
    filtered_data = preprocess_data(data)
    filtered_data2 = filtered_data[filtered_data['SepalWidthCm'] > 3.5]
    return filtered_data2['ID'].sort_values(ascending = True).tolist()

def species_count_petal_width_above_1_5(data):
    filtered_data = preprocess_data(data)
    filtered_data2 = filtered_data[filtered_data['PetalWidthCm'] > 1.5]
    # Call previously defined species_count function
    return filtered_data2.value_counts('Species').to_dict()

def get_virginica_petal_length_above_6(data):
    filtered_data = preprocess_data(data)
    filtered_data2 = filtered_data[(filtered_data['PetalLengthCm'] > 6) & (filtered_data['Species'] == 'Iris-virginica')]
    return filtered_data2['ID'].sort_values(ascending = True).tolist()
    
def get_largest_sepal_width(data):
    pass

