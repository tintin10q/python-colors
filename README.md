# python-colors
Python colors output.

This is a module that assigns terminal ansi formatting codes to variables. So it is an abstraction above the whole '\033[xx' thing.

Most formatting codes are implemented. 

The module tries to check automatically if colors are supported. If colors are not supported than the color codes turn into empty strings.
This means that users on non color supported terminals do not see anything.

There is also a printc function mainly for testing where it automatically puts a STOP at the end of the print.

```python

from colors import *

printc(RED + 'Yo! this color is red!')

print(f'''{RED}Is it red?{STOP}{GREEN}{BLINK}Am I blinking{STOP_BLINK}?{STOP}''')
# Question mark should not blink.
```

I hope this is use full for you!