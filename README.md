# PyMath

- [Commands](https://github.com/eggsnham07/pymath#commands)
- [Syntax](https://github.com/eggsnham07/pymath#syntax)
- [Installation](https://github.com/eggsnham07/pymath#installation)

### Commands:
- `pymath`
- - add: usage: `pymath add 12.5 12.5`
- - sub: usage: `pymath sub 25 12.5`
- - div: usage: `pymath div 144 12`
- - mult: usage: `pymath mult 12 12`
- - sqr: usage: `pymath sqr 49`
- - gui: usage: `pymath gui`

### Syntax:
The pymath command can multipy/divide/subract/add with only `mult*` or `div*` or `sub*` or `add*` replacing `*` with anything, for example: `pymath divydodad 144 12` and the output will be 12

### Installation
***Only*** compatible with **linux** at the time of writing!

Run the command below:

```shell
cd ~/Downloads
git clone https://github.com/eggsnham07/pymath
cd pymath
chmod +x ./setup.sh
./setup.sh
```

Add `export PATH=$PATH:~/.local/bin/pymath` to `~/.bashrc` to use `pymath` command via cli
