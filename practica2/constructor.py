import astropy.units as u
import numpy as np
import gala.potential as gp
from gala.units import galactic
import matplotlib.pyplot as plt
import gala.dynamics as gd

def create_gal_potential(total_mass, r_s, dm_fraction=0.73,
                    disk_total=0.7,bulge_total=0.29,
                         nucleus_total=0.01,
                         bulge_b=0.7,
                         disk_a=0.8,
                         nucleus_b=1,
                         units=galactic):
    """
    This function creates a "gala.potential.potential.ccompositepotential.CCompositePotential" that is reminiscent of a S0 galaxy
    using a NFW potential for the halo, a Plummer potential for the bulge and nucleus and a Kuzmin potential for the disk
    The default values are given only to not break the function, these should be set by the user.
    PARAMETERS
    -------------------------------------
    RETURNS
    -------------------------------------
    """
    bar_mass = total_mass*(1-dm_fraction)
    dm_mass = total_mass*dm_fraction
    bulge_mass = bar_mass*bulge_total
    disk_mass = bar_mass*disk_total
    nucleus_mass = bar_mass*nucleus_total
    gal_potential = gp.CCompositePotential()
    gal_potential['halo'] = gp.NFWPotential(m=dm_mass,r_s=r_s,units=galactic)
    gal_potential['bulge'] = gp.PlummerPotential(m=bulge_mass, b=bulge_b, units=galactic)
    gal_potential['disk'] = gp.KuzminPotential(m=disk_mass, a=disk_a, units=galactic)
    gal_potential['nucleus'] = gp.PlummerPotential(m=nucleus_mass, b=nucleus_b, units=galactic)
    return(gal_potential)


def create_complex_potential(total_mass, r_s, 
                             dm_fraction=0.73,
                             disk_total=0.7,
                             bulge_total=0.29,
                             nucleus_total=0.01,
                             bulge_b=0.7,
                             disk_a=10,
                             disk_b=0.5,
                             nucleus_b=1,
                             units=galactic):
    """
    This function creates a "gala.potential.potential.ccompositepotential.CCompositePotential"
    using a NFW for the halo, a Plummer for the bulge and nucleus and a Miyamoto-Nagai potential for the disk
    The default values are given only to not break the function, these should be set by the user.
    PARAMETERS
    -------------------------------------
    RETURNS
    -------------------------------------
    """
    bar_mass = total_mass*(1-dm_fraction)
    dm_mass = total_mass*dm_fraction
    bulge_mass = bar_mass*bulge_total
    disk_mass = bar_mass*disk_total
    nucleus_mass = bar_mass*nucleus_total
    gal_potential = gp.CCompositePotential()
    gal_potential['halo'] = gp.NFWPotential(m=dm_mass,r_s=r_s,units=galactic)
    gal_potential['bulge'] = gp.PlummerPotential(m=bulge_mass, b=bulge_b, units=galactic)
    gal_potential['disk'] = gp.MiyamotoNagaiPotential(m=disk_mass,a=disk_a,b=disk_b,units=galactic)
    gal_potential['nucleus'] = gp.PlummerPotential(m=nucleus_mass, b=nucleus_b, units=galactic)
    return(gal_potential)