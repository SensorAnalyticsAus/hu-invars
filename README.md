## Hu Invariant Moments

Implementations of Hu's invariants with respect to translation, scale, and rotation using `skimage` and `opencv` APIs.

### Usage

With `skimage`
``` 
python hu.py img/shapes-01.jpg
```
Output:
```
[ 3.0877   6.74289 14.92162 14.59358 29.37642 18.02443 29.83101]
```
With `opencv`
```
python hu-cv2.py img/shapes-01.jpg
```
Output
```
[  3.0877    6.74289  14.92162  14.59358  29.37642  18.02443 -29.83101]
```

### Refs
* M. K. Hu, "Visual Pattern Recognition by Moment Invariants", IRE Trans. Info. Theory, vol. IT-8, pp.179–187, 1962
* [Hu Moments' OpenCV method]( http://docs.opencv.org/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html?highlight=cvmatchshapes#humoments) 
