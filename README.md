# Miscellaneous
Miscellaneous data processing applications

### Inerpolate_list.py

Based on a list of real numbers where consecutive numbers are equal to or greater than the previous one,
it generates a list where consecutive numbers are always greater than the previous one.
When it finds a group of equal numbers, it modifies their values, generating regular spacing between 
that value and the next greater number.

### Delete_Outliers.ipynb

Starting from a series of data $(x, y)$, perform the following process to clean outlier data:

1. Apply the Savitzky–Golay filter (`savgol_filter`) to smooth the dependent variable $Y$.
2. Analyze the data series. Values of $Y$ whose distance from the corresponding value (with the same $X$ value) on the smoothed curve is greater than the standard deviation multiplied by a certain factor (e.g., 0.5) are considered outliers and are removed from the data series.
3. Generate a figure with the original data series, the smoothed curve, the filtered data series, and the outliers.

**Note**: The tolerance factor for detecting outliers can be adjusted depending on the nature of the data and the required level of smoothing.
