# Complex Number Calculator

This is a simple implementation of complex numbers basic functionality in case complex nubers are not supported from python. 

## General Info 
The app have a simple stracture where in the class ComplexNum under the folder app we have implement a new type. 
It is taking as arguments two numbers, the first one represent the real part of a complex nuber and the second the imaginary part. 
We have overload the basic math operators to achive a more "native" functionality.


    pythonComplex
    |
    |---app
    |    |---ComplexNum.py
    |
    |---test
    |    |---ComplexCalcTest.py
    |
    |---main.py
    
    
## How To
The main.py file contains some simple exaples of how we can use the app, a simple exaple is listed below:

    cn1 = ComplexNum(3, 7)
    cn2 = ComplexNum(3, 7)
    cn1 + cn2

    output: 
    6+14j



ComplexCalcTest.py contains some unit test for the verifiction of the basic functionality of the application. 
If we want to run the integration tests from CLI we have to type in the root folder of the project: 

    nosetests test/ComplexCalcTest.py
    
## Miscellaneous
If there is some problem with current python venv or you want to run the app outside of the venv you should install only the nose lybraty for the integration tests. 

    pip install nose
