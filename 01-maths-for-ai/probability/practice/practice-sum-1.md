# 🎯 Practice Sum 1 — Colored Balls in a Bag

**Problem Statement**:

A bag contains:
- 3 Red balls  
- 5 Blue balls  
- 2 Green balls  

One ball is drawn **at random** from the bag.

Answer the following:

---

## Q1. What is the probability of drawing a red ball?

### ✅ Solution:

Total balls = 3 (Red) + 5 (Blue) + 2 (Green) = **10**

\[
P(\text{Red}) = \frac{\text{Number of Red balls}}{\text{Total number of balls}} = \frac{3}{10}
\]

---

## Q2. What is the probability of drawing a blue **or** green ball?

This is a **union** of two events: Blue ∪ Green

\[
P(\text{Blue or Green}) = P(\text{Blue}) + P(\text{Green}) = \frac{5}{10} + \frac{2}{10} = \frac{7}{10}
\]

---

## Q3. What is the probability of **not** drawing a blue ball?

This is the **complement** of drawing a blue ball.

\[
P(\text{Not Blue}) = 1 - P(\text{Blue}) = 1 - \frac{5}{10} = \frac{5}{10} = \frac{1}{2}
\]

---

## Q4. If the drawn ball is **not red**, what is the probability that it is green?

This is a **conditional probability**:

Let:
- Event A = ball is green
- Event B = ball is not red

We need \( P(A \mid B) \)

First, total non-red balls = 5 (Blue) + 2 (Green) = 7

\[
P(\text{Green | Not Red}) = \frac{P(\text{Green and Not Red})}{P(\text{Not Red})} = \frac{2}{7}
\]

---

## Q5. What is the probability of drawing a ball that is **either red or green**?

\[
P(\text{Red or Green}) = P(\text{Red}) + P(\text{Green}) = \frac{3}{10} + \frac{2}{10} = \frac{5}{10} = \frac{1}{2}
\]

---

## ✅ Summary Table

| Event                          | Probability |
|-------------------------------|-------------|
| Drawing a red ball            | 3/10        |
| Drawing a blue or green ball  | 7/10        |
| Not drawing a blue ball       | 1/2         |
| Green given not red           | 2/7         |
| Red or green ball             | 1/2         |

---

> 📌 **Tip**: Always break total count and favorable count carefully. Conditional probability narrows down your sample space.

