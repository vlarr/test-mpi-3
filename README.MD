Пример программы MPI с динамическим количеством потоков (mpi4py, Spawn).

Запуск из папки с проектом:
```commandline
mpiexec -n 1 python main.py
```

Пример взят из:
https://mpi4py.readthedocs.io/en/stable/tutorial.html#dynamic-process-management 

* Python 3.11
* Microsoft MPI 10.1.1. [(link)](https://github.com/microsoft/Microsoft-MPI/releases/tag/v10.1.1)
* Пакеты: `numpy`, `mpi4py`