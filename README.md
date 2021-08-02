# Prefix notation calculator

### Background
I was set the challenge of writing a [prefix notation](https://en.wikipedia.org/wiki/Polish_notation) calculator. 

Having never seen the notation before I got a bit caught up in getting my head around the system and didn't progess as much as far as I would have liked in the time allotted. This repo provides a more complete solution to the test than I produced at the time. 

The complication in the challenge was to allow the user to inject variables into expressions. Where variables are provided the program should return the highest possible value. Variables take the form `{'x': (1, 5)}` where the tuple denotes the lower and upper limit of a range of values.

### Development

- There are unit tests for pretty much every function.
- To run tests just use `poetry run pytest`. 

###  Installation / running
- I use poetry for dependency management. Clone the repo and run `poetry install`
- To run the evaluator use `poetry run python main.py`
- You'll be prompted to provide an expression. 

### Incomplete bits
- I perform a basic validation on the expression provided but can think of cases where invalid expression would be counted as valid (e.g. `1 2 +`). I'd like to do some fancier validation.
- Refactoring - things can always be tidier and better named! 
- I quite like Makefiles as a simple way of recording