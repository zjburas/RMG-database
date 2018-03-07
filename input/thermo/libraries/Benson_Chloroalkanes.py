#!/usr/bin/env python
# encoding: utf-8

name = "Benson_Chloroalkanes"
shortDesc = u"Chloroalkanes used to fit/validate Benson Cl GAVs"
longDesc = u"""
Based on experimental measurements taken from:
Thermochemical Kinetics (book), 2nd edition, by Sidney Benson
and
Benson et al., Additivity Rules for the Estimation of Thermochemical Properties, Chem. Rev., vol. 69, pg. 279 (1969)
"""
entry(
    index = 0,
    label = "Cl",
    molecule = 
"""
multiplicity 2
1 Cl u1 p3 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.61674,9.55905e-13,-2.26881e-15,2.23748e-18,-7.78638e-22,13763.2,4.96934], Tmin=(298,'K'), Tmax=(1167.42,'K')),
            NASAPolynomial(coeffs=[2.61674,3.8212e-10,-4.56773e-13,2.41658e-16,-4.77396e-20,13763.2,4.96935], Tmin=(1167.42,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "Cl2",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14206,0.00479031,-6.92268e-06,4.81713e-09,-1.29784e-12,-1096.85,7.7609], Tmin=(298,'K'), Tmax=(894.11,'K')),
            NASAPolynomial(coeffs=[3.88928,0.00148489,-1.44019e-06,7.76119e-10,-1.8104e-13,-1231.97,4.23125], Tmin=(894.11,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "HCl",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53628,0.000374097,-2.62701e-06,4.78617e-09,-2.27479e-12,-12126.4,2.26447], Tmin=(298,'K'), Tmax=(674.86,'K')),
            NASAPolynomial(coeffs=[4.11121,-0.00302163,4.89403e-06,-2.61729e-09,4.58076e-13,-12204.3,-0.285156], Tmin=(674.86,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "ClO",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {2,S}
2 O  u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.32449,0.000246424,7.1635e-06,-1.16098e-08,5.42331e-12,11133.4,7.98445], Tmin=(298,'K'), Tmax=(627.97,'K')),
            NASAPolynomial(coeffs=[2.39177,0.00620933,-7.13173e-06,3.62145e-09,-6.62331e-13,11250.1,12.0469], Tmin=(627.97,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "CCl4",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 Cl u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.83114,0.0400388,-6.92547e-05,5.78087e-08,-1.8956e-11,-13639.3,11.8805], Tmin=(298,'K'), Tmax=(711.74,'K')),
            NASAPolynomial(coeffs=[7.23134,0.0153093,-1.71368e-05,8.99091e-09,-1.80854e-12,-14265.7,-7.85163], Tmin=(711.74,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "CHCl3",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.50654,0.0318882,-4.31201e-05,2.81802e-08,-6.90751e-12,-13916,19.1716], Tmin=(298,'K'), Tmax=(811.17,'K')),
            NASAPolynomial(coeffs=[5.93472,0.0128665,-1.315e-05,7.82627e-09,-1.95272e-12,-14727,-1.83579], Tmin=(811.17,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "CH2Cl2",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H  u0 p0 c0 {1,S}
3 H  u0 p0 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
5 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.67987,0.0181637,-1.07685e-05,-1.85287e-09,3.41554e-12,-12683.5,18.0126], Tmin=(298,'K'), Tmax=(684.96,'K')),
            NASAPolynomial(coeffs=[1.93499,0.0185429,-1.56921e-05,6.92293e-09,-1.24151e-12,-12762.3,16.5582], Tmin=(684.96,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "CCl3CCl3",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
5 Cl u0 p3 c0 {1,S}
6 Cl u0 p3 c0 {2,S}
7 Cl u0 p3 c0 {2,S}
8 Cl u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.21794,0.139402,-0.000305829,3.0791e-07,-1.1585e-10,-20253.2,46.9821], Tmin=(298,'K'), Tmax=(668.62,'K')),
            NASAPolynomial(coeffs=[12.0754,0.0382038,-8.38645e-05,9.16454e-08,-3.68766e-11,-22616.3,-29.8645], Tmin=(668.62,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "CH3CHCl2",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.19731,0.0260213,-3.47146e-06,-2.27533e-08,1.58849e-11,-16335.5,16.7355], Tmin=(298,'K'), Tmax=(520.98,'K')),
            NASAPolynomial(coeffs=[0.784738,0.0369138,-3.49684e-05,1.77246e-08,-3.6221e-12,-16189,22.6232], Tmin=(520.98,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "C2H5Cl",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 H  u0 p0 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28845,0.00198677,7.28501e-05,-1.24463e-07,6.37394e-11,-14931.3,11.6737], Tmin=(298,'K'), Tmax=(594.41,'K')),
            NASAPolynomial(coeffs=[-4.68439,0.0550688,-5.96642e-05,2.25461e-08,2.58814e-12,-13973.4,46.0754], Tmin=(594.41,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "C2Cl4",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,D}
2 Cl u0 p3 c0 {1,S}
3 Cl u0 p3 c0 {1,S}
4 C  u0 p0 c0 {1,D} {5,S} {6,S}
5 Cl u0 p3 c0 {4,S}
6 Cl u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.26786,0.0796422,-0.000169852,1.70581e-07,-6.44315e-11,-3777.77,30.5655], Tmin=(298,'K'), Tmax=(692.75,'K')),
            NASAPolynomial(coeffs=[9.06504,0.019711,-3.9503e-05,4.45821e-08,-1.87592e-11,-5202.96,-15.4453], Tmin=(692.75,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "CH2CCl2",
    molecule = 
"""
1 C  u0 p0 c0 {2,D} {5,S} {6,S}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.69375,0.0281237,-2.50035e-05,7.33735e-09,1.18746e-12,-1396.98,17.7349], Tmin=(298,'K'), Tmax=(758.37,'K')),
            NASAPolynomial(coeffs=[3.17805,0.0241053,-2.45923e-05,1.36014e-08,-3.0617e-12,-1731.69,10.2621], Tmin=(758.37,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "C2H3Cl",
    molecule = 
"""
1 C  u0 p0 c0 {2,D} {4,S} {5,S}
2 C  u0 p0 c0 {1,D} {3,S} {6,S}
3 Cl u0 p3 c0 {2,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70051,0.000863876,4.61027e-05,-6.94228e-08,3.16348e-11,1090.31,8.91651], Tmin=(298,'K'), Tmax=(590.44,'K')),
            NASAPolynomial(coeffs=[0.152401,0.0243855,-1.2344e-05,-4.90911e-09,4.9449e-12,1518.28,24.2407], Tmin=(590.44,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "CH3CH2CH2Cl",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C  u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  H  u0 p0 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  Cl u0 p3 c0 {3,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.54242,0.0274482,1.88171e-05,-5.61748e-08,3.21938e-11,-17449.2,21.0756], Tmin=(298,'K'), Tmax=(519.48,'K')),
            NASAPolynomial(coeffs=[-1.05587,0.0474399,-3.8865e-05,1.77941e-08,-3.37656e-12,-17179,31.9111], Tmin=(519.48,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "CH3CHClCH3",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  Cl u0 p3 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[78.8438,-0.676397,0.00240217,-3.59755e-06,1.97275e-09,-25042.5,-289.141], Tmin=(298,'K'), Tmax=(641.65,'K')),
            NASAPolynomial(coeffs=[570478,-3480.62,7.96016,-0.0080873,3.07974e-06,-7.47864e+07,-2.51121e+06], Tmin=(641.65,'K'), Tmax=(700,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (700,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "(CH3)3CCl",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C  u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  Cl u0 p3 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[145.871,-1.26118,0.00433884,-6.32156e-06,3.36217e-09,-36651.1,-559.982], Tmin=(298,'K'), Tmax=(693.1,'K')),
            NASAPolynomial(coeffs=[1.47458e+08,-788417,1570.83,-1.38063,0.000450996,-2.19441e+10,-6.68191e+08], Tmin=(693.1,'K'), Tmax=(700,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (700,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "C6H5Cl",
    molecule = 
"""
1  C  u0 p0 c0 {2,B} {6,B} {7,S}
2  C  u0 p0 c0 {1,B} {3,B} {8,S}
3  C  u0 p0 c0 {2,B} {4,B} {9,S}
4  C  u0 p0 c0 {3,B} {5,B} {10,S}
5  C  u0 p0 c0 {4,B} {6,B} {11,S}
6  C  u0 p0 c0 {1,B} {5,B} {12,S}
7  Cl u0 p3 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {5,S}
12 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0551034,0.0337056,5.12838e-05,-1.2581e-07,7.14182e-11,4572.15,26.8036], Tmin=(298,'K'), Tmax=(522.72,'K')),
            NASAPolynomial(coeffs=[-6.02157,0.0793436,-7.96246e-05,4.10785e-08,-8.36573e-12,5196.17,51.7203], Tmin=(522.72,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

