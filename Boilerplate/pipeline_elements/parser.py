
import numpy as np
import pandas as pd 

FOLDER ="data"

def parser(filename: str):
    """
    returns: m(number of pizzas) : int, 
            t2(number of team of 2) : int,
            t3(number of team of 3) : int,
            t4(number of team of 4) : int,
            
             [pizzas] 
    """
    with open(f"{FOLDER}/{filename}", "r") as f:
        first_line = f.readline()
        content = f.read()
        m, t2, t3, t4 = first_line.split("\n")[0].split(" ")

    input_data = 0
    return input_data