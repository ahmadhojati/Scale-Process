# Scale-Process
The script is written according to the Trujillo et al., 2007 work on fractal features and scale process.
You can find the paper from the address below:
https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2006WR005317


This code reads an square image and fits broken powerlaw to the power spectral density of it at 18 directions and then estimates the scale breaks for each individual direction.
In addition, the code plots the breaks against dominant wind direction.
To run the code you need some packages:

1. powerlaw
2. PIL
3. numpy
4. matplotlib
5. scipy
6. math
7. cv2
8. seaborn as sns
9. collections
10. pandas
11. pwlf


Reference:
Trujillo, E., Ramírez, J. A. and Elder, K. J.: Topographic, meteorologic, and canopy controls on the scaling characteristics of the spatial distribution of snow depth fields: SPATIAL SCALING OF SNOW DEPTH, Water Resour. Res., 43(7), doi:10.1029/2006WR005317, 2007.
