Python 3.8.6rc1 (tags/v3.8.6rc1:08bd63d, Sep  7 2020, 23:10:23) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t=turtle.Turtle()
>>> t.shape('turtle')
>>> t.circle(100)
>>> t.shape('Hi')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t.shape('Hi')
  File "C:\Users\Happiness\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named Hi
>>> t.write('Hi')
>>> t.forward(200)
t
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.color('green')
>>> t.circle(10)
>>> t.begin_fill()
>>> t.forward(100)
>>> t.right(120)
>>> t.forwar(100)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    t.forwar(100)
AttributeError: 'Turtle' object has no attribute 'forwar'
>>> t.forward(100)
>>> t.right(240)
>>> t.right(120)
>>> t.left(240)
>>> t.forward(100)
>>> t.end_fill
<bound method RawTurtle.end_fill of <turtle.Turtle object at 0x0000023FCDCB2340>>
>>> t.end_fill()
>>> 