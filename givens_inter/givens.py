from ctypes import *
from numpy.ctypeslib import ndpointer

# On charge le module go compilé
lib = cdll.LoadLibrary("./givens.so")


pyarr = [1,2,3,4,5,6,7,8,9]  # Matrice à décomposer (en 1D)
rows = 3 # On précise les lignes
cols = 3 # les colonnes

# On précise les types des paramètres en entrées et sortie de la fonction QR sur Go 
lib.QR.argtypes = [c_double * len(pyarr)]
lib.QR.restype = ndpointer(dtype = c_double, shape = (2*len(pyarr),))

# Crée un C array à la base d'un py array 
arr = (c_double * len(pyarr))(*pyarr)
# qr_array est une liste à 1D qui contient R et Q
qr_array = lib.QR(arr, len(arr), rows, cols)

# On reconstruit les deux matrices grâce à qr_array
r = qr_array[0:rows * cols].reshape(rows, cols)
q = qr_array[rows * cols:].reshape(rows, cols)
print("R", r)
print("Q", q)
