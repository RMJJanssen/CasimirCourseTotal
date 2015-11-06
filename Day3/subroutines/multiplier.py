""" Module for converting energy scales """

e =1.6e-19

def J_to_eV(energy,string=True):
    """ Function to convert energy from Joules to eV
    
    This function returns a number or a string with units, depending on the values of 'string'
    Triple quotation marks means a string running over multiple lines
    
    Parameters
    ----------------
    energy: energy in units of J
    string: if True, then string with unit is return, else just a number
    
    Returns
    ----------------
    String or Number with the energy in units of eV
    """
    E_in_eV = energy / e
    if string:
        return str(E_in_eV)+' eV'
    else:
        return E_in_eV
    
def eV_to_J(energy,string=True):
    """ Function to convert energy from eV to Joules
    
    This function returns a number or a string with units, depending on the values of 'string'
    Triple quotation marks means a string running over multiple lines
    
    Parameters
    ----------------
    energy: energy in units of eV
    string: if True, then string with unit is return, else just a number
    
    Returns
    ----------------
    String or Number with the energy in units of J
    """
    E_in_J = energy * e
    if string:
        return str(E_in_J)+' J'
    else:
        return E_in_J