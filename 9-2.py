import timeit, sys, time, random


data = [
[5,4,5,7,8,8,9,1,0,1,9,8,9,9,9,9,8,7,6,5,4,3,2,1,0,1,2,3,5,9,8,9,3,2,1,9,7,8,5,6,8,8,9,5,6,9,8,9,8,9,4,3,2,9,3,2,9,9,7,8,9,9,6,5,4,3,2,9,9,8,7,6,5,4,6,7,9,5,4,3,2,1,9,8,6,5,6,9,8,7,6,5,4,5,6,7,9,1,0,1,],[4,3,4,5,6,7,8,9,1,9,8,7,9,8,9,8,9,8,9,8,7,4,3,2,2,2,3,4,5,6,7,8,9,4,3,9,6,5,4,5,6,7,9,6,9,8,7,6,7,8,9,9,9,8,9,9,8,7,6,7,8,8,9,9,5,4,9,8,9,9,8,7,8,3,5,7,8,9,5,2,1,0,9,7,5,4,9,8,7,6,5,4,3,4,5,8,9,2,1,3,],[3,2,3,4,5,8,9,9,9,8,7,6,4,7,6,7,9,9,8,7,6,5,4,3,3,7,9,5,6,8,8,9,7,5,9,8,5,4,3,2,7,9,8,9,9,9,5,4,5,6,7,8,9,7,8,9,7,6,5,6,7,6,7,8,9,9,8,7,8,9,9,8,9,4,5,6,9,7,6,3,2,9,8,6,4,3,2,9,8,8,6,5,4,5,6,7,8,9,2,4,],[2,1,2,3,4,5,9,9,8,7,6,5,3,4,5,9,8,9,9,8,8,7,6,5,4,6,8,9,7,8,9,8,9,9,8,7,6,5,2,1,2,8,7,7,8,9,6,3,7,8,8,9,7,6,7,8,9,5,4,3,4,5,6,7,8,9,7,6,9,9,8,9,6,5,6,7,8,9,9,4,3,9,6,4,3,2,1,2,9,8,7,6,5,6,7,8,9,5,4,5,],[4,0,1,2,3,4,8,9,9,8,4,3,2,3,9,8,7,7,6,9,9,8,7,6,5,7,9,9,8,9,8,7,7,9,7,6,5,4,3,0,3,4,5,6,7,8,9,2,3,9,9,9,8,5,8,9,5,4,3,2,3,4,5,8,9,2,4,5,9,8,7,9,8,6,7,9,9,7,8,9,9,8,7,6,8,1,0,3,4,9,9,9,6,7,8,9,9,6,5,6,],[2,1,2,3,4,5,6,7,9,9,2,1,0,9,8,7,6,5,5,3,4,9,8,8,9,8,9,2,9,7,6,5,6,9,8,6,4,3,2,1,2,3,9,7,8,9,4,1,4,8,9,6,5,4,5,9,9,5,5,1,2,3,8,8,9,1,2,9,8,7,6,7,9,7,8,9,4,6,7,8,9,7,6,5,4,2,1,5,6,7,9,8,7,8,9,9,8,7,6,9,],[3,2,3,4,7,6,7,9,8,9,6,2,9,8,7,6,5,4,4,2,3,6,9,9,9,9,0,1,9,6,5,4,5,6,9,7,5,4,3,2,3,9,8,9,9,6,3,2,5,7,8,9,2,3,4,7,8,9,6,2,3,5,6,7,8,9,9,8,7,6,5,6,9,8,9,4,3,5,6,7,9,8,7,8,5,6,7,6,7,8,9,9,8,9,9,9,9,8,7,8,],[5,3,4,9,8,7,9,8,7,6,5,3,6,9,6,5,4,3,2,1,2,5,4,7,8,9,1,9,8,7,3,2,0,1,9,8,9,8,6,5,4,6,7,8,9,5,4,5,9,8,9,6,5,4,5,6,7,8,9,3,4,8,7,8,9,9,8,9,8,7,4,5,6,9,6,5,2,6,7,8,8,9,8,7,6,7,8,7,8,9,2,1,9,6,7,8,9,9,8,9,],[6,6,5,7,9,8,9,9,8,9,5,4,5,9,8,8,5,4,1,0,1,2,3,6,7,8,9,9,9,5,4,3,3,2,3,9,9,9,7,7,5,7,8,9,7,6,5,6,7,9,8,7,8,7,6,7,8,9,6,5,6,7,8,9,9,8,7,6,5,4,3,4,9,8,7,2,1,2,3,6,7,8,9,8,9,8,9,8,9,4,3,2,3,5,6,7,8,9,9,9,],[7,7,8,9,1,9,7,8,9,8,6,5,6,9,8,7,6,5,2,1,4,3,4,5,6,9,9,8,7,6,5,4,4,3,4,7,8,9,9,8,9,8,9,9,9,9,8,7,8,9,9,8,9,8,7,8,9,8,7,6,7,9,9,1,2,9,9,5,4,3,2,3,4,9,8,3,2,3,4,5,8,9,9,9,9,9,9,9,6,5,4,3,4,5,8,9,9,9,8,9,],[8,8,9,3,2,5,6,7,9,8,7,6,7,8,9,8,7,6,3,2,3,4,5,8,9,7,6,9,9,7,6,9,5,4,5,6,7,8,9,9,8,9,9,9,8,8,9,8,9,9,9,9,8,9,8,9,0,9,8,9,8,9,8,9,3,9,8,9,5,4,1,2,3,4,9,5,6,6,5,7,9,9,8,9,9,8,9,9,9,8,5,4,5,6,7,9,8,6,7,8,],[9,9,9,9,3,4,5,6,7,9,8,7,8,9,3,9,8,7,6,3,4,5,6,7,8,9,5,4,9,8,9,8,6,5,7,7,9,9,7,6,7,8,9,9,7,7,8,9,9,9,8,8,7,8,9,2,1,2,9,9,9,8,7,8,9,8,7,8,9,2,0,3,4,9,7,6,7,8,6,9,8,9,7,9,8,7,9,9,8,7,6,5,6,9,9,8,7,5,6,9,],[2,3,9,8,9,5,9,7,8,9,9,8,9,3,2,1,9,6,5,4,9,8,7,8,9,5,4,3,5,9,6,9,8,9,8,9,3,5,6,5,6,7,9,8,5,6,7,9,8,7,6,7,6,7,8,9,2,4,5,9,8,7,6,7,9,7,6,7,9,3,1,5,6,7,9,9,8,9,9,8,7,8,5,8,7,6,7,8,9,8,7,6,9,8,7,6,5,4,6,7,],[3,9,8,7,8,9,9,9,9,9,8,9,8,9,9,9,8,7,6,5,6,9,9,9,6,4,3,2,3,4,5,6,9,9,9,2,1,4,3,4,7,9,8,7,4,3,9,8,7,6,5,7,5,6,7,8,9,5,6,7,9,8,5,4,8,6,5,7,8,9,9,6,7,8,9,3,9,9,8,7,6,5,4,3,6,5,6,9,9,9,8,9,8,9,8,7,6,5,6,7,],[9,8,7,6,7,8,9,8,9,8,7,8,7,9,8,9,9,8,7,6,8,9,8,7,6,5,4,1,2,3,6,7,8,9,2,1,0,1,2,3,9,8,7,6,3,2,3,9,9,5,4,3,4,5,8,9,7,6,7,9,8,5,4,3,2,3,4,5,9,7,8,9,9,9,3,2,3,9,8,6,5,4,3,2,3,4,7,8,9,0,9,8,7,6,9,8,7,6,7,8,],[6,5,4,5,6,9,8,7,6,6,5,4,5,6,7,9,9,9,8,7,8,9,9,9,8,7,4,2,3,4,5,6,7,8,9,2,1,2,3,4,5,9,6,5,4,3,9,8,8,4,3,2,3,5,7,9,9,7,9,8,7,6,5,2,1,2,3,4,5,6,9,7,8,9,2,1,2,3,9,9,7,3,2,1,2,3,4,8,9,1,9,7,6,5,4,9,9,8,8,9,],[9,6,5,6,9,8,7,6,5,7,3,2,4,7,8,8,9,9,9,9,9,2,1,2,9,8,5,3,4,5,6,7,9,9,5,3,4,9,9,9,9,8,7,7,8,4,9,7,6,7,2,1,2,3,6,7,8,9,9,9,9,7,6,1,0,1,2,8,7,8,9,6,7,8,9,2,3,9,8,7,6,5,3,4,3,4,5,6,8,9,8,7,5,4,3,4,3,9,9,6,],[8,9,9,7,8,9,8,5,4,3,2,1,3,7,6,7,8,9,3,4,5,9,0,1,2,9,9,4,9,6,7,8,9,9,6,4,9,8,8,7,8,9,8,8,9,9,8,8,5,8,3,0,2,4,5,8,9,9,9,8,9,8,7,5,4,3,4,5,8,9,6,5,8,7,8,9,9,9,9,8,7,6,7,7,4,5,6,7,9,9,9,8,4,3,2,1,2,3,4,5,],[7,8,8,9,9,0,9,6,5,4,1,0,4,4,5,6,9,3,2,9,9,8,9,2,3,9,8,9,8,9,8,9,9,8,9,9,8,6,5,6,5,6,9,9,9,8,7,6,4,3,2,1,3,4,6,7,8,9,8,7,6,9,7,6,5,4,5,6,9,7,5,4,5,5,6,7,8,9,7,9,8,8,9,6,5,7,7,8,9,8,7,6,5,9,1,0,1,2,5,6,],[5,6,7,8,9,1,9,7,9,8,4,1,2,3,6,7,8,9,9,8,8,7,8,9,9,8,7,8,7,8,9,9,8,7,8,9,9,6,4,3,4,5,6,7,8,9,9,6,5,4,7,5,4,5,7,8,9,8,7,6,5,9,8,9,6,7,6,7,8,9,4,3,2,4,5,9,9,7,6,5,9,9,8,7,6,7,8,9,4,9,9,7,9,8,9,3,2,3,8,7,],[4,5,5,9,8,9,9,9,8,7,3,2,3,4,5,6,7,8,9,7,5,6,9,9,8,7,6,8,6,7,8,9,7,6,7,8,9,4,3,2,3,4,5,8,9,9,8,7,6,8,7,6,5,6,8,9,9,9,8,7,6,7,9,8,9,8,7,8,9,4,3,2,1,2,9,8,9,9,5,4,3,2,9,8,7,8,9,3,2,9,8,9,8,7,9,4,3,5,9,8,],[3,4,4,6,7,8,9,8,7,6,5,3,5,5,6,7,8,9,7,5,4,5,6,9,8,6,5,4,5,6,7,8,9,5,6,7,8,9,1,0,1,9,6,7,8,9,9,8,7,8,9,8,8,7,9,9,9,9,9,8,9,8,9,7,8,9,8,9,7,6,4,1,0,9,8,7,9,8,9,9,4,3,6,9,8,9,5,4,9,8,7,8,9,6,8,9,4,7,8,9,],[2,1,3,5,6,7,8,9,8,7,6,7,6,6,9,8,9,7,6,5,2,3,9,8,7,6,4,3,7,8,9,9,5,4,5,7,8,9,2,2,9,8,9,9,9,8,9,9,8,9,4,9,9,8,9,9,8,9,9,9,4,9,4,6,7,8,9,6,5,4,3,2,9,8,9,6,7,7,8,8,9,4,5,6,9,7,6,9,8,7,6,6,8,5,7,8,9,9,9,1,],[4,5,7,6,7,9,9,5,9,8,9,8,9,7,8,9,7,6,5,4,3,5,6,9,8,7,5,5,6,7,8,9,4,3,4,5,8,9,3,9,8,7,8,8,8,7,8,9,9,6,5,6,9,9,7,6,7,8,9,4,3,2,3,5,9,9,8,7,8,5,4,9,8,7,6,5,4,5,6,7,8,9,9,9,9,8,9,8,7,6,5,4,3,4,5,6,7,8,9,0,],[5,6,8,9,8,9,5,4,0,9,4,9,9,8,9,9,8,7,6,5,4,6,7,9,8,7,6,7,7,8,9,6,5,6,5,6,7,8,9,8,7,6,6,7,7,6,7,8,9,7,6,9,8,7,4,5,8,9,4,3,2,1,2,9,8,9,9,8,9,6,5,9,9,8,5,4,3,4,5,6,7,6,7,8,9,9,9,9,9,8,4,3,2,3,4,5,6,7,8,9,],[6,7,9,9,9,7,4,3,1,2,3,4,7,9,9,9,9,8,7,6,5,6,8,9,9,8,7,8,9,9,8,7,9,8,6,7,8,9,8,7,6,5,5,5,7,5,8,9,9,9,9,8,7,6,5,6,9,6,5,4,1,0,9,8,7,8,5,9,8,7,9,8,7,9,4,3,2,3,4,5,4,5,6,8,9,9,9,8,5,4,3,0,1,2,3,4,7,8,9,5,],[7,8,9,8,7,6,5,4,2,3,4,5,6,7,8,9,8,9,8,9,6,7,9,4,5,9,8,9,4,3,9,8,9,9,8,8,9,8,7,6,5,4,3,4,5,4,6,8,9,8,9,9,8,7,6,7,8,9,6,5,2,9,8,7,6,5,4,5,9,8,9,9,6,4,3,2,1,0,1,2,3,5,6,7,8,9,8,7,6,5,2,1,2,5,4,5,6,9,5,4,],[8,9,2,9,8,7,6,5,6,7,8,6,7,8,9,6,7,8,9,8,7,8,9,3,9,8,9,6,3,2,3,9,2,0,9,9,8,7,6,5,4,4,2,1,2,3,4,5,6,7,8,9,9,8,7,8,9,8,5,4,3,9,9,8,7,6,7,6,7,9,9,9,9,5,4,5,2,3,7,8,9,7,7,8,9,8,7,6,5,4,3,4,3,4,5,8,7,8,9,3,],[9,2,1,3,9,8,7,6,7,8,8,7,9,9,7,5,6,9,8,9,8,9,4,9,8,7,6,5,4,3,4,5,9,1,2,3,9,7,5,4,3,2,1,0,1,2,3,6,7,8,9,0,1,9,8,9,8,7,6,5,9,8,9,9,9,7,8,7,8,9,9,8,7,6,5,6,3,4,6,7,8,9,8,9,6,9,8,7,6,5,6,5,6,8,9,9,8,9,3,2,],[2,1,0,2,7,9,8,9,9,9,9,8,9,4,5,4,9,8,7,6,9,2,3,4,9,9,7,6,5,9,6,7,8,9,9,9,8,7,6,5,6,7,2,1,2,3,4,7,8,9,8,9,9,9,9,9,9,8,7,9,8,7,8,9,9,8,9,8,9,3,4,9,8,7,6,8,4,5,8,9,9,9,9,9,5,4,9,8,8,9,7,7,8,9,6,7,9,3,2,1,],[3,2,1,5,6,9,9,9,8,9,9,9,4,3,4,3,5,9,8,5,4,3,5,6,8,9,8,9,9,8,7,8,9,9,8,7,9,8,7,6,5,4,3,2,3,4,6,7,9,6,7,8,8,9,9,9,9,9,9,8,7,6,7,8,9,9,9,9,3,2,3,4,9,8,7,9,5,6,9,3,2,8,7,8,9,3,4,9,9,9,8,8,9,4,5,9,8,7,6,2,],[4,3,2,4,9,8,9,8,7,8,9,4,3,2,3,2,3,4,9,6,9,4,5,6,7,8,9,5,6,9,8,9,1,0,9,6,5,9,8,7,6,5,4,3,4,5,7,8,9,5,5,6,7,8,9,8,9,9,9,7,6,5,4,5,9,8,9,3,2,1,2,7,8,9,9,8,6,7,8,9,1,5,6,7,8,9,9,8,7,6,9,9,2,3,4,5,9,8,5,3,],[5,4,3,9,8,7,6,7,6,7,8,9,3,1,0,1,2,9,8,9,8,9,6,7,8,9,3,4,9,9,9,3,2,9,8,7,7,9,9,8,7,6,5,4,5,9,9,9,4,3,4,5,6,9,8,7,9,9,8,7,5,4,3,9,8,7,8,9,3,2,5,6,7,8,9,9,9,8,9,4,3,4,5,8,9,8,9,7,5,4,3,2,1,4,5,9,8,7,6,7,],[7,5,9,8,7,6,5,6,5,6,9,6,4,5,6,7,9,8,7,9,7,8,9,8,9,1,2,9,8,7,8,9,3,4,9,8,9,8,9,9,8,8,7,5,9,8,9,4,3,2,3,5,9,8,7,6,7,9,8,7,6,7,9,8,7,6,7,8,9,3,4,5,9,9,0,2,4,9,6,5,4,5,6,9,8,7,8,9,6,5,4,3,2,3,4,5,9,8,9,8,],[8,9,8,7,6,5,4,3,4,9,8,9,5,8,7,9,8,9,6,8,6,7,8,9,9,9,9,8,7,6,9,8,9,5,7,9,8,7,8,9,9,9,9,9,8,7,8,9,9,1,0,2,3,9,8,5,8,9,9,8,7,9,8,7,6,5,6,7,8,9,5,6,7,8,9,3,9,8,7,6,6,7,9,8,7,6,7,8,9,6,5,4,5,6,9,6,7,9,8,9,],[9,8,7,6,5,4,3,2,3,4,7,8,9,9,9,8,7,6,5,4,5,6,7,8,9,8,9,9,6,5,8,7,8,9,9,8,9,6,7,6,8,9,9,8,7,6,7,7,8,9,9,3,4,5,9,4,5,6,7,9,8,9,9,8,9,8,7,8,9,7,6,7,8,9,5,4,5,9,8,9,8,9,8,7,6,5,6,7,8,9,6,5,6,7,8,9,9,8,7,7,],[8,9,8,7,8,9,4,1,2,3,6,7,8,9,8,7,6,5,4,3,4,7,8,9,6,7,8,9,7,4,5,6,7,9,8,7,7,5,6,5,7,8,9,9,9,5,4,6,7,8,8,9,5,6,9,3,2,3,4,5,9,9,9,9,6,9,8,9,9,8,9,9,9,9,9,7,6,9,9,9,9,8,7,6,5,4,5,7,8,9,9,6,7,8,9,9,8,7,6,6,],[7,9,9,8,9,6,3,2,3,4,5,8,9,9,9,8,7,4,3,2,1,2,3,4,5,6,7,8,9,3,4,5,9,9,9,6,5,4,3,4,6,7,8,9,8,4,3,4,5,6,7,8,9,9,8,9,0,9,5,6,7,8,9,4,5,8,9,9,8,9,8,8,9,9,8,9,7,8,9,9,8,9,8,7,4,3,5,6,7,8,8,9,8,9,9,8,7,6,5,5,],[6,9,8,7,6,5,4,3,4,5,6,7,8,9,9,9,8,5,4,3,2,3,4,8,9,7,8,9,1,2,5,9,8,7,6,5,4,3,2,3,4,5,9,8,7,6,2,8,9,7,8,9,9,8,7,6,9,8,9,7,8,9,2,3,6,7,9,8,7,9,7,7,9,8,7,8,9,9,9,8,7,6,5,4,3,2,4,9,8,6,7,8,9,9,8,7,6,5,3,4,],[5,4,9,8,7,7,5,4,5,6,7,8,9,9,9,9,7,6,5,4,3,5,6,7,8,9,9,9,9,3,9,8,7,6,5,4,3,2,1,2,5,9,8,7,6,5,1,7,8,9,9,9,8,7,6,5,6,7,8,9,9,2,1,9,7,9,8,7,6,5,6,6,5,7,6,9,8,9,9,9,9,5,4,5,4,1,2,3,4,5,6,7,8,9,7,6,4,3,2,3,],[4,3,0,9,8,8,6,5,7,8,9,9,6,7,8,9,9,8,6,5,4,5,7,8,9,5,7,9,8,9,9,9,8,7,6,5,4,1,0,1,9,8,7,6,5,4,0,6,8,9,9,9,9,8,5,4,5,8,9,6,5,4,9,8,9,9,9,8,5,4,5,2,3,4,5,6,7,8,9,8,7,6,3,2,1,0,1,2,3,4,7,9,9,7,6,5,3,2,1,3,],[3,2,1,2,9,9,7,6,8,9,3,4,5,9,9,6,7,9,7,6,5,6,8,9,5,4,9,8,7,8,9,8,7,6,5,4,3,2,1,2,3,9,8,7,4,3,2,5,6,7,8,9,8,7,6,5,7,8,9,7,6,9,8,7,9,8,7,6,4,3,2,1,2,3,4,5,9,9,9,8,6,5,4,3,2,1,3,4,4,6,9,9,9,8,7,5,4,3,2,4,],[4,3,2,3,4,9,8,7,9,3,2,3,9,8,9,5,6,9,8,7,8,7,9,7,6,9,8,7,6,7,8,9,8,8,6,6,5,4,2,5,4,5,9,7,5,4,3,4,5,8,9,6,9,9,7,6,9,9,9,8,9,8,7,6,7,9,8,9,3,2,1,0,1,2,5,6,8,9,5,9,7,6,6,5,4,3,4,6,5,6,7,8,9,9,7,6,5,4,3,6,],[5,6,3,4,5,9,9,8,9,2,1,0,9,7,8,9,9,9,9,8,9,8,9,9,7,8,9,6,5,6,7,9,9,9,7,7,6,4,3,4,7,6,9,8,6,5,4,5,6,7,9,4,5,9,8,7,8,9,9,9,8,7,6,5,6,7,9,8,9,3,2,1,2,3,6,7,9,1,4,9,8,7,7,6,5,4,5,7,8,7,8,9,9,9,8,9,6,5,9,7,],[6,5,4,5,9,8,7,9,8,9,9,9,7,6,7,9,8,9,6,9,6,9,8,9,8,9,9,5,4,5,8,9,9,9,8,8,9,5,5,6,8,7,8,9,7,6,5,6,7,8,9,3,4,9,9,8,9,9,9,8,7,6,7,4,3,9,8,7,6,5,3,2,4,5,7,8,9,2,3,5,9,9,8,7,6,7,6,8,9,8,9,9,8,9,9,8,7,6,9,8,],[7,6,5,9,8,7,6,5,6,7,8,9,6,5,9,8,7,6,5,4,5,6,7,8,9,8,8,4,3,6,7,8,9,9,9,9,8,6,6,7,9,9,9,9,8,7,8,7,8,9,1,2,9,8,7,9,9,9,8,9,6,5,4,3,2,1,9,8,9,8,5,4,5,6,8,9,8,9,4,9,9,9,9,8,9,8,8,9,5,9,5,6,7,8,9,9,8,9,9,9,],[8,7,6,7,9,8,5,4,5,6,7,8,9,4,5,9,8,7,6,3,4,5,7,9,8,7,6,5,4,5,6,7,8,9,0,9,8,7,8,8,9,9,8,6,9,8,9,8,9,8,9,3,9,7,6,7,8,9,7,8,9,6,5,4,1,0,2,9,8,7,6,7,6,7,9,8,7,8,9,8,7,8,9,9,9,9,9,5,4,3,4,5,7,8,9,9,9,9,9,9,],[9,8,7,9,8,9,4,3,4,8,9,9,2,3,4,5,9,8,7,2,1,2,3,4,9,8,7,8,5,6,7,8,9,2,1,9,9,9,9,9,7,6,9,4,3,9,3,9,6,7,8,9,7,6,5,3,4,5,6,9,8,7,6,5,2,3,3,4,9,8,9,8,7,8,9,7,6,7,8,7,6,7,8,9,8,7,6,5,3,2,3,4,6,7,8,9,9,9,8,9,],[5,9,9,8,7,6,3,2,3,8,9,4,3,4,5,6,9,9,2,1,0,1,2,9,9,9,8,9,6,7,8,9,9,9,9,8,9,8,9,8,9,5,4,3,2,1,2,4,5,8,9,9,8,5,4,2,3,6,7,8,9,6,5,4,3,4,4,5,7,9,3,9,8,9,7,8,5,6,9,6,5,6,7,8,9,8,7,5,4,1,2,5,6,7,9,9,9,8,7,8,],[3,3,4,9,6,5,4,3,6,7,8,9,4,5,6,9,8,9,4,3,2,3,9,8,9,9,9,3,9,8,9,9,9,8,7,7,6,7,8,7,8,9,5,4,1,0,1,2,3,9,8,9,9,6,9,4,9,9,9,9,9,8,7,5,6,9,6,9,8,9,2,9,9,9,6,5,4,5,6,3,4,5,6,9,8,9,8,3,1,0,1,2,7,8,9,8,7,7,6,7,],[2,1,9,8,7,6,7,4,5,6,9,8,7,6,9,8,7,6,5,4,5,9,8,7,8,9,3,2,1,9,9,9,8,9,5,4,5,4,7,6,7,8,9,3,2,1,2,3,4,5,6,8,9,9,8,9,8,8,9,2,1,9,9,9,9,8,7,8,9,2,9,8,7,8,7,4,3,2,1,2,4,5,8,9,7,8,9,3,2,9,4,3,8,9,8,7,6,5,5,3,],[9,0,9,9,8,7,6,5,6,7,8,9,9,7,8,9,9,8,6,5,9,8,7,6,7,8,9,1,0,1,9,8,7,8,2,3,4,3,4,5,6,7,9,6,3,2,3,4,5,6,7,8,9,9,7,8,7,7,8,9,0,9,8,7,9,9,8,9,2,1,9,7,6,5,4,3,2,1,0,7,6,7,8,9,6,8,9,4,9,8,9,4,9,9,9,6,5,4,3,2,],[8,9,8,6,9,8,7,6,7,8,9,9,8,9,9,0,2,9,7,9,8,7,7,5,8,9,8,9,9,9,7,9,6,7,1,0,1,2,3,4,7,8,9,5,4,3,4,8,9,9,8,9,8,7,6,4,6,6,7,8,9,8,7,6,7,8,9,8,9,0,9,8,7,6,5,4,3,2,1,4,5,9,9,6,5,9,8,9,8,7,8,9,9,9,8,7,4,3,2,1,],[7,8,5,5,6,9,8,7,8,9,9,8,7,8,9,4,3,7,9,8,7,6,5,4,5,8,7,9,8,7,6,5,4,3,2,4,2,9,4,5,6,7,8,9,6,4,5,6,8,9,9,8,6,9,4,3,5,5,6,9,9,7,6,5,7,7,6,7,8,9,9,9,8,7,6,5,4,3,2,3,6,8,9,7,9,9,7,8,7,6,7,9,9,9,9,7,6,4,3,0,],[6,5,4,3,2,3,9,8,9,9,8,7,6,7,8,9,5,6,7,9,6,5,4,3,4,5,6,7,9,8,9,8,5,4,3,5,6,8,5,6,7,8,9,9,7,8,7,8,9,9,9,8,5,4,3,2,3,4,9,8,8,6,5,4,5,6,5,6,7,8,9,9,9,9,8,6,5,4,3,4,5,9,9,9,8,7,6,7,6,5,6,7,8,9,9,8,4,3,2,1,],[7,6,8,4,1,0,2,9,9,8,7,7,5,6,9,8,9,7,9,8,5,4,3,2,3,6,5,8,9,9,8,7,6,5,6,7,8,9,6,7,8,9,9,9,8,9,8,9,5,9,8,7,6,5,4,3,4,9,8,7,6,5,4,3,3,3,4,5,6,7,8,9,9,8,9,8,6,5,4,5,6,7,8,9,9,6,5,6,3,4,5,6,7,8,9,6,5,4,3,2,],[9,8,7,3,2,1,3,9,8,7,6,5,4,5,6,7,8,9,8,7,8,3,0,1,2,3,4,9,9,9,9,9,7,6,7,8,9,9,9,8,9,9,9,9,9,4,9,5,4,5,9,8,7,6,5,6,5,6,9,8,8,4,3,2,1,2,5,6,7,8,9,9,8,7,8,9,7,6,5,6,7,9,9,9,8,5,4,3,2,3,4,5,6,9,8,7,6,5,4,5,],[8,7,6,4,3,2,9,8,9,6,5,4,3,4,5,6,7,8,9,6,5,2,1,2,3,4,5,6,8,9,4,3,9,9,8,9,8,9,9,9,5,9,8,9,9,5,9,6,3,6,9,9,8,7,6,7,6,7,8,9,9,5,6,3,2,3,4,8,8,9,6,8,7,6,7,8,9,7,6,7,8,9,9,8,7,6,5,4,3,4,7,6,7,8,9,8,7,6,7,6,],[9,9,6,5,4,9,8,7,6,5,4,3,2,3,4,7,8,9,6,5,4,3,2,3,4,5,9,9,9,4,3,2,0,1,9,6,7,8,9,5,4,9,7,7,8,9,8,9,2,9,8,7,9,8,7,8,9,8,9,8,7,6,5,4,3,4,5,7,9,6,4,4,4,5,6,9,9,9,7,9,9,8,7,9,8,9,8,7,6,5,6,7,8,9,7,9,8,9,8,7,],[9,8,7,6,7,8,9,8,8,7,6,5,4,5,5,6,9,8,7,7,5,4,3,4,5,9,8,8,9,5,6,9,1,2,3,5,6,7,8,9,3,4,5,6,9,8,7,9,0,9,7,6,5,9,9,9,3,9,6,9,8,7,6,5,4,5,6,7,8,9,3,2,3,4,5,8,9,9,8,9,8,7,6,5,9,1,9,8,7,6,7,8,9,7,6,7,9,9,9,8,],[8,9,8,7,8,9,8,9,9,8,7,6,5,6,7,7,8,9,8,9,6,5,4,5,9,7,6,7,9,9,9,8,9,5,4,5,7,8,9,1,2,3,4,9,8,7,6,8,9,8,6,5,4,3,2,1,2,3,5,6,9,9,7,6,8,8,7,8,9,3,2,1,2,3,5,7,8,9,9,8,9,6,5,4,1,0,1,9,8,7,8,9,5,5,5,6,7,9,9,9,],[7,6,9,8,9,9,7,9,9,9,9,8,7,8,9,8,9,4,9,9,9,6,5,6,9,8,5,6,9,8,9,7,8,9,7,6,9,9,1,0,1,4,9,8,7,6,5,4,5,9,5,4,3,2,1,0,1,2,3,9,7,9,8,7,9,9,8,9,8,4,6,2,3,7,6,8,9,5,6,7,8,9,4,3,2,1,9,9,9,8,9,5,4,3,4,5,6,7,8,9,],[6,5,4,9,6,5,6,8,9,1,2,9,9,9,9,9,2,3,4,9,8,9,6,7,9,8,7,9,8,7,8,6,7,8,9,7,8,9,2,1,2,9,8,7,6,5,4,3,4,5,9,5,9,3,2,1,2,4,9,8,6,6,9,8,9,9,9,8,7,6,5,4,4,8,7,8,9,4,9,8,9,6,5,9,3,9,8,9,9,9,5,4,3,2,3,4,5,6,9,8,],[5,4,3,2,3,4,5,9,9,3,3,4,5,6,9,2,1,2,9,8,7,8,9,8,9,9,9,8,6,6,6,5,6,9,9,8,9,4,3,2,9,8,7,6,5,5,4,2,3,9,8,9,8,9,3,2,3,9,9,7,5,5,4,9,9,9,8,9,8,9,6,5,6,8,8,9,2,3,8,7,8,9,9,8,9,8,7,8,9,5,4,3,2,1,2,3,9,9,8,7,],[9,9,4,0,1,3,7,7,8,9,4,5,6,7,8,9,9,9,8,7,6,7,8,9,9,9,8,6,5,4,3,4,5,8,9,9,7,5,4,5,6,9,8,5,4,3,2,1,0,9,7,8,7,8,9,3,9,8,7,5,4,2,3,4,9,7,6,5,9,9,8,6,7,9,9,0,1,4,5,6,9,9,7,6,8,7,6,7,9,9,5,6,3,4,3,9,8,8,7,6,],[8,8,9,3,2,3,5,6,7,8,9,6,7,8,9,9,8,7,6,6,5,6,7,8,9,9,9,7,6,3,2,5,6,7,9,9,7,6,5,6,9,8,7,6,5,4,5,9,9,8,6,5,6,9,8,9,9,9,5,4,3,1,4,5,8,9,5,4,4,5,9,7,8,9,2,1,9,5,6,7,9,8,6,5,4,3,5,6,7,8,9,7,8,5,9,7,7,6,4,5,],[7,7,8,9,5,4,5,7,8,9,8,7,8,9,9,7,9,8,5,5,4,5,6,7,9,8,7,6,5,4,1,2,4,5,6,8,9,7,6,7,8,9,8,7,8,5,9,8,7,6,5,4,9,8,6,9,8,7,6,5,8,6,5,6,7,8,9,3,2,9,9,8,9,4,3,9,8,9,8,9,9,8,5,4,3,2,6,7,8,9,9,8,9,9,8,6,4,5,2,4,],[6,6,7,8,9,9,6,7,9,9,9,8,9,8,7,6,5,4,4,2,3,4,5,6,7,9,8,9,7,1,0,3,5,5,7,8,9,9,7,8,9,8,9,8,7,6,7,9,8,7,6,5,9,7,5,4,9,8,8,6,8,7,8,7,8,9,8,9,9,8,7,9,8,9,9,8,7,8,9,9,8,7,6,5,4,3,7,8,9,1,2,9,9,8,7,5,3,2,1,2,],[4,5,6,9,9,8,9,9,8,9,9,9,3,9,8,9,7,3,4,1,4,6,4,5,6,7,9,7,6,5,1,2,3,4,5,6,7,8,9,9,8,7,8,9,8,7,8,9,9,9,7,8,9,9,4,3,0,9,9,8,9,8,9,8,9,5,7,9,8,7,6,5,7,8,9,5,6,7,8,9,9,8,7,6,7,4,5,9,9,0,1,9,7,9,8,6,5,3,0,1,],[3,6,5,6,9,7,8,8,7,8,9,2,1,2,9,8,9,2,1,0,1,2,3,6,7,8,9,8,7,3,2,3,4,5,7,7,8,9,9,8,7,6,7,8,9,8,9,3,4,9,8,9,9,8,3,2,1,2,3,9,7,9,9,9,3,4,5,7,9,9,5,4,6,2,3,4,5,6,9,9,9,9,8,7,8,5,6,7,8,9,9,8,6,9,8,7,5,4,1,2,],[2,3,4,9,8,6,5,4,6,7,9,3,2,9,8,7,4,3,2,1,5,6,7,7,8,9,2,9,8,4,3,6,5,6,9,8,9,9,8,7,6,5,6,7,9,9,3,2,3,9,9,9,8,7,6,7,2,3,4,5,6,7,8,9,2,3,9,9,8,7,6,3,2,1,2,8,9,9,8,9,8,9,9,8,7,6,7,8,9,8,7,6,5,6,9,9,6,5,2,3,],[1,0,9,8,9,5,4,3,5,9,8,9,9,8,7,6,5,4,5,2,4,5,8,9,9,2,1,9,9,7,4,7,6,8,9,9,9,8,7,6,5,4,5,6,7,8,9,0,9,8,9,8,7,6,5,4,3,6,5,6,7,8,9,0,1,9,8,9,9,7,6,5,4,2,6,7,9,9,7,8,7,8,9,9,8,9,8,9,2,9,8,5,4,3,4,9,8,4,3,4,],[2,9,8,7,6,4,3,2,3,4,7,6,7,9,8,7,6,5,6,3,4,5,9,9,8,9,9,8,7,6,5,6,8,9,9,9,8,9,6,5,4,3,4,5,6,7,8,9,8,7,6,9,9,8,6,7,4,7,6,9,8,9,9,9,9,8,7,7,8,9,7,9,5,4,5,9,8,8,6,7,6,7,8,9,9,2,9,9,1,2,9,4,3,2,5,9,9,5,4,5,],[3,4,9,9,6,3,2,1,2,7,6,5,6,7,9,8,9,6,5,4,5,6,9,8,7,8,9,9,8,9,6,7,9,5,9,8,7,6,5,4,3,2,3,6,8,9,9,9,8,6,5,6,9,8,7,6,5,6,7,9,9,9,9,8,7,6,5,6,7,8,9,8,7,5,9,8,7,6,5,6,5,6,7,8,9,1,9,8,9,9,8,9,2,1,9,8,7,6,5,6,],[4,5,9,8,5,3,2,0,1,2,3,4,5,6,8,9,8,7,6,5,6,7,8,9,6,5,4,3,9,8,7,8,9,4,5,9,9,8,6,5,4,6,4,5,6,7,8,9,6,5,4,5,7,9,9,7,9,8,8,9,9,9,8,7,6,5,4,5,6,9,8,9,8,9,2,9,8,5,4,3,4,8,8,9,9,9,8,7,9,8,7,9,3,9,9,9,9,7,7,7,],[5,9,8,7,6,4,7,1,2,3,4,9,8,9,9,1,9,8,7,7,8,9,9,9,7,6,7,4,6,9,8,9,2,3,4,5,9,8,7,6,5,8,7,6,7,8,9,6,5,4,3,4,5,9,9,8,9,9,9,9,9,8,7,8,5,4,3,2,3,4,7,8,9,4,3,9,7,6,5,2,4,9,9,9,9,9,9,6,8,7,6,8,9,8,9,9,8,9,8,9,],[6,9,8,7,6,5,6,7,3,4,5,6,7,8,9,0,2,9,8,8,9,2,3,9,8,7,8,9,7,8,9,2,1,2,3,5,5,9,9,7,8,9,8,7,8,9,5,3,4,1,2,3,9,8,9,9,1,2,3,9,8,7,6,5,4,3,2,1,2,3,6,7,8,9,9,8,7,6,4,3,4,5,6,7,8,9,7,5,5,7,5,9,4,7,8,9,6,5,9,7,],[8,9,9,8,9,8,7,8,4,5,6,7,8,9,7,9,9,9,9,9,0,1,2,3,9,8,9,9,8,9,9,2,0,1,2,3,4,7,9,8,9,1,9,8,9,4,3,2,1,0,1,9,8,7,8,9,0,1,4,9,8,7,5,4,3,2,1,0,4,4,5,8,9,9,8,9,8,7,5,4,7,6,7,8,9,8,6,4,4,3,3,2,3,6,7,9,5,4,5,6,],[9,3,4,9,5,9,8,9,5,6,7,8,9,5,6,7,8,9,9,9,1,9,3,4,8,9,8,7,9,7,8,9,2,9,3,9,5,6,7,9,3,2,3,9,8,9,5,3,5,1,9,9,7,6,9,8,9,9,5,9,8,7,6,5,4,3,2,1,2,3,7,9,9,8,7,7,9,8,6,7,8,9,8,9,7,6,5,3,2,1,0,1,4,5,6,8,9,3,4,6,],[2,1,0,2,3,4,9,7,6,7,8,9,3,4,5,6,9,9,8,8,9,8,9,6,7,8,9,6,5,6,7,8,9,8,9,8,9,7,9,8,9,3,9,9,7,8,9,4,5,9,8,8,9,5,6,7,9,8,9,9,9,8,7,6,5,4,3,4,3,4,5,6,9,7,6,6,7,9,7,8,9,9,9,9,9,7,5,4,3,2,3,2,3,4,8,9,6,5,5,6,],[3,2,1,2,4,5,9,8,7,9,9,1,2,3,4,9,8,8,7,7,6,7,8,9,8,9,2,3,4,5,8,9,9,7,6,7,8,9,9,7,8,9,8,7,6,7,8,9,9,8,7,7,5,4,6,5,8,7,9,9,8,9,8,9,7,5,4,5,4,5,6,7,8,9,4,4,6,9,8,9,8,9,9,9,8,7,6,5,4,3,4,3,4,5,7,8,9,9,6,7,],[4,3,4,3,4,5,7,9,8,9,1,0,1,2,4,9,7,8,6,6,5,6,7,8,9,9,1,2,3,4,9,8,7,6,5,6,9,8,7,6,7,9,8,9,5,4,0,9,8,7,6,5,3,2,3,4,5,6,9,8,7,8,9,9,9,8,7,6,7,8,9,8,9,4,3,3,5,6,9,6,7,8,9,9,9,8,8,7,8,6,5,4,5,6,7,9,9,8,7,8,],[5,4,5,4,5,9,9,9,9,5,2,1,2,9,9,8,6,5,5,5,4,5,6,7,9,8,9,3,9,9,8,7,6,5,4,7,8,9,6,5,9,8,7,5,4,3,1,2,9,8,7,6,4,5,4,6,7,7,8,9,6,7,8,9,3,9,8,7,8,9,8,9,4,3,2,2,4,5,4,5,6,9,8,9,9,9,9,9,9,7,6,5,8,7,8,9,8,9,8,9,],[6,5,6,9,9,8,8,9,9,4,3,2,9,8,7,7,5,4,4,4,3,4,5,9,8,7,9,9,8,9,9,8,7,6,5,6,7,8,9,4,9,8,7,6,7,5,4,3,4,9,8,7,5,6,5,7,8,9,9,6,5,6,8,9,2,3,9,8,9,8,7,6,5,4,1,0,1,2,3,6,9,8,7,8,9,8,9,8,9,8,7,6,7,9,9,8,7,6,9,5,],[7,8,9,8,8,7,7,8,8,9,9,3,4,9,6,5,4,3,2,1,2,3,9,8,7,6,8,8,7,8,9,9,8,7,6,7,8,9,2,3,4,9,8,7,8,6,6,4,5,6,9,8,9,7,6,8,9,7,6,5,4,5,7,8,9,9,9,9,7,9,8,7,6,3,2,1,2,4,5,9,8,7,6,9,8,7,6,7,8,9,8,7,8,9,8,7,6,5,3,4,],[8,9,9,7,6,6,6,5,7,8,8,9,5,6,9,6,5,4,4,0,1,9,8,7,6,5,7,7,6,7,8,9,9,8,7,8,9,0,1,2,5,6,9,8,9,7,8,9,6,7,8,9,9,8,7,9,7,6,5,4,3,4,6,7,9,8,9,7,6,3,9,8,7,4,4,3,4,5,6,7,9,8,5,9,7,6,5,6,7,8,9,8,9,9,9,5,4,3,2,3,],[9,9,8,7,5,4,3,4,6,7,7,8,9,9,8,7,6,5,2,1,2,9,7,6,5,4,5,6,5,6,7,8,9,9,8,9,2,1,2,3,4,7,8,9,9,8,9,9,8,8,9,3,4,9,8,9,8,9,4,3,2,3,4,5,6,7,8,9,5,4,5,9,7,5,5,6,5,6,7,9,8,9,4,3,2,3,4,7,9,9,8,9,8,9,9,6,5,9,1,2,],[3,6,9,6,5,4,2,5,7,6,6,8,9,9,9,8,5,4,3,2,9,8,6,5,4,3,2,5,4,5,8,9,9,9,9,4,3,2,3,4,5,6,9,8,7,9,6,7,9,9,1,2,3,4,9,9,9,8,6,5,1,2,3,4,5,6,7,8,9,9,9,9,8,6,6,7,6,7,9,8,7,8,5,2,1,2,3,8,9,8,7,6,7,8,8,9,9,8,9,3,],[4,5,9,7,3,2,1,2,3,4,5,7,9,9,8,7,6,5,6,9,8,7,5,4,3,2,1,2,3,4,7,8,9,8,6,5,9,3,4,9,6,9,8,9,6,5,5,6,9,1,0,1,2,9,9,8,7,6,5,4,3,3,4,5,6,7,8,9,8,8,8,9,8,7,7,8,7,9,8,7,6,4,2,1,0,3,4,9,8,7,8,5,6,9,7,8,9,7,9,9,],[5,6,9,6,5,1,0,1,2,3,4,6,7,8,9,8,7,9,9,8,7,5,4,3,2,1,0,1,2,3,6,7,8,9,8,9,8,9,9,8,9,9,7,9,7,3,4,6,8,9,9,3,9,8,9,9,8,7,8,5,4,6,9,7,7,8,9,8,7,6,7,8,9,8,9,9,8,9,9,8,7,5,3,2,1,4,5,9,7,6,5,4,3,7,6,7,7,6,7,8,],[6,9,8,9,4,2,3,2,3,6,5,6,7,9,8,9,9,8,9,9,9,9,5,4,3,2,1,2,3,4,5,6,7,8,9,8,7,8,9,7,8,7,6,7,9,1,5,6,9,9,8,9,8,7,6,5,9,8,9,6,5,7,8,9,8,9,9,9,7,5,6,9,8,9,7,6,9,4,5,9,7,6,7,3,2,9,9,8,7,5,4,3,2,6,5,3,4,5,6,7,],[9,8,7,6,5,3,4,3,4,5,6,7,8,9,7,8,8,7,8,8,9,8,7,6,5,4,2,3,5,5,6,7,8,9,2,5,6,9,8,6,7,4,5,9,8,9,8,7,8,9,7,8,9,8,7,6,7,9,8,7,6,7,8,9,9,9,9,8,6,4,5,8,7,8,9,5,4,3,4,9,8,9,5,4,9,8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,],[5,9,9,7,8,4,5,6,5,6,7,8,9,7,6,9,8,6,7,7,8,9,8,7,6,5,3,4,6,6,7,8,9,6,3,4,7,8,9,4,3,3,1,8,7,8,9,8,9,5,6,8,9,9,8,8,9,9,9,9,7,8,9,1,2,9,8,7,8,3,4,7,5,6,8,9,9,2,3,5,9,7,6,7,8,9,8,7,6,5,6,9,2,1,4,3,4,5,8,7,],[4,3,9,8,6,5,9,8,6,7,8,9,6,5,4,6,7,4,5,6,7,8,9,8,7,8,6,5,7,7,8,9,6,5,4,5,9,9,7,3,2,1,0,1,6,8,9,9,5,4,6,7,8,9,9,9,9,8,7,9,8,9,2,0,1,9,7,6,5,2,3,2,3,4,5,7,8,9,5,9,8,9,9,8,9,4,9,9,8,6,9,8,9,6,5,4,5,6,9,8,],[3,2,0,9,8,9,7,9,7,9,9,8,7,6,3,1,2,3,6,7,8,9,9,9,8,9,8,9,8,8,9,9,7,6,5,6,9,8,6,5,3,2,2,3,4,7,8,9,4,3,4,9,9,0,2,9,8,7,6,7,9,9,2,1,9,8,7,5,4,1,0,1,3,4,5,6,7,8,9,3,7,9,8,9,2,3,4,5,9,9,8,7,8,9,6,7,6,7,8,9,],[4,3,9,9,9,6,5,9,8,9,9,9,9,7,4,6,3,4,5,6,7,8,9,6,9,8,9,0,9,9,7,9,8,7,6,7,8,9,7,6,4,5,4,4,5,6,7,8,9,2,7,8,9,1,9,9,9,6,5,6,7,8,9,2,9,8,6,4,3,2,1,2,4,5,6,7,8,9,5,2,6,6,7,9,1,2,5,9,9,9,7,6,7,9,7,8,7,8,9,8,],[5,9,8,9,6,5,4,5,9,8,8,9,9,9,7,5,4,5,8,7,8,9,6,5,6,7,9,1,9,7,6,5,9,8,9,8,9,9,8,9,8,7,6,7,6,7,8,9,0,1,6,7,8,9,8,7,6,5,4,5,6,7,8,9,1,9,6,5,4,3,2,3,5,6,7,8,9,5,4,3,4,5,8,9,0,1,9,8,7,8,6,5,6,8,9,9,8,9,6,7,],[9,8,7,8,9,4,3,6,5,6,7,8,9,8,7,6,5,6,7,8,9,6,5,4,5,6,8,9,7,6,5,4,2,9,9,9,8,7,9,5,9,8,9,9,7,9,9,2,1,2,5,6,7,8,9,8,7,6,3,6,7,8,9,9,2,9,7,6,5,4,3,4,6,7,8,9,8,6,5,6,7,6,7,8,9,9,8,7,6,7,6,4,6,7,8,9,9,4,5,6,],[9,7,6,7,8,9,2,5,4,5,6,7,8,9,8,7,6,7,8,9,6,7,4,3,4,5,7,8,9,6,5,3,1,2,9,8,9,6,5,4,3,9,3,9,8,9,4,3,2,3,4,5,6,7,8,9,8,7,2,4,5,6,7,8,9,9,8,7,6,5,4,5,7,8,9,9,8,7,6,7,9,7,8,9,9,8,7,6,5,4,3,3,4,4,5,6,8,9,6,8,],[7,6,5,9,9,0,1,2,3,4,5,6,7,8,9,9,7,8,9,6,5,4,3,2,3,4,8,9,9,8,6,3,2,9,8,7,6,5,4,3,2,1,2,3,9,6,5,4,5,4,5,6,7,8,9,9,9,4,3,4,6,7,8,9,0,1,9,8,7,6,5,6,7,9,0,1,9,8,7,8,9,8,9,9,8,7,6,5,4,3,2,1,2,3,6,7,9,8,7,9]
]

