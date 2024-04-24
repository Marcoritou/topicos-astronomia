import astropy.units as u
import numpy as np
import gala.potential as gp
from gala.units import galactic
import matplotlib.pyplot as plt

def create_gal_potential(total_mass, r_s, dm_fraction=0.73,
                         disk_total=0.7,bulge_total=0.29,
                         nucleus_total=0.01,
                         units=galactic):
    bar_mass = total_mass*(1-dm_fraction)
    dm_mass = total_mass*dm_fraction
    bulge_mass = bar_mass*bulge_total
    disk_mass = bar_mass*disk_total
    nucleus_mass = bar_mass*nucleus_total
    gal_potential = gp.CCompositePotential()
    gal_potential['halo'] = gp.NFWPotential(m=dm_mass,r_s=r_s,units=galactic)
    gal_potential['bulge'] = gp.PlummerPotential(m=bulge_mass, b=0.7, units=galactic)
    gal_potential['disk'] = gp.KuzminPotential(m=disk_mass, a=0.8, units=galactic)
    gal_potential['nucleus'] = gp.PlummerPotential(m=nucleus_mass, b=1, units=galactic)
    return(gal_potential)