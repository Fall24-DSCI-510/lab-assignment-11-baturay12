# Solution code for the Iris Dataset Homework (run.py)

import pandas as pd
from scipy.stats import zscore

# Question 1: Pre-process the data
def preprocess_data(input_filename):
    iris = pd.read_csv(input_filename, header = None, names = ['SepalLengthcm', 'SepalWidthcm', 'PetalLengthcm', 'PetalWidthcm', 'Species'])

    # Calculate z-scores for SepalLengthCm and SepalWidthCm
    iris['SepalLengthCm_z'] = zscore(iris['SepalLengthcm'])
    iris['SepalWidthCm_z'] = zscore(iris['SepalWidthcm'])

    # Remove z-scores less than -2 or greater than 2
    filtered_iris = iris[(iris['SepalLengthCm_z'] > -2) & 
                     (iris['SepalLengthCm_z'] < 2) & 
                     (iris['SepalWidthCm_z'] > -2) &  
                     (iris['SepalWidthCm_z'] < 2)]

    # Create new 'ID' column
    filtered_iris['ID'] = range(1, filtered_iris.shape[0]+1)
    
    return filtered_iris



# Question 2: Descriptive Statistics Functions
def species_count(data):
    pass 

def average_sepal_length(data):
    pass

def max_petal_width(data):
    pass

def min_petal_length(data):
    pass

def count_sepal_length_above_5(data):
    pass

# Question 3: Analysis Functions
def count_petal_length_below_2(data):
    pass

def get_sepal_width_above_3_5(data):
    pass

def species_count_petal_width_above_1_5(data):
    pass

def get_virginica_petal_length_above_6(data):
    pass
    
def get_largest_sepal_width(data):
    pass

