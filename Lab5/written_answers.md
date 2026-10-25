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
| Kenji | Yes | Priya, Isadora, Malik, Kenji | Priya, Harper, Lucia, Jasper, Kenji |
| Priya | Yes | Priya | Priya |
| Gideon | Yes | Priya, Harper, Dahlia, Farah, Gideon | Priya, Harper, Dahlia, Farah, Gideon |

**2. Base cases:** 
if not items: returns False because there's nothing left to search.
if items[mid] == target: returns True because the target has been found.

**3. Number of activations when "Gideon" is found:**
5 activations. Each activation checks one middle entry, and Gideon is found on the fifth check.

**4. An unsorted list and target where binary search fails:**
An unsorted list like [2, 9, 4, 7, 1] with a target of 9 causes binary search to fail. It checks 4 first and searches the right half because 9 > 4, even though 9 is in the left half. It eventually returns False even though 9 is in the list.

---

## Problem 6 (10 pts)

**Insertion sort table (paste):**

```text
   n | sorted     n-1| reversed (n^2-n)/2| shuffled  (n^2-n)/4
   10|      9       9|       45        45|       27       22.5
   20|     19      19|      190       190|      146       95.0
   40|     39      39|      780       780|      414      390.0
   80|     79      79|     3160      3160|     1766     1580.0
  160|    159     159|    12720     12720|     6309     6360.0
  320|    319     319|    51040     51040|    25558    25520.0
```

**Binary search table (paste):**

```text
n      | max visited | log2(n)
15     |      4      |  3.91
100    |      7      |  6.64
200    |      8      |  7.64
1000   |      10     |  9.97
30000  |      15     |  14.87
100000 |      17     |  16.61
```

1. Do best and worst cases match the formulas exactly?
Yes, both the best and worst cases match the formulas exactly. The sorted lists followed n - 1 comparisons, and the reversed lists followed (n² - n) / 2 comparisons.

2. How close is the shuffled count to the average-case estimate?
The shuffled counts were pretty close to the average-case estimates, especially for larger lists. There were some differences because the shuffled lists were randomly arranged, but the estimates were generally accurate.

3. What happens to the work when n doubles (insertion sort vs. binary search)?
When n doubles, insertion sort takes about four times as many comparisons in the worst case, while binary search only needs about one additional check. Binary search handles larger lists much more efficiently.

4. Why does binary search make the registrar's 30,000-record search feel instant?
Binary search makes searching 30,000 records feel almost instant because it cuts the remaining list in half with each check. Instead of searching through thousands of records one by one, it only needed a maximum of 15 checks in our experiment.

5. A real situation where data arrives almost sorted:
A real example would be a school adding a new student to an already alphabetized roster. Most of the names are already in order, so only the new student's name needs to be placed in the correct position.
