# byterun_exercise

## forLoop.py
```
_> python forLoop.py
```
  3           0 LOAD_CONST               1 (0)
              2 STORE_FAST               0 (x)

  4           4 SETUP_LOOP              24 (to 30)
              6 LOAD_GLOBAL              0 (range)
              8 LOAD_CONST               2 (5)
             10 CALL_FUNCTION            1
             12 GET_ITER
        >>   14 FOR_ITER                12 (to 28)
             16 STORE_FAST               0 (x)

  5          18 LOAD_FAST                0 (x)
             20 LOAD_CONST               3 (1)
             22 INPLACE_ADD
             24 STORE_FAST               0 (x)
             26 JUMP_ABSOLUTE           14
        >>   28 POP_BLOCK

  6     >>   30 LOAD_FAST                0 (x)
             32 RETURN_VALUE
## whileLoop.py
```
_> python whileLoop.py
```
  3           0 LOAD_CONST               1 (0)
              2 STORE_FAST               0 (x)

  4           4 SETUP_LOOP              20 (to 26)
        >>    6 LOAD_FAST                0 (x)
              8 LOAD_CONST               2 (5)
             10 COMPARE_OP               0 (<)
             12 POP_JUMP_IF_FALSE       24

  5          14 LOAD_FAST                0 (x)
             16 LOAD_CONST               3 (1)
             18 INPLACE_ADD
             20 STORE_FAST               0 (x)
             22 JUMP_ABSOLUTE            6
        >>   24 POP_BLOCK

  6     >>   26 LOAD_CONST               0 (None)
             28 RETURN_VALUE

## elif.py
```
_> python elif.py
```
  3           0 LOAD_CONST               1 (0)
              2 STORE_FAST               0 (x)

  4           4 LOAD_FAST                0 (x)
              6 LOAD_CONST               1 (0)
              8 COMPARE_OP               4 (>)
             10 POP_JUMP_IF_FALSE       18

  5          12 LOAD_CONST               2 (1)
             14 STORE_FAST               0 (x)
             16 JUMP_FORWARD            18 (to 36)

  6     >>   18 LOAD_FAST                0 (x)
             20 LOAD_CONST               1 (0)
             22 COMPARE_OP               0 (<)
             24 POP_JUMP_IF_FALSE       32

  7          26 LOAD_CONST               2 (1)
             28 STORE_FAST               0 (x)
             30 JUMP_FORWARD             4 (to 36)

  9     >>   32 LOAD_CONST               1 (0)
             34 STORE_FAST               0 (x)
        >>   36 LOAD_CONST               0 (None)
             38 RETURN_VALUE


