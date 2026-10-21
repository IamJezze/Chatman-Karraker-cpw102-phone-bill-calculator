# Test Cases

Run each case separately. Determine the expected results by hand before running your program.

From the repository folder, run:

```text
python 03_execution/data_bill.py
```

Check the usage message, overage amount when applicable, and total bill. Paste each terminal run as evidence, then mark Pass or Fail and explain why.

## Case 1: At the data limit

- Data used (GB): 10
- Base plan cost: 40

**Expected results:**
Shown that input for at usage is correct.

**Evidence (paste your terminal run):**

```
How much data was used (in GB)? : 10
What is the base cost of the plan? : 40
Usage status: AT LIMIT.
You have reached the 10 GB limit.
Total cost: $40.00
```

**Pass / Fail and why:**
PASS

## Case 2: At 5 GB over the limit

- Data used (GB): 15
- Base plan cost: 40

**Expected results:**
Shown that the user is now at a moderate overage and how much they've incurred with their overage.

**Evidence (paste your terminal run):**

```text
How much data was used (in GB)? : 15
What is the base cost of the plan? : 40
Usage status: MODERATE OVERAGE.
You are 5.00 GB over the limit.
Extra charges: $10.00
Total cost: $50.00
```

**Pass / Fail and why:**
PASS

## Case 3: Above 5 GB over the limit

- Data used (GB): 15.5
- Base plan cost: 50

**Expected results:**
Shown that the user is highly over their limit.

**Evidence (paste your terminal run):**

```
How much data was used (in GB)? : 15.5
What is the base cost of the plan? : 40
Usage status: HIGH OVERAGE.
You are 5.50 GB over the limit.
Extra charges: $11.00
Total cost: $51.00
```

**Pass / Fail and why:**
PASS

If a case fails, fix the program and add evidence of the rerun below that case.
