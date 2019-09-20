
all:
	python context_to_lattice.py

t: tests
tests:
	python -m pytest context_to_lattice.py
