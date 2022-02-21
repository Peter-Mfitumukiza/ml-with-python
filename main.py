import numpy
import pandas

df = pandas.read_csv("C:\\Users\\mfite\\OneDrive\\Documents\\salaryGender.csv", delimiter=',')
salary = numpy.array(df['Salary'])
gender = numpy.array(df['Gender'])
age = numpy.array(df['Age'])
phd = numpy.array(df['PhD'])
print("Mean: ")
print(df.mean())
print("Mode: ")
print(df.mode(axis=1))
