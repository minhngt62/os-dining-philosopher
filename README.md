# Dining Philosopher Problem

In computer science, **the dining philosophers problem** [[1]](https://en.wikipedia.org/wiki/Dining_philosophers_problem) is an example problem often used in concurrent algorithm design to illustrate synchronization issues and techniques for resolving them. 
It was originally formulated in 1965 by Edsger Dijkstra as a student exam exercise, presented in terms of computers competing for access to tape drive peripherals.

Five philosophers dine together at the same table. Each philosopher has their own place at the table. There is a fork between each plate. The dish served is a kind of spaghetti which has to be eaten with two forks. Each philosopher can only alternately think and eat. Moreover, a philosopher can only eat their spaghetti when they have both a left and right fork. Thus two forks will only be available when their two nearest neighbors are thinking, not eating. After an individual philosopher finishes eating, they will put down both forks. The problem is how to design a regimen (a concurrent algorithm) such that no philosopher will starve; i.e., each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to eat or think.

The problem was designed to illustrate the challenges of avoiding deadlock, a system state in which no progress is possible. To see that a proper solution to this problem is not obvious, consider a proposal in which each philosopher is instructed to behave as follows:

```
- think until the left fork is available; when it is, pick it up;
- think until the right fork is available; when it is, pick it up;
- when both forks are held, eat for a fixed amount of time;
- put the left fork down;
- put the right fork down;
- repeat from the beginning.
```

However, they each will think for an undetermined amount of time and may end up holding a left fork thinking, staring at the right side of the plate, unable to eat because there is no right fork, until they starve. Therefore, a valid process synchronization solution has to handle such deadlock cases as well as tackling other sequence and access problems

**For more details, please read the report provided in folder [`docs`](https://github.com/minhngt62/os-dining-philosopher/tree/main/docs).**

<p align="center">
  <img src="https://user-images.githubusercontent.com/86721208/218491029-e246d361-4130-46b7-a5e0-7d65ca511303.jpg" />
</p>

## Operating Systems - DSAI K65: Topic 10
1. Nguyễn Tống Minh (Email: minh.nt204885@sis.hust.edu.vn)
2. Nguyễn Công Đạt (Email: dat.nc200137@sis.hust.edu.vn)
3. Nguyễn Trung Hiếu (Email: hieu.nt204877@sis.hust.edu.vn)
4. Ngô Thị Thu Huyền (Email: huyen.ntt200289@sis.hust.edu.vn)

## Project Structure

```
dining_philosophers         # source code
-- ./gui/                   # UI and event handler
-- ./solutions/             # backends - solutions' implementation
-- ./forks.py               # implemented for fork objects in the problem statement
-- ./philosophers.py        # implemented for philosopher objects in the problem statement
-- ./table.py               # problem mode
docs                        # project report
README.md           
```
---

# Setup

To run the program (through [`main.py`](https://github.com/minhngt62/os-dining-philosopher/blob/main/main.py) (terminal version) or [`app.py`](https://github.com/minhngt62/os-dining-philosopher/blob/main/app.py) (GUI version)), `Python 3` is required.

1. Install [`Python 3`](https://www.python.org/downloads/) (above $3.6$).
2. Change the working directory to the project root.
3. Run the program (suggested):
    ```
    python -m app
    ```
    
# Guideline

<p align="center">
  <img src="https://user-images.githubusercontent.com/86721208/218496714-f786a9ed-1e3d-4533-ac11-036cc446ac7d.png" />
</p>
