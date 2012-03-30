import galsim

class GSObject:
    """Base class for defining the interface with which all GalSim Objects access their shared 
    methods and attributes, particularly those from the C++ SBProfile classes.
    """
    def __init__(self, SBProfile):
        self.SBProfile = SBProfile

    # Now define direct access to all SBProfile methods via calls to self.SBProfile.method_name()
    #
    # ...Do we want to do this?  Barney is not sure... Surely most of these are pretty stable at,
    # the SBP level but this scheme would demand that changes to SBProfile are kept updated here.
    #
    # The alternative is for these methods to always be accessed from the top level 
    # via GSWhatever.SBProfile.method(), which I guess makes it explicit what is going on, but
    # is starting to get clunky...
    #
    # Will add method specific docstrings later if we go for this overall layout
    def maxK(self):
        maxk = self.SBProfile.maxK()
        return maxk

    def nyquistDx(self):
        return self.SBProfile.nyquistDx()

    def stepK(self):
        return self.SBProfile.stepK()

    def isAxisymmetric(self):
        return self.SBProfile.isAxisymmetric()

    def isAnalyticX(self):
        return self.SBProfile.isAnalyticX()

    # This method does not seem to be wrapped from C++
    # def isAnalyticK(self):
    # return self.SBProfile.isAnalyticK()

    def centroid(self):
        return self.SBProfile.centroid()

    def setFlux(self, flux=1.):
        self.SBProfile.setFlux(flux)
        return

    def getFlux(self):
        return self.SBProfile.getFlux()

    def distort(self, ellipse):
        self.SBProfile.distort(ellipse)
        return

    def shear(self, e1, e2):
        self.SBProfile.distort(galsim.Ellipse(e1, e2))
        return

    def rotate(self, theta):
        self.SBProfile.rotate(theta)
        return

    def shift(self, dx, dy):
        self.SBProfile.shift(dx, dy)
        return    

    def draw(self, dx=0., wmult=1):
    # Raise an exception here since C++ is picky about the input types
        if type(wmult) != int:
            raise TypeError("Input wmult should be an int")
        if type(dx) != float:
            raise Warning("Input dx not a float, converting...")
            dx = float(dx)
        return self.SBProfile.draw(dx=0., wmult=1)

    # Did not define all the other draw operations that operate on images inplace, would need to
    # work out slightly different return syntax for that in Python

    def shoot(self):
        raise NotImplementedError("Sorry, photon shooting coming soon!")


# Now define some of the simplest derived classes, those which are otherwise empty containers for
# SBPs...


# Gaussian class inherits the GSObject method interface, but therefore has a "has a" relationship 
# with the C++ SBProfile class rather than an "is a"... The __init__ method is very simple and all
# the GSObject methods & attributes are inherited.
# 
# In particular, the SBGaussian is now an attribute of the GSGaussian, an attribute named 
# "SBProfile", which can be queried for type as desired.
class GSGaussian(GSObject):
    """GalSim Gaussian, which has an SBGaussian in the SBProfile attribute.
    """
    def __init__(self, flux=1., sigma=1.):
        GSObject.__init__(self, galsim.SBGaussian(flux=flux, sigma=sigma))

    # Hmmm, these Gaussian-specific methods do not appear to be wrapped yet (will add issue to 
    # myself for this)... when they are, uncomment below:
    # def getSigma(self):
    #     return self.SBProfile.getSigma()
    #
    # def setSigma(self, sigma):
    #     return self.SBProfile.setSigma(sigma)


class GSMoffat(GSObject):
    """GalSim Moffat, which has an SBMoffat in the SBProfile attribute.
    """
    def __init__(self, beta, truncationFWHM=2., flux=1., re=1.):
        GSObject.__init__(self, galsim.SBMoffat(beta, truncationFWHM=truncationFWHM, flux=flux,
                          re=re))
    # As for the Gaussian currently only the base layer SBProfile methods are wrapped
    # def getBeta(self):
    #     return self.SBProfile.getBeta()
    # ...etc.


class GSSersic(GSObject):
    """GalSim Sersic, which has an SBSersic in the SBProfile attribute.
    """
    def __init__(self, n, flux=1., re=1.):
        GSObject.__init__(self, galsim.SBSersic(n, flux=flux, re=re))
    # Ditto!

