import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors


def shepards_weights(distances, power=0):
    """Returns inverse distance weights using Shepard's method for input distances
       wi = 1 / (d0, di) ** power: for d != 0, otherwise 1.
       
    Args:
        distances ([float]): distances from point to its neighbors
        power (float): Shepards power parameter
        
    Returns:
        [float]: Shepards inverse distance weights
    """
    return [1 / (d ** power) if d != 0 else 1 for d in distances]


def local_deviation_transform(df, r_local=24, dist_sensitivity=6):
    """Adds column to data frame (df) with a transforms of input values to
       deviation from surrounding neighborhood weighted value: 
       
       LDT = value - neighborhood_weighted_value.
       
       Values to be transformed must be in df['Value'] column.
    
    Args:
        df (pandas.dataFrame): dataFrame containing map coordinates and values to                          be transformed. Must contain the following columns:
                - X, Y, R, Theta, Value

        radius (float): local neighborhood radius
        dist_sensitivity (float): Shepards inverse distance weighting power
                                  parameter:

                weighti = 1 / d ** dist_sensitivity, 
                                  
                where d is distance between a point and its neighbor
    
    Returns:
        transformed_values [pd.Series]: array of transformed values, matching indeces with input frame `df`
    """
    # Check if data frame contains necessary columns
    if any(col not in df for col in ['X', 'Y', 'Value']):
        print('Error: dataframe does not contain one of the required columns X, Y, R, Theta, Value')
        return
    
    # array to store local deviations
    deviations = np.zeros(len(df.index))
    # array of X, Y coordinates for NN search
    coordinates = np.array([[x, y] for x, y in zip(df.X, df.Y)])
        
    # find nearest coordinate neighbors 
    # using sklearn.neaighbors.NearestNeighbors with default parameters
    nbrs = NearestNeighbors().fit(coordinates)
    # return neighbors within radius=r_local
    nbr_distances, nbr_indices = nbrs.radius_neighbors(coordinates, radius=r_local)
    
    for idx, value in enumerate(df.Value):
        # calculate neighborhood weighted mean value
        nbr_weights = shepards_weights(nbr_distances[idx], power=dist_sensitivity)
        nbr_values = df.Value[nbr_indices[idx]]
        neighborhood_weighted_value =(np.dot(nbr_weights, nbr_values) 
                                      / np.sum(nbr_weights))
        # calculate deviation of point from local neighborhood weighted mean
        deviations[idx] = value - neighborhood_weighted_value
    
    transformed_values = pd.Series(deviations, index=df.index.copy())

    return transformed_values