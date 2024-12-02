# 🎄 Day 1: Historian Hysteria

## 🔍 The Mystery of the Missing Chief Historian

The Chief Historian, an essential figure at the annual Christmas sleigh launch, has mysteriously vanished for months. Reports indicate he was last seen investigating historically significant locations around the North Pole. A distinguished group of Senior Historians has requested your assistance in their search mission.

### 🎯 The Challenge
- **Goal**: Collect 50 stars by checking potential locations ⭐️
- **Deadline**: Before Santa's December 25th departure 🎅
- **Method**: Solve daily puzzles (two per day) to earn stars 🧩
- **Note**: Second puzzle unlocks after completing the first 🔓

## 📖 Part One: The Search Begins

### 🏃‍♂️ Initial Investigation
The Elvish Senior Historians encounter their first obstacle before the search even begins - their location checklist is empty. The team decides to start at the most logical place: the Chief Historian's office.

### 💡 The Discovery
While the Chief Historian remains absent, the office yields an unexpected treasure trove: detailed notes and lists of historically significant locations. These locations are identified not by names, but by unique numerical IDs.

### ⚔️ The Challenge
To be thorough, the Historians divide into two groups, each compiling their own list of location IDs. However, a concerning discrepancy emerges when comparing the lists side-by-side.

#### 📊 Sample Data
```txt
3   4
4   3
2   5
1   3
3   9
3   3
```

### 📝 Analysis Method
The task is to quantify the differences between the lists by:
1. 📍 Pairing numbers from smallest to largest
2. 📏 Calculating the distance between each pair
3. ➕ Summing all distances

#### 🔢 Example Analysis
1. Pair 1: 1 (left) vs 3 (right) = Distance 2
2. Pair 2: 2 (left) vs 3 (right) = Distance 1
3. Pair 3: 3 (left) vs 3 (right) = Distance 0
4. Pair 4: 3 (left) vs 4 (right) = Distance 1
5. Pair 5: 3 (left) vs 5 (right) = Distance 2
6. Pair 6: 4 (left) vs 9 (right) = Distance 5

**Total Distance**: 2 + 1 + 0 + 1 + 2 + 5 = `11`

### ✨ Your Task
Calculate the total distance between your actual left and right lists.

[Solution for part 1](./day1_pt1.py) 💻



## 🔄 Part Two: A Different Perspective

### 🕵️‍♂️ The Plot Thickens
Initial analysis confirms the lists' differences, but a crucial observation emerges: many location IDs appear in both lists. Could some numbers be misinterpreted handwriting rather than actual location IDs?

### 📊 New Approach: Similarity Score
Calculate how frequently each number from the left list appears in the right list, then multiply and sum to find the total similarity score.

#### 📈 Sample Data
```txt
3   4
4   3
2   5
1   3
3   9
3   3
```

#### 🧮 Similarity Score Calculation
1. 3 (appears 3 times): 3 * 3 = 9
2. 4 (appears 1 time): 4 * 1 = 4
3. 2 (appears 0 times): 2 * 0 = 0
4. 1 (appears 0 times): 1 * 0 = 0
5. 3 (appears 3 times): 3 * 3 = 9
6. 3 (appears 3 times): 3 * 3 = 9

**Total Similarity Score**: 9 + 4 + 0 + 0 + 9 + 9 = `31`

### 🎉 Your Task
Calculate the similarity score for your complete lists.

[Solution for part 2](./day1_pt2.py) 💻
