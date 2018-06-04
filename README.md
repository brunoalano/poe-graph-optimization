PoE Optimizer
&middot;
[![Latest Github release](https://img.shields.io/github/release/brunoalano/poe-graph-optimization.svg)](https://github.com/brunoalano/poe-graph-optimization/releases/latest)
[![Build status of the master branch on Linux/OSX](https://img.shields.io/travis/brunoalano/poe-graph-optimization/master.svg?label=Linux%20%2F%20OSX%20build)](https://travis-ci.org/brunoalano/poe-graph-optimization)
[![Chat on Gitter](https://img.shields.io/gitter/room/brunoalano/poe-graph-optimization.svg?colorB=753a88)](https://gitter.im/brunoalano/poe-graph-optimization)
=====

Backpropagation in Graph (DAG) Structure for Attribute Maximization focused on __Path of Exile__ Skill Tree.


## Features
* Calculates local-optima for a DAG using the `g2o` library with a custom loss function.
* It can find **optimal direct path** given a set of constraints\*.
* Updated PoE Skill Tree _(current: 3.3)_.
* Skill Attribute Parsing using different set of techniques.

__PoEGO__ is available for **Python** using:

```bash
$ pip install poego
```

## Contents
- [Features](#features)
- [Loss Function](#loss-function)
- [Regularization Options](#regularization-options)
- [Constraints](#constraints)
- [Data](#data)

## Loss Function

The main point of the optimization algorithm it's based on the set of global
attributes of the Skill Tree _(see: `poego/attributes/definition.py`)_.

[!log-min-nonlinear](https://latex.codecogs.com/gif.latex?w%5E*%3D%5Ctext%7Bargmin%7D_w%5Csum_%7Bi%3D1%7D%5En%5Cpsi%5Cleft%28y_i-%5Csum_%7Bj%3D1%7D%5Enx_%7Bij%7Dw_j%5Cright%29)

Given that `x_{i,j}` it's a non-linear constraint.

## Regularization Options

TODO

## Constraints

TODO

## Data

The data was provided by __[PoE Skill Tree](https://github.com/PoESkillTree/PoESkillTree/releases)__ under the MIT License.
