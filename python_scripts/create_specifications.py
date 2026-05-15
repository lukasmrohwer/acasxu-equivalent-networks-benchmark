# creates a VNN-LIB 2.0 file (list of text lines) according to a fixed template:
def vnnlib_template_2():

    lines = []

    # intro comment
    lines.append("; An example of a monotonicity specification for ACAS-XU:")
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
    lines.append("(assert (and (>= X_f[0] X_g[0]) (>= X_g[0] -0.16247807)))") # The plane is further away in f than in g
    lines.append("(assert (== X_f[1] X_g[1]))")
    lines.append("(assert (== X_f[2] X_g[2]))")
    lines.append("(assert (== X_f[3] X_g[3]))")
    lines.append("(assert (== X_f[4] X_g[4]))")
    lines.append("")

    # output constraints
    lines.append("; Output Constraints")
    lines.append("(assert (Y_f[3] < Y_g[3]))") # Find an input where the cost associated with a strong left for f is smaller than for g

    return lines