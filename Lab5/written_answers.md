# Lab 5: Written Answers

Name: Jonah Brisson

---

## Problem 1 (2 pts)

**Which loop-control part is broken in the book's never-ending loop?** The test is broken because the number increases by 2 each time, skipping over 6 and never meeting the condition to stop.

**What change in your 1a guarantees termination?** I changed the loop so that once the number reaches or passes the limit, the loop stops instead of continuing forever.

---

## Problem 3 (3 pts)

| Product | `solve_ages` result | One, none, or many answers? |
|---:|---|---|
|  |  |  |
|  |  |  |
|  |  |  |

**Which Polya phase is writing the functions? Which phase is trying other products?** Writing the functions is the carrying out the plan phase because we are putting our algorithm into code. Trying other products is the looking back phase because we are testing our solution with different inputs to see how it works.

---

## Problem 4 (7 pts)

**1. Prediction (written BEFORE running):** the list after outer passes 1–4.

Starting list: Marisol, Dev, Quinn, Abel, Tamsin, Jonah, Beatriz, Ollie, Keiko, Hugo, Ingrid, Ezra
pass 1: Dev, Marisol, Quinn, Abel, Tamsin, Jonah, Beatriz, Ollie, Keiko, Hugo, Ingrid, Ezra
pass 2: Dev, Marisol, Quinn, Abel, Tamsin, Jonah, Beatriz, Ollie, Keiko, Hugo, Ingrid, Ezra
pass 3: Abel, Dev, Marisol, Quinn, Tamsin, Jonah, Beatriz, Ollie, Keiko, Hugo, Ingrid, Ezra
pass 4: Abel, Dev, Marisol, Quinn, Tamsin, Jonah, Beatriz, Ollie, Keiko, Hugo, Ingrid, Ezra


**Actual output (copied from the run):**
Before: ['Marisol', 'Dev', 'Quinn', 'Abel', 'Tamsin', 'Jonah', 'Beatriz', 'Ollie', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Dev', 'Marisol', 'Quinn', 'Abel', 'Tamsin', 'Jonah', 'Beatriz', 'Ollie', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Dev', 'Marisol', 'Quinn', 'Abel', 'Tamsin', 'Jonah', 'Beatriz', 'Ollie', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Abel', 'Dev', 'Marisol', 'Quinn', 'Tamsin', 'Jonah', 'Beatriz', 'Ollie', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Abel', 'Dev', 'Marisol', 'Quinn', 'Tamsin', 'Jonah', 'Beatriz', 'Ollie', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Abel', 'Dev', 'Jonah', 'Marisol', 'Quinn', 'Tamsin', 'Beatriz', 'Ollie', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Abel', 'Beatriz', 'Dev', 'Jonah', 'Marisol', 'Quinn', 'Tamsin', 'Ollie', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Abel', 'Beatriz', 'Dev', 'Jonah', 'Marisol', 'Ollie', 'Quinn', 'Tamsin', 'Keiko', 'Hugo', 'Ingrid', 'Ezra']
['Abel', 'Beatriz', 'Dev', 'Jonah', 'Keiko', 'Marisol', 'Ollie', 'Quinn', 'Tamsin', 'Hugo', 'Ingrid', 'Ezra']
['Abel', 'Beatriz', 'Dev', 'Hugo', 'Jonah', 'Keiko', 'Marisol', 'Ollie', 'Quinn', 'Tamsin', 'Ingrid', 'Ezra']
['Abel', 'Beatriz', 'Dev', 'Hugo', 'Ingrid', 'Jonah', 'Keiko', 'Marisol', 'Ollie', 'Quinn', 'Tamsin', 'Ezra']
['Abel', 'Beatriz', 'Dev', 'Ezra', 'Hugo', 'Ingrid', 'Jonah', 'Keiko', 'Marisol', 'Ollie', 'Quinn', 'Tamsin']
After:  ['Abel', 'Beatriz', 'Dev', 'Ezra', 'Hugo', 'Ingrid', 'Jonah', 'Keiko', 'Marisol', 'Ollie', 'Quinn', 'Tamsin']

**2. Loop control in your code**

| Loop | Initialize | Test | Modify |
|---|---|---|---|
| Outer | i = 1 | 1 > len(items) | i increases by 1 |
| Inner | j = i -1 | j <= 0 and items [j] > pivot | j -= 1 |

**3. Why "greater than" and not "greater than or equal to"?** What changed with `["Fay", "Al", "Fay", "Bo"]`? We use > instead of >= because we don't want to move names that are equal. With ["Fay", "Al", "Fay", "Bo"], the final alphabetical order stays the same, but using >= would switch the order of the two Fays. Using > keeps them in their original order.

---

## Problem 5 (6 pts)

**1. Predictions vs. results**

| Target | On roster? | Predicted `visited` | Actual `visited` |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

**2. Base cases:**

**3. Number of activations when "Gideon" is found:**

**4. An unsorted list and target where binary search fails:**

---

## Problem 6 (10 pts)

**Insertion sort table (paste):**

```text
```

**Binary search table (paste):**

```text
```

1. Do best and worst cases match the formulas exactly?

2. How close is the shuffled count to the average-case estimate?

3. What happens to the work when n doubles (insertion sort vs. binary search)?

4. Why does binary search make the registrar's 30,000-record search feel instant?

5. A real situation where data arrives almost sorted:
