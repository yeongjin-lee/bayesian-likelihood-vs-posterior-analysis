# Bayesian Likelihood vs Posterior

This repository contains a small Monte Carlo simulation and an academic poster illustrating the difference between **likelihood** and **posterior** in Bayesian inference.

The project was developed as part of an academic **Mathematics & Computer Science (MCS)** seminar.

---

## What is this?

We study a simple probabilistic toy model (a jelly-drawing experiment) to show how:

- empirical **likelihood** converges as more data is observed,
- **posterior** inference incorporates prior information and can differ from likelihood.

The goal is to make Bayesian reasoning visually and experimentally intuitive.

---

## Repository

├── jelly_simulation.py # Monte Carlo sampler

└── poster/

├── poster.pdf # MCS academic poster

└── summary.md # Extended explanation


---

## Running the simulation

```bash
python jelly_simulation.py
This will sample jellies from a known probability distribution and report empirical frequencies.

