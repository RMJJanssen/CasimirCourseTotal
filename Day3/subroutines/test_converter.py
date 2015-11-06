import subroutines.converter

def test_J_to_eV():
    assert converter.J_to_eV(1) == '6.25e+18 eV' #assert is statement that says: "Make sure that this is the case"

def test_J_to_eV2():
    assert converter.J_to_eV(1,False) == 1.0/converter.e