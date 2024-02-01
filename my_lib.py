from mpi4py import MPI
import numpy
import sys


def calc_PI(max_process_num):
    print('call calc_PI. max_process_num=', max_process_num)
    comm = MPI.COMM_SELF.Spawn(sys.executable, args=['child_mpi.py', 'my_arg_1', 'my_arg_2'], maxprocs=max_process_num)

    N = numpy.array(100, 'i')
    comm.Bcast([N, MPI.INT], root=MPI.ROOT)
    PI = numpy.array(0.0, 'd')
    comm.Reduce(None, [PI, MPI.DOUBLE], op=MPI.SUM, root=MPI.ROOT)
    print(PI)

    comm.Disconnect()


def calc_PI_2(max_process_num):
    print('call calc_PI_2. max_process_num=', max_process_num)
    comm = MPI.COMM_SELF.Spawn_multiple([sys.executable, sys.executable],
                                        args=[['child_mpi_2.py'], ['child_mpi_3.py', 'my_arg_3']],
                                        maxprocs=max_process_num)

    N = numpy.array(100, 'i')
    comm.Bcast([N, MPI.INT], root=MPI.ROOT)
    PI = numpy.array(0.0, 'd')
    comm.Reduce(None, [PI, MPI.DOUBLE], op=MPI.SUM, root=MPI.ROOT)
    print(PI)

    comm.Disconnect()
