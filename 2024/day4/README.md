# 🎄 Day 4: Ceres Search

## 🔍 The Search Continues

### 📍 The Ceres Station
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

### 📝 The Word Search Challenge
As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

#### 🎯 Search Rules
This word search allows words to be:
- Horizontal
- Vertical
- Diagonal
- Written backwards
- Even overlapping other words

It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them.

#### 📊 Pattern Examples
Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

```txt
..X...
.SAMX.
.A..A.
XMAS.S
.X....
```

### 🧩 Sample Puzzle
The actual word search will be full of letters instead. For example:
```txt
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```

In this word search, XMAS occurs a total of 18 times. Here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

```txt
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
```

### ⭐️ Your Task
Take a look at the little Elf's word search. How many times does XMAS appear?

[View Solution (part1)](./day4_pt1.py) 💻

---

## 🔄 Part Two: The X-MAS Pattern

### 🤔 A Misunderstanding
The Elf looks quizzically at you. Did you misunderstand the assignment?

### 📜 The Real Instructions
Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X.

#### 📋 Pattern Format
One way to achieve that is like this:
```txt
M.S
.A.
M.S
```
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

#### 🔍 Example Analysis
Here's the same example from before, but this time all of the X-MASes have been kept instead:
```txt
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
```
In this example, an X-MAS appears 9 times.

### ⭐️ Your Task
Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?

[View Solution (part2)](./day4_pt2.py) 💻

references: *Advent of Code 2024*, [Day 4: Ceres Search](https://adventofcode.com/2024/day/4)
