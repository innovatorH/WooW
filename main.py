import numpy as np
import matplotlib as plt


def calculate(*args, **kwargs):

    sigma_x = float(Element("sigma_x").value)
    sigma_y = float(Element("sigma_y").value)
    sigma_z = float(Element("sigma_z").value)
    tau_xy = float(Element("tau_xy").value)
    tau_yz = float(Element("tau_yz").value)
    tau_xz = float(Element("tau_xz").value)
    E = float(Element("E").value)
    v = float(Element("v").value)
    AnswerOne = Element("outputOne")
    AnswerTwo = Element("outputwo")
    AnswerThree = Element("outputhree")
    AnswerFour = Element("outputFour")
    AnswerFive = Element("outputFive")
    AnswerSix = Element("outputSix")


    
    d = 1/E # inverse of Young's modulus
    
    x = [
    [d, -v*d, -v*d, 0, 0, 0],
    [-v*d, d, -v*d, 0, 0, 0],
    [-v*d, -v*d, d, 0, 0, 0],
    [0, 0, 0, 2*(1+v)*d, 0, 0],
    [0, 0, 0, 0, 2*(1+v)*d, 0],
    [0, 0, 0, 0, 0, 2*(1+v)*d]
    ]
    
    
    y = [
    [sigma_x],
    [sigma_y],
    [sigma_z],
    [tau_xy],
    [tau_yz],
    [tau_xz]
    ]
    
    result = [
    [0],
    [0],
    [0],
    [0],
    [0],
    [0]
    ]
    
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]
    
    strain_x = result[0][0]
    strain_y = result[1][0]
    strain_z = result[2][0]
    gamma_xy = result[3][0]
    gamma_yz = result[4][0]
    gamma_xz = result[5][0]
    
    
    AnswerOne.write(strain_x)
    AnswerTwo.write(strain_y)
    AnswerThree.write(strain_z)
    AnswerFour.write(gamma_xy)
    AnswerFive.write(gamma_yz)
    AnswerSix.write(gamma_xz)


def clear(*args, **kwargs):
    Element("sigma_x").clear()
    Element("sigma_y").clear()
    Element("sigma_z").clear()
    Element("tau_xy").clear()
    Element("tau_xz").clear()
    Element("tau_yz").clear()
    Element("E").clear()
    Element("v").clear()
    Element("outputOne").clear()
    Element("outputwo").clear()
    Element("outputhree").clear()
    Element("outputFour").clear()
    Element("outputFive").clear()
    Element("outputSix").clear()