# 🎄 Day 5: Print Queue

## 🖨️ The Safety Manual Crisis

### 📍 The Printing Department
Satisfied with their search on Ceres, the squadron of scholars suggests subsequently scanning the stationery stacks of sub-basement 17.

The North Pole printing department is busier than ever this close to Christmas, and while The Historians continue their search of this historically significant facility, an Elf operating a very familiar printer beckons you over.

### 📝 The Print Order Problem
The Elf must recognize you, because they waste no time explaining that the new sleigh launch safety manual updates won't print correctly. Failure to update the safety manuals would be dire indeed, so you offer your services.

#### 📋 Print Rules
Safety protocols clearly indicate that new pages for the safety manuals must be printed in a very specific order. The notation X|Y means that if both page number X and page number Y are to be produced as part of an update, page number X must be printed at some point before page number Y.

#### 🔍 Sample Input
The Elf has for you both the page ordering rules and the pages to produce in each update (your puzzle input), but can't figure out whether each update has the pages in the right order.

For example:
```txt
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
```

### 🧩 Understanding the Rules

#### 📜 Page Order Rules
The first section specifies the page ordering rules, one per line. The first rule, 47|53, means that if an update includes both page number 47 and page number 53, then page number 47 must be printed at some point before page number 53. (47 doesn't necessarily need to be immediately before 53; other pages are allowed to be between them.)

#### 📊 Update Sequences
The second section specifies the page numbers of each update. Because most safety manuals are different, the pages needed in the updates are different too. The first update, 75,47,61,53,29, means that the update consists of page numbers 75, 47, 61, 53, and 29.

### 🔍 Example Analysis
In the above example, the first update (75,47,61,53,29) is in the right order:

- 75 is correctly first because there are rules that put each other page after it: 75|47, 75|61, 75|53, and 75|29.
- 47 is correctly second because 75 must be before it (75|47) and every other page must be after it according to 47|61, 47|53, and 47|29.
- 61 is correctly in the middle because 75 and 47 are before it (75|61 and 47|61) and 53 and 29 are after it (61|53 and 61|29).
- 53 is correctly fourth because it is before page number 29 (53|29).
- 29 is the only page left and so is correctly last.

#### 🎯 Validation Rules
- The second and third updates are also in the correct order according to the rules
- The fourth update, 75,97,47,61,53, violates rule 97|75
- The fifth update, 61,13,29, breaks rule 29|13
- The last update breaks several rules

### 📊 Middle Page Numbers
The correctly-ordered updates are:
```txt
75,47,61,53,29
97,61,53,29,13
75,29,13
```
These have middle page numbers of 61, 53, and 29 respectively. Adding these page numbers together gives 143.

### ⭐️ Your Task
Determine which updates are already in the correct order. What do you get if you add up the middle page number from those correctly-ordered updates?

[View Solution (part1)](./day5_pt1.py) 💻

---

## 🔄 Part Two: Fixing the Order

### 🛠️ The Challenge
While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.

### 📋 Correcting the Sequences
For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:

```txt
75,97,47,61,53 becomes 97,75,47,61,53
61,13,29 becomes 61,29,13
97,13,75,29,47 becomes 97,75,47,29,13
```

After taking only the incorrectly-ordered updates and ordering them correctly, their middle page numbers are 47, 29, and 47. Adding these together produces 123.

### ⭐️ Your Task
Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?

[View Solution (part2)](./day5_pt2.py) 💻

references: *Advent of Code 2024*, [Day 5: Print Queue](https://adventofcode.com/2024/day/5)
