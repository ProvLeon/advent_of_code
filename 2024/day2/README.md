# 🎄 Day 2: Red-Nosed Reports

## 🔬 The Nuclear Mystery

### 🏭 The Red-Nosed Reactor
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

### 📊 The Data Dilemma
They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

#### 📈 Sample Reports
The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:
```txt
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```
This example data contains six reports each containing five levels.

### 🔍 Safety Analysis Rules
The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

- 📈 The levels are either all increasing or all decreasing
- 🔢 Any two adjacent levels differ by at least one and at most three

#### 📋 Example Analysis:
- `7 6 4 2 1`: ✅ Safe because the levels are all decreasing by 1 or 2
- `1 2 7 8 9`: ❌ Unsafe because 2 7 is an increase of 5
- `9 7 6 2 1`: ❌ Unsafe because 6 2 is a decrease of 4
- `1 3 2 4 5`: ❌ Unsafe because 1 3 is increasing but 3 2 is decreasing
- `8 6 4 4 1`: ❌ Unsafe because 4 4 is neither an increase or a decrease
- `1 3 6 7 9`: ✅ Safe because the levels are all increasing by 1, 2, or 3

In this example, 2 reports are safe.

### ⭐️ Your Task
Analyze the unusual data from the engineers. How many reports are safe?

[View Solution](/day2_pt1.py) 💻

## 🔄 Part Two: The Problem Dampener

### 🛠️ New Safety Feature
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

### 📊 Updated Analysis Rules
Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

#### 📋 Revised Example Analysis:
- `7 6 4 2 1`: ✅ Safe without removing any level
- `1 2 7 8 9`: ❌ Unsafe regardless of which level is removed
- `9 7 6 2 1`: ❌ Unsafe regardless of which level is removed
- `1 3 2 4 5`: ✅ Safe by removing the second level, 3
- `8 6 4 4 1`: ✅ Safe by removing the third level, 4
- `1 3 6 7 9`: ✅ Safe without removing any level

Thanks to the Problem Dampener, 4 reports are actually safe!

### ⭐️ Your Task
Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?

[View Solution](/day2_pt2.py) 💻

references: *Advent of Code 2024*, [Day 2: Red-Nosed Reports](https://adventofcode.com/2024/day/2)