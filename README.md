# Project: Finding small local perturbations using Local Deviation Transform
## Summary:
Application of Local Deviation Transform on 2D spatial datasets for discovery of small local perturbations in long-range non-uniform data is explored in Python Jupyter Notebooks. Maps with dominant long range effects are transformed into maps of local neighborhood deviations, allowing to detect perturbations smaller than 1% of the toal non-uniformity of data. 

This type of transformations has been demonstrate in analysis of non-uniformities of properties of thin films used in Semiconductor and LED industries. The general approach can be generalized to higher dimensions.  

Project overview and analysis are found in the "Finding Hidden Local Patterns.ipynb" notebook. "2D Polar Maps With Hidden Patterns.ipynb" is a supplementary notebook detailing how sample data was generated. Sample datasets are found in the /data folder. Each dataset contains 625 samples with the following features:

    X
    Y
    R
    Theta
    Value

The notebooks are also available for viewing in the html format.
## Requrements:
Python 3.6+ and the following Python libraries installed:

    NumPy
    Pandas
    matplotlib
    scikit-learn
    scipy


