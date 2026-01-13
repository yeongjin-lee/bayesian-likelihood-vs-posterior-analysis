# Empirical Analysis of Likelihood and Posterior in a Bayesian Toy Model

This project investigates the difference between likelihood-based and posterior-based inference in a simple Bayesian setting using theoretical derivations and Monte Carlo simulation.

---

## Motivation

In Bayesian statistics, two related but distinct quantities are often confused:

- **Likelihood** P(x | θ): how well data x is explained by parameter θ  
- **Posterior** P(θ | x): how probable θ is after observing data x and applying prior belief

While likelihood reflects data fit, posterior reflects belief after combining data with prior knowledge. This distinction becomes important when data is limited or when prior information is meaningful.

---

## Jelly Toy Model

We define a simple probabilistic world where each jelly has two attributes: color and taste.  
Four combinations exist, each with equal probability 0.25.

Random draws from this distribution simulate sampling from a true likelihood function.

By increasing the number of draws, we empirically observe convergence of the estimated likelihood to the true probability distribution.

---

## Monte Carlo Simulation

A Monte Carlo sampler repeatedly draws jellies according to the true probability model and counts empirical frequencies. As the number of samples increases, these frequencies converge to the true likelihood.

This provides an experimental verification of statistical consistency.

---

## Bayesian Interpretation

While likelihood converges with enough data, posterior inference may differ depending on prior assumptions.  
The poster discusses this distinction and illustrates how MAP and MLE can lead to different parameter estimates in Bayesian models.

---

## Academic Context

This work was conducted as part of the **MCS (Mathematics & Computer Science)** academic seminar at Seoul Women’s University and presented as a poster.

The goal was not to propose a new algorithm, but to develop a rigorous, intuitive understanding of Bayesian inference through theory and experiment.
