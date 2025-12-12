
# 🔢 Numbers & Bases Toolkit (Python)

*A compact toolkit for base conversions, arithmetic across bases, and two’s complement negative values.*

---

## 📚 Overview

This project provides Python utilities for:

1. **Base → Decimal**: Convert a number in base `b` to base 10.  
2. **Decimal → Base**: Convert a base 10 integer to any target base.  
3. **Add Across Bases**: Add two numbers given in their respective bases.  
4. **Two’s Complement Negative**: Given a binary string and a digit width, return its negative value (as a binary string) in **two’s complement** with the same width.

All functions include examples and tests.

---

## ✨ Features

- Supports bases **2 to 36** (digits `0-9` and letters `A-Z`/`a-z`).  
- Raises clear errors on invalid digits/base mismatches.  
- Handles **signed** decimal inputs when converting to/from bases.  
- Provides two’s complement negation with fixed bit width.
