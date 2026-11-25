# F# Bank Account - Task 1 Repeat 2

## Overview

This deliverable demonstrates an F# program that models a bank account with deposits, withdrawals, and an overdraft rule. The program was built and run using the .NET 8 F# toolchain.

## F# Program

The program is located at `/home/hatch/workspace/persona-null-paper/runs/fsharp-lang/C/BankAccount/Program.fs` and implements:

- **`BankAccount` record** - Immutable record with `Owner`, `Balance`, `OverdraftRule`, and `AllowedOverdraftLimit` fields
- **`createAccount` function** - Creates a new bank account with specified owner, initial balance, and overdraft rule
- **`deposit` function** - Adds funds to the account (validates positive amount)
- **`withdraw` function** - Removes funds with overdraft rule enforcement:
  - `NoOverdraft` rule: cannot go below zero balance
  - `AllowOverdraft` rule: allows withdrawals up to the overdraft limit
- **`displayState` function** - Prints account state including balance and overdraft status

## Key Features

1. **Discriminated unions** for transaction types and account state
2. **Immutable record types** with functional updates
3. **Exhaustive pattern matching** on overdraft rules
4. **Input validation** at function boundaries
5. **Explicit error handling** with descriptive messages

## Example Usage

The `main` function demonstrates:

1. Creating two accounts:
   - Alice: 100 balance with AllowOverdraft rule
   - Bob: 50 balance with NoOverdraft rule

2. Performing operations:
   - Deposit 50 into Alice's account
   - Withdraw 30 from Alice's account
   - Attempt withdrawal of 150 from Alice (exceeds overdraft - expected error)
   - Attempt withdrawal of 60 from Bob (insufficient funds - expected error)

## Build and Run Commands

```bash
# Navigate to the project directory
cd /home/hatch/workspace/persona-null-paper/runs/fsharp-lang/C/BankAccount

# Build the project
dotnet build

# Run the program
dotnet run
```

## Output

The program produces console output showing:

- Initial account states for Alice and Bob
- Account state after each deposit/withdrawal
- Error messages for failed withdrawal attempts (overdraft exceeded, insufficient funds)

## Verification

- Build command: `dotnet build` - exit code 0 (success)
- The F# program follows the [fsharp-lang.SKILL.md](home/hatch/workspace/persona-null-paper/skills/fsharp-lang.SKILL.md) canonical skill requirements
- Uses discriminated unions and records for domain modeling
- Pure functions with IO pushed to the edge
- Exhaustive pattern matching on all code paths