testData = [
[2,1,9,9,9,4,3,2,1,0,],
[3,9,8,7,8,9,4,9,2,1,],
[9,8,5,6,7,8,9,8,9,2,],
[8,7,6,7,8,9,6,7,8,9,],
[9,8,9,9,9,6,5,6,7,8]
]


def numFind(n):
    totals = []
    for row in range(0, len(n)):
        for col in range(0, len(n[row])):
            if n[row][col] < 9:
                n[row][col] = 1
            else:
                n[row][col] = "X"
    options = [shiftLeft, cross, xCross, shiftUp, shiftRight, taper, shiftDown]
    for _ in range(random.randrange(1000, 5000)):
        random.choice(options)(n)
    for row in range(0, len(n)):
        for col in range(0, len(n[row])):
            if n[row][col] != "X" and n[row][col] != 0:
                totals.append(n[row][col])
    totals.sort(reverse=True)
    return (totals[0] * totals[1] * totals[2])

def shiftLeft(n):
    for row in range(len(n) - 1, -1, -1):
        for col in range(len(n[row]) - 1, 0, -1):
            if n[row][col] == "X" or n[row][col] == 0:
                pass
            elif n[row][col - 1] == "X":
                pass
            else:
                n[row][col - 1] += n[row][col]
                n[row][col] = 0
    return n

