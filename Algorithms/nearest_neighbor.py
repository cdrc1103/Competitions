import numpy as np
from tqdm import tqdm

class NN():

    def __init__(self, dist_mat):
        """   
        dist_mat: matrix that contains all distances between instances
        size: shape of the matrix (only symmetrical matrices)
        """
        self.dist_mat = dist_mat
        np.fill_diagonal(self.dist_mat, np.nan) # fill diagonal with np.nan so that the minimizer ignores it
        self.size = dist_mat.shape[0]

    def nn_algo(self, startPoint):
        """
        Nearest Neighbour algorithm

        startPoint: index from which to start the tour
        """
        # print(f"start_point: {startPoint}")
        tour = [startPoint]
        tour_distance = 0
        temp_dist_mat = self.dist_mat.copy()
        for i in tqdm(range(self.size-1)):
            min_index = np.nanargmin(temp_dist_mat[tour[-1],:]) # Block the column so that the same tour point is not picked again.
            tour_distance += temp_dist_mat[tour[-1], min_index]
            temp_dist_mat[:,tour[-1]] = np.nan
            tour.append(min_index)
        tqdm._instances.clear()

        return np.array(tour), tour_distance
    
    def run(self, iterations):
        """
        Randomly choose starting point and run the algorithm for a specified number of iterations.
        Than compare the results and pick the best tour
        
        iterations: number of times the nn algorithm is run (should be not larger than the size of the distance matrix)
        """

        if iterations > self.size:
            raise ValueError("Iterations should be smaller than the size of the distance matrix.")

        tours = np.zeros([iterations, self.size], dtype=np.int64)
        tour_dist = np.zeros([iterations, 1])
        rng = np.random.default_rng()
        start_points = rng.choice(self.size, iterations, replace=False)
        #print(f"start_point_list: {start_points}")
        for i, s in enumerate(start_points):
            tour, tour_distance = self.nn_algo(s)
            tours[i, :] = tour
            tour_dist[i, 0] = tour_distance
        #print(f"end_matrix: {self.dist_mat}")
        best_tour_idx = np.argmin(tour_dist)
        return tours[best_tour_idx,:]   