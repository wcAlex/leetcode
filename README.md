# 🧠 Algorithm Patterns Cheatsheet

> A compact, collapsible collection of key coding interview templates  
> (Python + JavaScript) — fully GitHub-compatible.

---

## 🔁 Two Pointers

<details>
<summary><b>One Input — Opposite Ends</b></summary>

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
<summary><b>Two Inputs — Exhaust Both</b></summary>

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
            # do logic here to add arr[right] to curr

            while WINDOW_CONDITION_BROKEN:
                # remove arr[left] from curr
                left += 1

            # update ans

        return ans

**JavaScript**

    let fn = arr => {
        let left = 0, ans = 0, curr = 0;

        for (let right = 0; right < arr.length; right++) {
            // do logic here to add arr[right] to curr

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

## 🔤 Efficient String Building

<details>
<summary><b>Concatenate Characters</b></summary>

**Python**

    # arr is a list of characters
    def fn(arr):
        ans = []
        for c in arr:
            ans.append(c)
        return "".join(ans)

**JavaScript**

    // arr is a list of characters
    let fn = arr => {
        let ans = [];
        for (const c of arr) ans.push(c);
        return ans.join("");
    };

    // or, faster concatenation
    let fn = arr => {
        let ans = "";
        for (const c of arr) ans += c;
        return ans;
    };

> 💡 In JavaScript, `+=` concatenation is often faster than `.join()`.

</details>

---

## 🔗 Linked List

<details>
<summary><b>Fast and Slow Pointers</b></summary>

**Python**

    def fn(head):
        slow = head
        fast = head
        ans = 0
        while fast and fast.next:
            # do logic
            slow = slow.next
            fast = fast.next.next
        return ans

**JavaScript**

    let fn = head => {
        let slow = head, fast = head, ans = 0;
        while (fast && fast.next) {
            // do logic
            slow = slow.next;
            fast = fast.next.next;
        }
        return ans;
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
        let curr = head, prev = null;
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

## 📊 Subarray Counting / Prefix + Hash Map

<details>
<summary><b>Count Subarrays Meeting Criteria</b></summary>

**Python**

    from collections import defaultdict
    def fn(arr, k):
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0
        for num in arr:
            # do logic to change curr
            ans += counts[curr - k]
            counts[curr] += 1
        return ans

**JavaScript**

    let fn = (arr, k) => {
        let counts = new Map(); counts.set(0, 1);
        let ans = 0, curr = 0;
        for (const num of arr) {
            // do logic to change curr
            ans += counts.get(curr - k) || 0;
            counts.set(curr, (counts.get(curr) || 0) + 1);
        }
        return ans;
    };

</details>

---

## 🧱 Monotonic Stack

<details>
<summary><b>Increasing Stack Template</b></summary>

**Python**

    def fn(arr):
        stack = []
        ans = 0
        for num in arr:
            while stack and stack[-1] > num:
                # do logic
                stack.pop()
            stack.append(num)
        return ans

**JavaScript**

    let fn = arr => {
        let stack = [], ans = 0;
        for (const num of arr) {
            while (stack.length && stack[stack.length - 1] > num) {
                // do logic
                stack.pop();
            }
            stack.push(num);
        }
        return ans;
    };

</details>

---

## 🌲 Binary Tree Traversals

<details>
<summary><b>DFS (Recursive)</b></summary>

**Python**

    def dfs(root):
        if not root: return
        ans = 0
        # do logic
        dfs(root.left)
        dfs(root.right)
        return ans

**JavaScript**

    let dfs = root => {
        if (!root) return;
        let ans = 0;
        // do logic
        dfs(root.left);
        dfs(root.right);
        return ans;
    };

</details>

---

<details>
<summary><b>DFS (Iterative)</b></summary>

**Python**

    def dfs(root):
        stack = [root]
        ans = 0
        while stack:
            node = stack.pop()
            # do logic
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return ans

**JavaScript**

    let dfs = root => {
        let stack = [root], ans = 0;
        while (stack.length) {
            let node = stack.pop();
            // do logic
            if (node.left) stack.push(node.left);
            if (node.right) stack.push(node.right);
        }
        return ans;
    };

</details>

---

<details>
<summary><b>BFS (Level Order)</b></summary>

**Python**

    from collections import deque
    def fn(root):
        queue = deque([root])
        ans = 0
        while queue:
            current_length = len(queue)
            # do logic for current level
            for _ in range(current_length):
                node = queue.popleft()
                # do logic
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return ans

**JavaScript**

    let fn = root => {
        let queue = [root], ans = 0;
        while (queue.length) {
            let currentLength = queue.length;
            let nextQueue = [];
            // do logic for current level
            for (let i = 0; i < currentLength; i++) {
                let node = queue[i];
                // do logic
                if (node.left) nextQueue.push(node.left);
                if (node.right) nextQueue.push(node.right);
            }
            queue = nextQueue;
        }
        return ans;
    };

</details>

---

## 🌐 Graph Traversal

<details>
<summary><b>DFS (Recursive)</b></summary>

**Python**

    def fn(graph):
        def dfs(node):
            ans = 0
            # do some logic
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            return ans
        seen = {START_NODE}
        return dfs(START_NODE)

**JavaScript**

    let fn = graph => {
        let seen = new Set([START_NODE]);
        let dfs = node => {
            let ans = 0;
            // do some logic
            for (const neighbor of graph[node]) {
                if (!seen.has(neighbor)) {
                    seen.add(neighbor);
                    ans += dfs(neighbor);
                }
            }
            return ans;
        };
        return dfs(START_NODE);
    };

</details>

---

<details>
<summary><b>DFS (Iterative) and BFS</b></summary>

**Python – DFS Iterative**

    def fn(graph):
        stack = [START_NODE]
        seen = {START_NODE}
        ans = 0
        while stack:
            node = stack.pop()
            # do some logic
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return ans

**Python – BFS**

    from collections import deque
    def fn(graph):
        queue = deque([START_NODE])
        seen = {START_NODE}
        ans = 0
        while queue:
            node = queue.popleft()
            # do some logic
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return ans

**JavaScript**

    // DFS iterative
    let fn = graph => {
        let stack = [START_NODE], seen = new Set([START_NODE]), ans = 0;
        while (stack.length) {
            let node = stack.pop();
            // do some logic
            for (const neighbor of graph[node]) {
                if (!seen.has(neighbor)) {
                    seen.add(neighbor);
                    stack.push(neighbor);
                }
            }
        }
        return ans;
    };

    // BFS
    let bfs = graph => {
        let queue = [START_NODE], seen = new Set([START_NODE]), ans = 0;
        while (queue.length) {
            let next = [];
            for (const node of queue) {
                // do some logic
                for (const neighbor of graph[node]) {
                    if (!seen.has(neighbor)) {
                        seen.add(neighbor);
                        next.push(neighbor);
                    }
                }
            }
            queue = next;
        }
        return ans;
    };

</details>

---

## 🧮 Heap / Top-K Elements

<details>
<summary><b>Using Heap in Python</b></summary>

**Python**

    import heapq
    def fn(arr, k):
        heap = []
        for num in arr:
            # push according to criteria
            heapq.heappush(heap, (CRITERIA, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for num in heap]

**JavaScript**

    /*
    JavaScript lacks a built-in heap.
    Consider using Python or C++ for heap-based problems.
    */

</details>

---

## ⚡ Binary Search Patterns

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

<details>
<summary><b>Left-Most / Right-Most Insertion Points</b></summary>

**Python**

    # Left-most
    def fn(arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] >= target: right = mid
            else: left = mid + 1
        return left

    # Right-most
    def fn(arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > target: right = mid
            else: left = mid + 1
        return left

**JavaScript**

    // Left-most
    let leftMost = (arr, target) => {
        let left = 0, right = arr.length;
        while (left < right) {
            let mid = Math.floor((left + right) / 2);
            if (arr[mid] >= target) right = mid;
            else left = mid + 1;
        }
        return left;
    };

    // Right-most
    let rightMost = (arr, target) => {
        let left = 0, right = arr.length;
        while (left < right) {
            let mid = Math.floor((left + right) / 2);
            if (arr[mid] > target) right = mid;
            else left = mid + 1;
        }
        return left;
    };

</details>

---

<details>
<summary><b>Binary Search for Greedy Problems</b></summary>

**Python**

    # Find minimum
    def fn():
        def check(x): return BOOLEAN
        left, right = MINIMUM, MAXIMUM
        while left <= right:
            mid = (left + right) // 2
            if check(mid): right = mid - 1
            else: left = mid + 1
        return left

    # Find maximum
    def fn():
        def check(x): return BOOLEAN
        left, right = MINIMUM, MAXIMUM
        while left <= right:
            mid = (left + right) // 2
            if check(mid): left = mid + 1
            else: right = mid - 1
        return right

**JavaScript**

    // Minimum
    let minSearch = check => {
        let left = MINIMUM, right = MAXIMUM;
        while (left <= right) {
            let mid = Math.floor((left + right) / 2);
            if (check(mid)) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    };

    // Maximum
    let maxSearch = check => {
        let left = MINIMUM, right = MAXIMUM;
        while (left <= right) {
            let mid = Math.floor((left + right) / 2);
            if (check(mid)) left = mid + 1;
            else right = mid - 1;
        }
        return right;
    };

</details>

---

## 🔄 Backtracking / Dynamic Programming

<details>
<summary><b>Backtracking Template</b></summary>

**Python**

    def backtrack(curr, *args):
        if BASE_CASE:
            # modify answer
            return
        for choice in CHOICES:
            # choose
            backtrack(curr, *args)
            # undo

**JavaScript**

    let backtrack = curr => {
        if (BASE_CASE) return;
        for (const choice of CHOICES) {
            // choose
            backtrack(curr);
            // undo
        }
    };

</details>

---

<details>
<summary><b>Top-Down DP (Memoization)</b></summary>

**Python**

    def fn(arr):
        memo = {}
        def dp(state):
            if state in memo: return memo[state]
            if BASE_CASE: return 0
            ans = RECURRENCE(state)
            memo[state] = ans
            return ans
        return dp(STATE_FOR_WHOLE_INPUT)

**JavaScript**

    let fn = arr => {
        let memo = {};
        let dp = state => {
            if (state in memo) return memo[state];
            if (BASE_CASE) return 0;
            let ans = RECURRENCE(state);
            memo[state] = ans;
            return ans;
        };
        return dp(STATE_FOR_WHOLE_INPUT);
    };

</details>

---

## 🌳 Trie Construction
