#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import pwlf  # Ensure that pwlf package is installed

def segment_plot(X, Y, resolution, npixel, arg, S):
    """
    This function fits the power law to the data, finds breaks, and plots the fitted lines alongside the breakpoint.

    Parameters:
    - X (numpy.ndarray): Frequencies from the power spectral density function.
    - Y (numpy.ndarray): PSD from the power spectral density function.
    - resolution (float): Image resolution.
    - npixel (int): Length of the square image.
    - arg (tuple): Title and additional information for the plot.
    - S (int): If S==1, it saves the plot.

    Returns:
    - B0 (float): Slope of the first power law.
    - B1 (float): Slope of the second power law.
    - brk (float): Breakpoint in meters.
    """
    # Extracting the break point.
    my_pwlf = pwlf.PiecewiseLinFit(np.log10(X[1:]), np.log10(Y[1:]))
    breaks = my_pwlf.fit(2)[1]

    # The frequency at the breakpoint
    f_x = np.power(10, breaks)

    # Find the slope (power law) and intercept of the lines fitted on the psd plot.
    # Broken power law
    if len(X[X < f_x]) > 1 and len(X[X > f_x] > 1):
        # Frequencies less than the frequency at the breakpoint
        y0 = Y[0:len(X[X < f_x]) + 1]
        x0 = X[0:len(X[X < f_x]) + 1]
        p0 = np.polyfit(np.log(x0[1:]), np.log(y0[1:]), 1)  # Fit a line to psds
        z0 = np.polyval(p0, np.log(x0[1:]))
        B0 = -p0[0]  # First Power Law
        print('\u03B2_0:', B0)

        # Frequencies greater than the frequency at the breakpoint
        y = Y[len(X[X < f_x]) - 1:]
        x = X[len(X[X < f_x]) - 1:]
        p = np.polyfit(np.log(x), np.log(y), 1)  # Fit a line to psds
        z = np.polyval(p, np.log(x))
        B1 = -p[0]  # Second Power Law
        print('\u03B2_1:', B1)

        # Converting the breakpoint from frequency into meters
        # brk = 1/f_x * resolution *np.max(X)
        brk = 1 / f_x

        # PSD and power law fit log-log Plot
        plt.figure(figsize=(12, 6))
        plt.loglog(X[1:], Y[1:], 'k')  # PSD log-log plot
        plt.loglog(x0[1:], np.exp(z0), '--b')  # Log-log plot of the first power law fit
        plt.loglog(x, np.exp(z), '--b')  # Log-log plot of the second power law fit
        plt.title(arg[0], fontsize=15)
        plt.xlabel('k', fontsize=15)
        plt.ylabel('Power Spectral Density', fontsize=15)

        # Show the breakpoint in the plot with a vertical line
        if B1 > 0 and B1 > B0:
            plt.axvline(f_x, ls='-.', c='r')
            plt.text(.85 * f_x, np.mean(np.exp(z)), "{:.1f} m".format(brk), fontsize=20, rotation=90)
            plt.text(x0[2], np.median((y0)), "\u03B2 = {:.2f}".format(B0), fontsize=20)
            plt.text(np.mean(x), np.mean((y)), "\u03B2 = {:.2f}".format(B1), fontsize=20)

        # If it does not follow a power law, print "None" for the breakpoint and betas
        else:
            brk = None
            B0 = None
            B1 = None
        print('Break in meters:', brk)
        print('----------------------')

    # If only one power law fits the data
    else:
        y = Y[1:]
        x = X[1:]
        p = np.polyfit(np.log(x), np.log(y), 1)  # Fit a line to psd
        z = np.polyval(p, np.log(x))

        # Plot the psd log-log with the power law fit
        plt.figure(figsize=(12, 6))
        plt.loglog(X[1:], Y[1:], 'k')  # PSD log-log plot
        plt.loglog(x, np.exp(z), '--b')  # Log-log plot of the power law fit
        plt.title(arg[0], fontsize=15)
        plt.xlabel('k', fontsize=15)
        plt.ylabel('Power Spectral Density', fontsize=15)
        B0 = None
        B1 = None
        brk = None

    # Save the plot
    if S == 1:
        plt.savefig('{}_{}.png'.format(arg[0], arg[1]), dpi=300)

    return B0, B1, brk

