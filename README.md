# PressureCalc
Uses Vinet equation of state for pressure calculations for DAC work

PfV.py calculates the pressure given a volume, inputs are either "element" "volume" or "element" "h" "k" "l" "d" for fcc or bcc crystal systems.

VfP.py calculates the volume given a pressure, inputs are "element" "pressure".  For bcc or fcc it additionally gives lattice parameter and the first few allowed d-spacings.


pvdata.dat contains information on elements (an example is given here).  Lines either start with a # for comments or a element name (eg Re) for data.  Data lines have format "element" "V0" "B0" "B1" "structure (optional)".  Only bcc and fcc structures have additional features.

