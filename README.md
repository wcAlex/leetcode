# 🧠 Algorithm Patterns Cheatsheet

> Clean collapsible Markdown reference for key coding interview templates  
> (Python + JavaScript) — 100 % GitHub compatible.

---

## 🔁 Two Pointers

<details>
<summary><b>Opposite Ends (one array)</b></summary>

**Python**

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

**JavaScript**

    let fn = arr => {
        let left = 0, ans = 0, right = arr.length - 1;
        while (left < right) {
            // do some logic here with left and right
            if (CONDITION) {
                left++;
            } else {
                right--;
            }
        }
        return ans;
    };

</details>

---

<details>
<summary><b>Two Inputs (exhaust both arrays)</b></summary>

**Python**

    def fn(arr1, arr2):
        i = j = ans = 0
        while i < len(arr1) and j < len(arr2):
            # do some logic here
            if CONDITION:
                i += 1
            else:
                j += 1
        while i < len(arr1):
            # do logic
            i += 1
        while j < len(arr2):
            # do logic
            j += 1
        return ans

**JavaScript**

    let fn = (arr1, arr2) => {
        let i = 0, j = 0, ans = 0;
        while (i < arr1.length && j < arr2.length) {
            // do some logic here
            if (CONDITION) i++;
            else j++;
        }
        while (i < arr1.length) i++;
        while (j < arr2.length) j++;
        return ans;
    };

</details>

---

## 🪟 Sliding Window

<details>
<summary><b>Standard Sliding Window</b></summary>

**Python**

    def fn(arr):
        left = ans = curr = 0
        for right in range(len(arr)):
            # add arr[right] to curr
            while WINDOW_CONDITION_BROKEN:
                # remove arr[left] from curr
                left += 1
            # update ans
        return ans

**JavaScript**

    let fn = arr => {
        let left = 0, ans = 0, curr = 0;
        for (let right = 0; right < arr.length; right++) {
            // add arr[right] to curr
            while (WINDOW_CONDITION_BROKEN) {
                // remove arr[left] from curr
                left++;
            }
            // update ans
        }
        return ans;
    };

</details>

---

## ➕ Prefix Sum

<details>
<summary><b>Build Prefix Sum Array</b></summary>

**Python**

    def fn(arr):
        prefix = [arr[0]]
        for i in range(1, len(arr)):
            prefix.append(prefix[-1] + arr[i])
        return prefix

**JavaScript**

    let fn = arr => {
        let prefix = [arr[0]];
        for (let i = 1; i < arr.length; i++) {
            prefix.push(prefix[prefix.length - 1] + arr[i]);
        }
        return prefix;
    };

</details>

---

## 🔗 Linked List

<details>
<summary><b>Fast & Slow Pointer</b></summary>

**Python**

    def fn(head):
        slow = head
        fast = head
        while fast and fast.next:
            # do logic
            slow = slow.next
            fast = fast.next.next

**JavaScript**

    let fn = head => {
        let slow = head;
        let fast = head;
        while (fast && fast.next) {
            // do logic
            slow = slow.next;
            fast = fast.next.next;
        }
    };

</details>

---

<details>
<summary><b>Reverse Linked List</b></summary>

**Python**

    def fn(head):
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

**JavaScript**

    let fn = head => {
        let curr = head;
        let prev = null;
        while (curr) {
            let nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }
        return prev;
    };

</details>

---

## 📊 Monotonic Stack

<details>
<summary><b>Increasing Stack Template</b></summary>

**Python**

    def fn(arr):
        stack = []
        for num in arr:
            while stack and stack[-1] > num:
                # do logic
                stack.pop()
            stack.append(num)

**JavaScript**

    let fn = arr => {
        let stack = [];
        for (const num of arr) {
            while (stack.length && stack[stack.length - 1] > num) {
                // do logic
                stack.pop();
            }
            stack.push(num);
        }
    };

</details>

---

## 🌲 Tree Traversal

<details>
<summary><b>DFS (Recursive)</b></summary>

**Python**

    def dfs(root):
        if not root:
            return
        # do logic
        dfs(root.left)
        dfs(root.right)

**JavaScript**

    let dfs = root => {
        if (!root) return;
        // do logic
        dfs(root.left);
        dfs(root.right);
    };

</details>

---

<details>
<summary><b>BFS (Level Order)</b></summary>

**Python**

    from collections import deque
    def fn(root):
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                # do logic
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

**JavaScript**

    let fn = root => {
        let queue = [root];
        while (queue.length) {
            let n = queue.length, next = [];
            for (let i = 0; i < n; i++) {
                let node = queue[i];
                // do logic
                if (node.left) next.push(node.left);
                if (node.right) next.push(node.right);
            }
            queue = next;
        }
    };

</details>

---

## 🌐 Graph Traversal

<details>
<summary><b>DFS (Recursive)</b></summary>

**Python**

    def fn(graph):
        def dfs(node):
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        seen = {START_NODE}
        dfs(START_NODE)

**JavaScript**

    let fn = graph => {
        let seen = new Set([START_NODE]);
        let dfs = node => {
            for (const nei of graph[node]) {
                if (!seen.has(nei)) {
                    seen.add(nei);
                    dfs(nei);
                }
            }
        };
        dfs(START_NODE);
    };

</details>

---

<details>
<summary><b>BFS</b></summary>

**Python**

    from collections import deque
    def fn(graph):
        queue = deque([START_NODE])
        seen = {START_NODE}
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append(nei)

**JavaScript**

    let fn = graph => {
        let queue = [START_NODE];
        let seen = new Set([START_NODE]);
        while (queue.length) {
            let node = queue.shift();
            for (const nei of graph[node]) {
                if (!seen.has(nei)) {
                    seen.add(nei);
                    queue.push(nei);
                }
            }
        }
    };

</details>

---

## ⚡ Binary Search

<details>
<summary><b>Standard Binary Search</b></summary>

**Python**

    def fn(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

**JavaScript**

    let fn = (arr, target) => {
        let left = 0, right = arr.length - 1;
        while (left <= right) {
            let mid = Math.floor((left + right) / 2);
            if (arr[mid] === target) return mid;
            if (arr[mid] > target) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    };

</details>

---

## 🔄 Backtracking / DP

<details>
<summary><b>Backtracking Template</b></summary>

**Python**

    def backtrack(curr):
        if BASE_CASE:
            # modify answer
            return
        for choice in CHOICES:
            # choose
            backtrack(curr)
            # unchoose

**JavaScript**

    let backtrack = curr => {
        if (BASE_CASE) return;
        for (const choice of CHOICES) {
            // choose
            backtrack(curr);
            // unchoose
        }
    };

</details>

---

<details>
<summary><b>Top-Down DP (Memoization)</b></summary>

**Python**

    def fn():
        memo = {}
        def dp(state):
            if state in memo: return memo[state]
            if BASE_CASE: return 0
            memo[state] = RECURRENCE(state)
            return memo[state]
        return dp(START_STATE)

**JavaScript**

    let fn = () => {
        let memo = new Map();
        let dp = state => {
            if (memo.has(state)) return memo.get(state);
            if (BASE_CASE) return 0;
            let ans = RECURRENCE(state);
            memo.set(state, ans);
            return ans;
        };
        return dp(START_STATE);
    };

</details>

---

### ✅ Usage

- Works on **GitHub** and **VS Code Preview**
- Every section collapses cleanly — no syntax conflicts  
- Print or export to PDF for offline review
