from csv import reader
from math import sqrt


def load_csv(filename):
    file = open(filename,'r')
    dataset = list()
    lines = reader(file)
    for line in lines:
        if not line:
            continue
        dataset.append(list(line))
    return dataset


def str_column_to_float(dataset, column):
    for rows in dataset:
        rows[column] = float(rows[column].strip())
    return dataset


def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup

            
def dataset_minmax(dataset):
    data_minmax = list()
    for i in range(len(dataset[0])):
        column_values = list()
        for row in dataset:
            column_values.append(row[i])
        min_column = min(column_values)
        max_column = max(column_values)
        data_minmax.append([min_column, max_column])
    return data_minmax
                  


def normalize_dataset(dataset, dataset_minmax):
    for i in range(len(dataset[0])):
        for row in dataset:
            row[i] = (row[i]-dataset_minmax[i][0])/(dataset_minmax[i][1]- dataset_minmax[i][0])
    

def mean_of_columns(dataset):
    means = [0 for i in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        column_values = [row[i] for row in dataset]
        means[i] = sum(column_values)/len(dataset)
    return means


def column_stdevs(dataset, means):
    stdevs = [0 for i in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        variance = [pow(row[i]- means[i], 2) for row in dataset]
        stdevs[i] = sum(variance)
        stdevs = [sqrt(x/float(len(dataset)-1)) for x in stdevs] 
    return stdevs


def standardize_dataset(dataset, means, std):
    for i in range(len(dataset[0])):
        standardize_dataset = [(row[i]-means[i]/std[i]) for row in dataset]
    return standardize_dataset



# Load pima-indians-diabetes dataset
filename =  'pima-indians-diabetes.csv'
dataset = load_csv(filename)
print( ' Loaded data file {0} with {1} rows and {2} columns ' .format(filename, len(dataset),len(dataset[0])))
# convert string columns to float
for i in range(len(dataset[0])):
    str_column_to_float(dataset, i)
print(dataset[0])
# Estimate mean and standard deviation
means = mean_of_columns(dataset)
stdevs = column_stdevs(dataset, means)
# standardize dataset
standardize_dataset(dataset, means, stdevs)
print(dataset[0])

print('Test')


# filename = 'pima-indians-diabetes.csv'
# iris_filename = 'iris.csv'

# dataset = load_csv(filename)

# for i in range(len(dataset[0])):
#     str_column_to_float(dataset,i)
# normalize_dataset(dataset, dataset_minmax(dataset))


# print(dataset[1])

# irisdata = load_csv(iris_filename)

# irisdata.pop()

# print(irisdata)

# print(irisdata[0])

# print('this file has {0} rows and has {1} column'.format(len(irisdata),len(irisdata[0])))


# for i in range(len(dataset[0])):
#     str_column_to_float(dataset, i)

# print(dataset[0])

# str_column_to_int(irisdata,4)

# print(irisdata)
