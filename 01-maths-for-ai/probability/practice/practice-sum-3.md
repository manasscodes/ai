# 📐 Practice Sum 3 — Bayes' Theorem: Disease Testing Example

**Problem Statement**:

A certain disease affects **0.5%** of the population. A medical test is available to detect the disease and has the following accuracy:
- If a person **has** the disease, the test is **98%** accurate (true positive rate)
- If a person **does not** have the disease, the test is **95%** accurate (true negative rate)

Let’s define the events:
- D = Person has the disease  
- D' = Person does **not** have the disease  
- T = Test result is positive

Answer the following using **Bayes’ Theorem**:

---

## Q1. What is the probability that a person **actually has the disease**, given that the test result is **positive**?

### ✅ Solution:

We are asked to find:

\[
P(D \mid T) = \frac{P(T \mid D) \cdot P(D)}{P(T)}
\]

#### Step 1: Assign known values

- \( P(D) = 0.005 \)
- \( P(D') = 0.995 \)
- \( P(T \mid D) = 0.98 \) (true positive)
- \( P(T \mid D') = 0.05 \) (false positive = 1 - true negative)

---

#### Step 2: Compute total probability of a positive test \( P(T) \)

\[
P(T) = P(T \mid D) \cdot P(D) + P(T \mid D') \cdot P(D')
\]

\[
P(T) = (0.98 \cdot 0.005) + (0.05 \cdot 0.995) = 0.0049 + 0.04975 = 0.05465
\]

---

#### Step 3: Apply Bayes’ Theorem

\[
P(D \mid T) = \frac{0.98 \cdot 0.005}{0.05465} = \frac{0.0049}{0.05465} \approx 0.0897
\]

\[
\boxed{P(D \mid T) \approx 8.97\%}
\]

---

## Q2. What is the probability that a person **does not have** the disease, given that the test result is **positive**?

This is \( P(D' \mid T) \)

Using:

\[
P(D' \mid T) = \frac{P(T \mid D') \cdot P(D')}{P(T)} = \frac{0.05 \cdot 0.995}{0.05465} \approx \frac{0.04975}{0.05465} \approx 0.9103
\]

\[
\boxed{P(D' \mid T) \approx 91.03\%}
\]

---

## Q3. Intuition Behind the Result

Even though the test is **98% accurate**, the disease is **rare (0.5%)**. So most positive tests actually come from healthy people — this is why the **posterior probability** of having the disease given a positive test is still **low (~9%)**.

🔍 This shows why **base rate** matters — and **why AI systems must adjust for real-world priors**.

---

## ✅ Summary Table

| Quantity                        | Value       |
|---------------------------------|-------------|
| P(Disease | Positive)           | ~8.97%      |
| P(No Disease | Positive)        | ~91.03%     |
| Test Accuracy (Positive case)   | 98%         |
| Test Accuracy (Negative case)   | 95%         |
| Prior Probability of Disease    | 0.5%        |

---

## 🔄 Recap of Bayes' Formula:

\[
P(H \mid E) = \frac{P(E \mid H) \cdot P(H)}{P(E)}
\]

Where:
- \( H \): Hypothesis (e.g., has disease)
- \( E \): Evidence (e.g., test result)
- \( P(H) \): Prior
- \( P(E \mid H) \): Likelihood
- \( P(E) \): Evidence probability

---

> 📌 **Real-World Insight**: This example is directly applicable to AI systems that deal with classification, prediction, and uncertainty reasoning.

