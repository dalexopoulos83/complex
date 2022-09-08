from app.ComplexNum import ComplexNum

""" This File have some example of Complex calculator app """

cn1 = ComplexNum(3, 7)
cn2 = ComplexNum(3, 7)
cn3 = ComplexNum(3)
cn4 = ComplexNum(0, 7)

print("-------------")
a, b = cn1.readComplex()
print(a + b)
print("-------------")

cn1 + cn2
cn1 - cn2
cn1 * cn2
cn1 / cn2
cn1**3
cn1 + cn3
cn2 + cn4
cn3 + cn4
