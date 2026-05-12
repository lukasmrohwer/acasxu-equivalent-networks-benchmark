# creates a VNN-LIB 2.0 file (list of text lines) according to a fixed template:
# Arguments:
# - eps_in: allowed distance from original network's output
def vnnlib_template_2():

    lines = []

    # intro comment
    lines.append("; Epsilion equivalence in pruned networks:")
    lines.append("; a VNN-COMP benchmark with equivalent networks.")
    lines.append("; Author: Lukas Rohwer")
    lines.append("")

    # tell the verifier to use VNN-LIB 2.0
    lines.append("(vnnlib-version <2.0>)")
    lines.append("")

    # neural network declaration
    lines.append("(declare-network f")
    lines.append("    (declare-input X_f real [5])")
    lines.append("    (declare-output Y_f real [5])")
    lines.append(")")
    lines.append("(declare-network g")
    lines.append("    (equal-to f)")
    lines.append("    (declare-input X_g real [5])")
    lines.append("    (declare-output Y_g real [5])")
    lines.append(")")
    lines.append("")

    # input constraints
    lines.append("; Input Constraints")
    lines.append("(assert (and (<= X_f[0] 0.667245963) (>= X_f[0] -0.16247807)))") # Unscaled distance in feet between 10000 and 60000
    lines.append("(assert (and (<= X_f[1] 0.0) (>= X_f[1] -0.25)))") # Unscaled angle to intruder relative to ownship heading (forward-right quadrant) (-1.57079632679, 0)
    lines.append("(assert (and (<= X_f[2] 0.5) (>= X_f[2] 0.25)))") # Unscaled heading angle of intruder relative to ownship heading (back-left quadrant) (1.57079632679, 3.141592653589793)
    lines.append("(assert (== X_f[3] 0.227272727))") # Unscaled speed of ownship at 900 feet per second
    lines.append("(assert (== X_f[4] 0.25 ))") # Unscaled speed of ownship at 900 feet per second
    lines.append("(assert (<= X_f[0] X_g[0]))") # For g, the distance is larger
    lines.append("(assert (== X_f[1] X_g[1]))")
    lines.append("(assert (== X_f[2] X_g[2]))")
    lines.append("(assert (== X_f[3] X_g[3]))")
    lines.append("(assert (== X_f[4] X_g[4]))")
    lines.append("")

    # output constraints
    lines.append("; Output Constraints")
    lines.append("(assert (and (Y_f[1] < Y_f[3]) (Y_g[1] >= Y_g[3])))") # Find an input to f that results in weak-left, and for g results in strong-left

    return lines

"""
; Unscaled Input 0: (55947.691, 60760) Distance from ownship to intruder (Feet)
(assert (<= X_0 0.679857769))
(assert (>= X_0 0.6))

; Unscaled Input 1: (-3.141592653589793, 3.141592653589793) Angle to intruder relative to ownship heading direction (counter clockwise) radians
(assert (<= X_1 0.5))
(assert (>= X_1 -0.5))

; Unscaled Input 2: (-3.141592653589793, 3.141592653589793) Heading angle of intruder relative to ownship heading direction (counter clockwise) radians
(assert (<= X_2 0.5))
(assert (>= X_2 -0.5))

; Unscaled Input 3: (1145, 1200) Speed of ownship  Feet per second
(assert (<= X_3 0.5))
(assert (>= X_3 0.45))

; Unscaled Input 4: (0, 60) Speed of intruder Feet per second
(assert (<= X_4 -0.45))
(assert (>= X_4 -0.5))


https://www.mathworks.com/help/deeplearning/ug/verify-global-stability-of-acas-xu-neural-networks.html


P -> Q === NOT P OR Q === NOT (P AND NOT Q)
we want to find the negation so simply
P AND NOT Q

P = Y_f[1] < Y_f[3]                choose weak left over strong left at shorter distance
Q = Y_g[1] < Y_g[3]                choose weak left over strong left at longer distance

NOT Q = Y_g[1] >= Y_g[3]

P AND NOT Q = (Y_f[1] < Y_f[3]) AND (Y_g[1] >= Y_g[3])

"""