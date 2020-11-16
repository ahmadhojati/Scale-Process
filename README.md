# Scale-Process
## The script is written according to the [9] work on fractal features and scale process.

This code reads an square image and fits broken powerlaw to the power spectral density of it at 18 directions and then estimates the scale breaks for each individual direction.
In addition, the code plots the breaks against dominant wind direction.

## Required Packanges
To run the code you need packages below:

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


## Data Samples
The name of the main code is "Fractal_features.ipynb".
I added four .tiff files of Airborne lidar snow depth as image input samples for three sites at Grand Mesa, Colorado.
The site names are A, F and M and the wind data related to each site provided in .csv files called "A_for_scale_process.csv", "LSOS_for_scale_process.csv" and "M_for_scale_process.csv" respectively.



## References

[1] Alstott, J., Bullmore, E. and Plenz, D.: powerlaw: A Python Package for Analysis of Heavy-Tailed Distributions, edited by F. Rapallo, PLoS ONE, 9(1), e85777, doi:10.1371/journal.pone.0085777, 2014.

[2] Anon: How to straighten a rotated rectangle area of an image using OpenCV in Python?, Stack Overflow [online] Available from: https://stackoverflow.com/questions/11627362/how-to-straighten-a-rotated-rectangle-area-of-an-image-using-opencv-in-python (Accessed 16 November 2020a), n.d.

[3] Anon: Plots with different scales — Matplotlib 2.2.3 documentation, [online] Available from: https://matplotlib.org/gallery/api/two_scales.html (Accessed 16 November 2020b), n.d.

[4] Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., Wieser, E., Taylor, J., Berg, S., Smith, N. J., Kern, R., Picus, M., Hoyer, S., van Kerkwijk, M. H., Brett, M., Haldane, A., del Río, J. F., Wiebe, M., Peterson, P., Gérard-Marchant, P., Sheppard, K., Reddy, T., Weckesser, W., Abbasi, H., Gohlke, C. and Oliphant, T. E.: Array programming with NumPy, Nature, 585(7825), 357–362, doi:10.1038/s41586-020-2649-2, 2020.

[5] Hunter, J. D.: Matplotlib: A 2D Graphics Environment, Comput. Sci. Eng., 9(3), 90–95, doi:10.1109/MCSE.2007.55, 2007.

[6] Jekel, C.: cjekel/piecewise_linear_fit_py, Python. [online] Available from: https://github.com/cjekel/piecewise_linear_fit_py (Accessed 16 November 2020), 2020.

[7] McKinney, W.: Data Structures for Statistical Computing in Python, pp. 56–61, Austin, Texas., 2010.

[8] SciPy 1.0 Contributors, Virtanen, P., Gommers, R., Oliphant, T. E., Haberland, M., Reddy, T., Cournapeau, D., Burovski, E., Peterson, P., Weckesser, W., Bright, J., van der Walt, S. J., Brett, M., Wilson, J., Millman, K. J., Mayorov, N., Nelson, A. R. J., Jones, E., Kern, R., Larson, E., Carey, C. J., Polat, İ., Feng, Y., Moore, E. W., VanderPlas, J., Laxalde, D., Perktold, J., Cimrman, R., Henriksen, I., Quintero, E. A., Harris, C. R., Archibald, A. M., Ribeiro, A. H., Pedregosa, F. and van Mulbregt, P.: SciPy 1.0: fundamental algorithms for scientific computing in Python, Nat Methods, 17(3), 261–272, doi:10.1038/s41592-019-0686-2, 2020.

[9] Trujillo, E., Ramírez, J. A. and Elder, K. J.: Topographic, meteorologic, and canopy controls on the scaling characteristics of the spatial distribution of snow depth fields: SPATIAL SCALING OF SNOW DEPTH, Water Resour. Res., 43(7), doi:10.1029/2006WR005317, 2007.

[10] Umesh, P.: Image Processing in Python, CSI Communications. 23, 2012.

[11] VAN ROSSUM, GUIDO. P. D. T.: PYTHON LIBRARY REFERENCE: release 3.6.4., 12TH MEDIA SERVICES, Place of publication not identified., 2018.

[12] Waskom, M., Botvinnik, O., O’Kane, D., Hobson, P., Lukauskas, S., Gemperline, D. C., Augspurger, T., Halchenko, Y., Cole, J. B., Warmenhoven, J., Ruiter, J. D., Pye, C., Hoyer, S., Vanderplas, J., Villalba, S., Kunter, G., Quintero, E., Bachant, P., Martin, M., Meyer, K., Miles, A., Ram, Y., Yarkoni, T., Williams, M. L., Evans, C., Fitzgerald, C., Brian, Fonnesbeck, C., Lee, A. and Qalieh, A.: Mwaskom/Seaborn: V0.8.1 (September 2017), Zenodo., 2017.

