# multiple-feedback-filter.py
#!/usr/bin/env python27
"""Multiple Feedback filter script

 Initally will be for Low Pass filter realizations only.

 Author: Douglass Murray
 Date: 2016-07-05

 Based on Figure 5-70 in Op Amp Applications Handbook, by Walt Jung.
 Figure 5-70 ASCII style
        +------+--------------+-----o
        R4     C5             |
        |      |   ___amp__   |
 o--R1--+--R3--+--| -      |  |
        |         |    out |--+
        C2     +--| +      |
        |      |  |________|
       -_-    -_-
"""
import numpy as np

def interface():
    """Runs general interface/welcome screen
    """
    print("")
    print("Multple Feedback Low Pass Filter")
    print("--------------------------------")
    print("         +------+--------------+-----o")
    print("         R4     C5             |")
    print("         |      |   ___amp__   |")
    print(" o---R1--+--R3--+--| -      |  |")
    print("         |         |    out |--+")
    print("         C2     +--| +      |")
    print("         |      |  |________|")
    print("        -_-    -_-")
    choice = int(input("Calculate filter response (1) or calculate component values (2): "))

    if choice == 1:
        rOne = float(input("Input R1: "))
        rThree = float(input("Input R3: "))
        rFour = float(input("Input R4: "))
        cTwo = float(input("Input C2 in uF: "))
        cFive = float(input("Input C5 in uF: "))
        component_transfer_function(rOne, rThree, rFour, cTwo, cFive)
    elif choice == 2:
        cut_off_freq = float(input("Input cut-off frequency: "))
        decent_cap = float(input("Input C5 capacitance in uF: "))
        cut_off_function(cut_off_freq, decent_cap)
    else:
        print("Please choose either 1 or 2")

def cut_off_function(f0, c5):
    """Calculates the component values for the given cut-off frequency

    Args:
        f0: cut-off frequency
        c5: based line capacitor
    Returns:
        None
    """
    # Intialized constants
    alpha = 0.5 # damping ratio, default (1/2)
    H = 1.0 # circuit gain at passband, default 1 (unity)

    # Convert to uF
    realC5 = c5 * 1.0e-6

    k = (2.0 * np.pi * f0 * realC5)
    r4 = alpha / (2.0 * k)
    r3 = alpha / (2.0 * (H + 1.0) * k)
    r1 = alpha / (2.0 * H * k)
    c2 = (4.0 / (2.0 * alpha)) * ((H + 1.0) * realC5)

    print("For cutoff frequency: ", f0, " Hz")
    print("R1: ", r1)
    print("R3: ", r3)
    print("R4: ", r4)
    print("C2: ", c2)
    print("C5: ", realC5)

def component_transfer_function(r1, r3, r4, c2, c5):
    """Calculates the cut-off frequency (f0) and damping ratio (alpha) based
    on filter's component choices

    Args:
        r1, r3, r4: resistors in filter, Ohms
        c2, c5: capacitors in filter, uF
    Returns:
        None
    """
    # Convert to uF
    realC2 = c2 * 1.0e-6
    realC5 = c5 * 1.0e-6
    H = 1.0 # circuit gain at passband, default 1 (unity)
    k = ((4.0 * (H + 1.0) * realC5) / realC2) / (2.0 * r3 * 4.0)
    alpha = r3 * 2.0 * (H + 1.0) * k
    f0 = k / (2.0 * np.pi * realC5)

    print("For R1: ", r1)
    print("For R3: ", r3)
    print("For R4: ", r4)
    print("For C2: ", realC2)
    print("For C5: ", realC5)
    print("Cutoff frequency: ", f0, " Hz")
    print("Damping ratio: ", alpha, " arb.")

if __name__ == '__main__':
    while(1):
        interface()
