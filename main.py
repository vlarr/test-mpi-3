from mpi4py import MPI
from my_lib import calc_PI
from my_lib import calc_PI_2

comm_current = MPI.COMM_WORLD
rank_current = comm_current.Get_rank()
rank_size_current = comm_current.Get_size()
if rank_size_current > 1:
    print('Master must run in 1 thread')
    exit(1)

calc_PI(1)

calc_PI(3)

calc_PI_2(5)
