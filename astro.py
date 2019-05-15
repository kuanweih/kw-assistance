import numpy as np


def ra_to_deg(hour: float, minute: float, second: float) -> float:
    """ Convert RA from (hr, min, sec) -> degree """
    return  (hour + minute / 60. + second / 3600.) * 15.


def dec_to_deg(degree: float, minute: float, second: float) -> float:
    """ Convert Dec from (deg, arcmin, arcsec) -> degree """
    deg_sign = 1. if (degree + np.absolute(degree)) > 0 else - 1.
    return  deg_sign * (np.absolute(degree) + minute / 60. + second / 3600.)


def dist_modulus_to_distance(dm: float) -> float:
    """ Convert distance modulus -> distance (pc)

    : dm : distance modulus
    """
    return  10.**(dm / 5. + 1.)


def distance_to_dist_modulus(distance: float) -> float:
    """ Convert distance (pc) -> distance modulus """
    return  5. * np.log10(distance) - 5.