def cross(n):
    for row in range(len(n) - 2, 0, -1):
        for col in range(1, len(n[row]) - 1):
            crossTotal = 0
            if n[row][col] == "X" or n[row][col] == 0:
                pass
            else:
                if n[row - 1][col] != "X":
                    crossTotal += n[row - 1][col]
                    n[row - 1][col] = 0
                if n[row + 1][col] != "X":
                    crossTotal += n[row + 1][col]
                    n[row + 1][col] = 0
                if n[row][col - 1] != "X":
                    crossTotal += n[row][col - 1]
                    n[row][col - 1] = 0
                if n[row][col + 1] != "X":
                    crossTotal += n[row][col + 1]
                    n[row][col + 1] = 0
                n[row][col] += crossTotal
    return n

def xCross(n):
    for row in range(len(n) - 2, 0, -1):
        for col in range(1, len(n[row]) - 1):
            xCrossTotal = 0
            if n[row][col] == "X" or n[row][col] == 0:
                pass
            else:
                if (n[row - 1][col] != "X" or n[row][col - 1] != "X") and n[row - 1][col -1] != "X":
                    xCrossTotal += n[row - 1][col -1]
                    n[row - 1][col -1] = 0
                if (n[row - 1][col] != "X" or n[row][col + 1] != "X") and n[row - 1][col + 1] != "X":
                    xCrossTotal += n[row - 1][col + 1]
                    n[row - 1][col + 1] = 0
                if (n[row][col + 1] != "X" or n[row + 1][col] != "X") and n[row + 1][col + 1] != "X":
                    xCrossTotal += n[row + 1][col + 1]
                    n[row + 1][col + 1] = 0
                if (n[row + 1][col] != "X" or n[row][col - 1] != "X") and n[row + 1][col - 1] != "X":
                    xCrossTotal += n[row + 1][col - 1]
                    n[row + 1][col - 1] = 0
                n[row][col] += xCrossTotal
    return n

