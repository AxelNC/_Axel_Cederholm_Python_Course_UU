import mpi4py
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("Hi from process", rank)
MPI.Finalize()