class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def getNames(self):
        return self.name, self.surname


class Student(Person):
    def __init__(self, name, surname, subject):
        super().__init__(name,surname)
        self.subject = subject
        
    def getSubject(self):
        return self.subject 


axel = Person("Axel", "Cederholm")


student = Student("Axel", "Cederholm", "medicine")


print(student.getNames())


print(student.getSubject())


#### Dag3 part 2. Numpy excercises
import numpy as np

#a. Create a null vector of size 10 but the fifth value which is 1
tom_vector = np.empty(10)
tom_vector[4] = 1
print(tom_vector)
#b. Create a vector with values ranging from 10 to 49
tenthirtyinine_vector = np.arange(10,50)
print(tenthirtyinine_vector)
#c. Reverse a vector (first element becomes last)
print(np.flip(tenthirtyinine_vector))
#d. Create a 3x3 matrix with values ranging from 0 to 8
testmatrix = np.arange(9).reshape(3, 3)
print(testmatrix)
#e. Find indices of non-zero elements from [1,2,0,0,4,0]
print(np.nonzero([1,2,0,0,4,0]))
#f. Create a random vector of size 30 and find the mean value
print(np.mean(np.random.rand(30)))
#g. Create a 2d array with 1 on the border and 0 inside
array2d_insidan_som_raknas = np.zeros((3, 3))
array2d_insidan_som_raknas[0, :] = 1
array2d_insidan_som_raknas[-1, :] = 1
array2d_insidan_som_raknas[:, 0] = 1
array2d_insidan_som_raknas[:, -1] = 1
print(array2d_insidan_som_raknas)
#h. Create a 8x8 matrix and fill it with a checkerboard pattern
schackdags = np.zeros((8, 8), dtype=int)
schackdags[::2, ::2] = 1
schackdags[1::2, 1::2] = 1
print(schackdags)
#i. Create a checkerboard 8x8 matrix using the tile function
#The line below is borrowed from https://python.pages.doc.ic.ac.uk/2021/lessons/numpy/08-summary/06-checkerboard.html
print(np.array(np.tile(np.eye(2) == 0, (4, 4)), dtype=int))
#j. Given a 1D array, negate all elements which are between 3 and 8, in place
Z = np.arange(11)
Z[3:9] = -Z[3:9]
print(Z)
#k. Create a random vector of size 10 and sort it
Z = np.random.random(10)
Z = np.sort(Z)
print(Z)
#l. Consider two random array A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A, B)
print(equal)
#m. How to convert an integer (32 bits) array into a float (32 bits) in place?
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = np.float32(Z)
print(Z.dtype)
#n. How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diagonal(C)
print(D)

##3. Revisit the matmult.py example from yesterday and improve its performance using Numpy.

#4. MPI parallelization a + b

#5. GPU Computing



