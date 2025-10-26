# Algorithm Patterns Cheatsheet

> Click a section header to expand/collapse each pattern.

---

## 🔁 Two Pointers

<details>
<summary>Opposite Ends (one array)</summary>

```python
def fn(arr):
    left = ans = 0
    right = len(arr) - 1

    while left < right:
        # do some logic here with left and right
        if CONDITION:
            left += 1
        else:
            right -= 1

    return ans
