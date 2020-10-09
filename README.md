# Problem

Calculate the fuel based on the masses of modules

## Input

txt file with masses (whole numbers)
formula: fuel = sum over all modules (round_down (mass of the module / 3) - 2)

## Output

amount of fuel

# Approaches

## Approach 1

1. Read txt file
1. Store each line (one number) as an integer in a list
1. Calculate the fuel for each module (seperate function)1
1. Sum all fuels
1. Print sum

## Approach 2

1. Use Generator to read each line (one module mass)
1. Calculate the fuel for the module
1. Add it to the total fuel needed
1. Print total fuel

## Approach 3

1. Read txt file
1. Store each line (one number) as an integer in a list
1. Use List comprehension to calculate a list of fuels
1. Sum all fuels
1. Print

## Approach 4

1. Read the lines in batches (combine 2 & 3)

# Design tradeoffs (best to worst, expected)

- time to implement: 1, 3, 2
- memory: 2, 3, 1
- performance (small data): 3, 1, 2
- performance (big data): 2, 3, 1
- readability: ?

# Potential add-ons

- check if each input is valid (typeof(int))
- performance and memory optimization
