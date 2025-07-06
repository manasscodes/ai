# 🧮 Linear Algebra for Machine Learning

This file contains detailed notes from the **Linear Algebra** module in the Coursera course *Mathematics for Machine Learning and Data Science* by DeepLearning.AI.

---

## 📘 Why Linear Algebra?

Linear Algebra is the **foundation of machine learning**. It helps describe data, model parameters, and computations like transformations and optimizations.

---

## 🧱 1. Vectors and Scalars

### ➤ Scalar

* A **single number**, e.g., `x = 3`
* Notation: lowercase letter, e.g., `x`

### ➤ Vector

* An **ordered list of numbers**
* Represents direction and magnitude
* Notation: bold lowercase `**v**` or `\vec{v}`

Example:

```
v = [2, 5, 7]ᵀ  →  3D column vector
```

### Vector Operations

* **Addition**: element-wise
* **Scalar multiplication**: each element × scalar
* **Dot product**: `v • w = v₁w₁ + v₂w₂ + ... + vₙwₙ`
* **Norm**: length of a vector `||v||`

---

## 🧱 2. Matrices

### ➤ Matrix

* A **2D array of numbers**, size `m × n`
* Notation: capital letter `A`

Example:

```
A = [ [1, 2], [3, 4] ]  → 2×2 matrix
```

### Matrix Operations

* **Addition**: shape must match
* **Multiplication**: `A (m×n) × B (n×p) = C (m×p)`
* **Transpose**: `Aᵀ` flips rows and columns

---

## 🌀 3. Linear Transformations

A matrix can represent a **transformation** on a vector:

```
A * x = y
```

This transformation can be:

* Rotation
* Scaling
* Reflection
* Projection

---

## 🧩 4. Systems of Linear Equations

Solving equations like:

```
Ax = b
```

Where:

* `A` is a matrix
* `x` is the variable vector
* `b` is the result vector

**Goal**: Find `x`

---

## ⚙️ 5. Inverse & Identity Matrix

* **Identity Matrix (I)**: `I * A = A`
* **Inverse Matrix (A⁻¹)**: `A⁻¹ * A = I`

  * Not all matrices have an inverse
  * Used to solve `Ax = b` → `x = A⁻¹b`

---

## 🧠 6. Eigenvalues & Eigenvectors

If `A * v = λ * v`, then:

* `v` is an **eigenvector**
* `λ` is the **eigenvalue**

Used in:

* PCA (Principal Component Analysis)
* Dimensionality reduction
* Stability analysis

---

## 🧰 Tools Used

* NumPy for coding
* Desmos / GeoGebra for visualizations

---

## 🔄 Summary

Linear Algebra gives you the **language of ML**: vectors = data, matrices = models. Understanding operations on them is key to working with neural networks, transformations, and optimizations.

Next Up: **Calculus for Machine Learning** → derivatives, gradients, and optimization!
