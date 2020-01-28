# Discovery of Hidden Local Spatial Patterns Using Local Deviation Transform
## Summary
Application of Local Deviation Transform on 2D spatial datasets for discovery of small local perturbations in long-range non-uniform data is explored in Python Jupyter Notebooks. Maps with dominant long range effects are transformed into maps of local neighborhood deviations, allowing to detect perturbations smaller than 1% of the total non-uniformity of data. 

Local Deviation Transform can be described by the following equation:
![](/resources/ldt_formula.png?raw=true)

This type of transformations has been demonstrated in analysis of non-uniformities of properties of thin films used in Semiconductor and LED industries.

![](/resources/ldt.png?raw=true)

**The approach can be generalized to higher dimensions and is applicable to various types of spatial data with superimposed local and long-range patterns.** 


## File Structure
```
|-- `Finding Hidden Local Patterns.ipynb`: main notebook demonstrating application of LDT in Jupyter Notebook
|-- `Finding Hidden Local Patterns.html`: main notebook demonstrating application of LDT in html

|-- `2D Polar Maps With Hidden Patterns.ipynb`: supplementary notebook detailing generation of sample data  in Jupyter Notebook
|-- `2D Polar Maps With Hidden Patterns.html`: supplementary notebook detailing generation of sample data in html 

|-- `local_deviation_transform.py`: python module with functions to calculate Shepards inverse distance and Local Deviation Transform

|-- data/  
    |-- `concave_nohidden.csv`: data with concave long range pattern without hidden local pattern  
    |-- `concave.csv`: data with concave long range pattern **with** hidden local pattern 
    |-- `convex_nohidden.csv`: data with convex long range pattern without hidden local pattern  
    |-- `convex.csv`: data with convex long range pattern **with** hidden local pattern
    |-- `donut_nohidden.csv`: data with donut-shaped long range pattern without hidden local pattern  
    |-- `donut.csv`: data with donut-shaped long range pattern **with** hidden local pattern
    |-- `smiley_kitty.csv`: hidden local pattern
```

Each dataset contains 625 points with the following features:
```
    X
    Y
    R
    Theta
    Value
```

The notebooks are also available for viewing in the html format.

## Requrements
Python 3.6+ and the following libraries installed:
```
    NumPy
    Pandas
    matplotlib
    scikit-learn
```


