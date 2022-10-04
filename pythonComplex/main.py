from app.ComplexNum import ComplexNum

""" This File have some example of Complex calculator app """

cn1 = ComplexNum(3, 7)
cn2 = ComplexNum(3, 7)
cn3 = ComplexNum(3)
cn4 = ComplexNum(1, 1)

print(cn1 * 4)
print(4 * cn1)
print(cn1 + 4)
print(cn1 - 4)
print(4 + cn1)
print(4 - cn1)
print(cn1 * cn2)
print(cn1 / 4.0)
print(4 / cn1)
print(cn1**3)
print(cn1 + cn3)
print(cn2 - cn4)
print(cn3 / cn4)
print(cn1 * cn2 * cn3)
