# Simple Spinning Wheel<br>![GitHub last commit (branch)](https://img.shields.io/github/last-commit/Nuggew/Simple-Spinning-Wheel/main)
A simple open-source cool spinning bar for your python Windows Terminal programs :)

## Guide
### Installation
Download the file ```spinningwheel.py``` and import in your script.
```python
# Example
import spinningwheel as sw

[...]
```

### Creating a Spinning Bar
```python
# Example
import spinningwheel as sw
import time

wheel = sw.SpinningWheel(msg="YOUR MESSAGE HERE...", color=(255,0,0)) # OBS.: Only RGB color scheme is supported!
wheel.start()

time.sleep(10)
wheel.stop()
```

### Creating a Progress Bar
```python
# Example
import spinningwheel as sw
import time

pb = sw.ProgressBar(value=0, showPercentage=False, msg="") # OBS.: Only values from 0 to 1 are allowed!
pb.show()

for i in range(101):
  pb.set(i/100)
  time.sleep(0.1)
```