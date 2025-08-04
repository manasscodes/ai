# 🧩 Practice Sum 2 — Mutually Exclusive vs. Independent Events

**Problem Statement**:

A card is drawn at random from a standard deck of **52 playing cards**.

Define the following events:
- Event A: Drawing a **heart**
- Event B: Drawing a **king**

Answer the following:

---

## Q1. Are events A and B mutually exclusive?

### ✅ Solution:

- Event A: All 13 hearts in the deck → includes **King of Hearts**
- Event B: All 4 kings → includes **King of Hearts**

Since **King of Hearts** is common to both A and B:

\[
A \cap B = \{\text{King of Hearts}\} \neq \emptyset
\]

🔸 **Conclusion**: A and B are **not mutually exclusive**

---

## Q2. What is the probability of drawing a heart or a king? \( P(A \cup B) \)

### ✅ Solution:

Use the formula:

\[
P(A \cup B) = P(A) + P(B) - P(A \cap B)
\]

- \( P(A) = \frac{13}{52} \)
- \( P(B) = \frac{4}{52} \)
- \( P(A \cap B) = \frac{1}{52} \) (King of Hearts)

\[
P(A \cup B) = \frac{13}{52} + \frac{4}{52} - \frac{1}{52} = \frac{16}{52} = \frac{4}{13}
\]

---

## Q3. Suppose two cards are drawn **with replacement**.  
Let:
- Event A: First card is a spade
- Event B: Second card is a red card

Are A and B independent?

### ✅ Solution:

Since replacement is used, the second draw does **not depend** on the first.

So A and B are **independent**.

Check with probabilities:

- \( P(A) = \frac{13}{52} = \frac{1}{4} \)
- \( P(B) = \frac{26}{52} = \frac{1}{2} \)
- \( P(A \cap B) = P(A) \cdot P(B) = \frac{1}{4} \cdot \frac{1}{2} = \frac{1}{8} \)

✅ Verified:  
\[
P(A \cap B) = P(A) \cdot P(B)
\]

🔸 **Conclusion**: Events are **independent**

---

## Q4. Suppose now the cards are drawn **without replacement**. Are the events still independent?

### ✅ Solution:

Without replacement, the total number of cards reduces on the second draw, so the probabilities change.

Thus, the second draw **depends on the first**.

🔸 **Conclusion**: A and B are **not independent** (they are **dependent** events)

---

## Q5. What is the probability of drawing two kings in two draws **without replacement**?

Let:
- First draw = King → \( \frac{4}{52} \)
- Second draw = King → \( \frac{3}{51} \)

\[
P(\text{2 Kings}) = \frac{4}{52} \cdot \frac{3}{51} = \frac{12}{2652} = \frac{1}{221}
\]

---

## ✅ Summary Table

| Question                         | Answer                         |
|----------------------------------|--------------------------------|
| A and B mutually exclusive?      | ❌ No                          |
| \( P(A \cup B) \)                | 4/13                           |
| A and B independent (with repl.) | ✅ Yes                         |
| A and B independent (no repl.)   | ❌ No                          |
| Probability (2 kings, no repl.)  | 1/221                          |

---

> 📌 **Key Idea**:  
> - **Mutually exclusive** → Cannot happen together  
> - **Independent** → Can happen together, but one does not affect the other  