def taper(n):
    clear = True
    for row in range(len(n) - 1, 0, -1):
        for col in range(len(n[row]) - 1, -1, -1):
            if n[row][col] == "X" or n[row][col] == 0:
                pass
            else:
                try:
                    if n[row][col - 1] == "X":
                        if n[row - 1][col] != "X":
                            clear = False
                            n[row - 1][col] += n[row][col]
                            n[row][col] = 0
                        elif n[row][col + 1] != "X" and n[row - 1][col + 1] != "X":
                            clear = False
                            n[row - 1][col + 1] += n[row][col]
                            n[row][col] = 0
                    elif n[row][col + 1] == "X":
                        if n[row - 1][col] != "X":
                            clear = False
                            n[row - 1][col] += n[row][col]
                            n[row][col] = 0
                        elif n[row][col - 1] != "X" and n[row -1][col - 1] != "X":
                            clear = False
                            n[row - 1][col - 1] += n[row][col]
                            n[row][col] = 0
                    else:
                        if n[row - 1][col] != "X":
                            clear = False
                            n[row - 1][col] += n[row][col]
                            n[row][col] = 0
                except Exception as e:
                    pass
    if clear:
        return n
    return taper(n)

def shiftUp(n):
    for row in range(len(n) - 1, 0, -1):
        for col in range(len(n[row]) - 1, -1, -1):
            if n[row][col] == "X" or n[row][col] == 0:
                pass
            elif n[row - 1][col] == "X":
                pass
            else:
                n[row - 1][col] += n[row][col]
                n[row][col] = 0
    return n

def shiftDown(n):
    for row in range(0, len(n) - 1, 1):
        for col in range(len(n[row]) - 1, -1, -1):
            if n[row][col] == "X" or n[row][col] == 0:
                pass
            elif n[row + 1][col] == "X":
                pass
            else:
                n[row + 1][col] += n[row][col]
                n[row][col] = 0
    return n

def shiftRight(n):
    for row in range(0, len(n), 1):
        for col in range(0, len(n[row]) - 1, 1):
            if n[row][col] == "X" or n[row][col] == 0:
                pass
            elif n[row][col + 1] == "X":
                pass
            else:
                n[row][col + 1] += n[row][col]
                n[row][col] = 0
    return n


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(time.asctime())
    n = data
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))