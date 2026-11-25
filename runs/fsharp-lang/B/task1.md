# F# Bank Account Model - Task 1

## Overview

This project implements a bank account system in F# with deposits, withdrawals, and an overdraft rule.

## The F# Program

```fsharp
// Bank.fs - Bank account model

type Account = {
    Owner: string
    Balance: decimal
    OverdraftLimit: decimal
}

let createAccount owner initialBalance overdraftLimit = {
    Owner = owner
    Balance = initialBalance
    OverdraftLimit = -overdraftLimit  // Store as negative number
}

/// Deposit money into the account
let deposit (account: Account) amount = {
    account with
    Balance = account.Balance + amount
}

/// Withdraw money from the account
/// Returns the updated account or None if withdrawal would exceed overdraft limit
let withdraw (account: Account) amount =
    let newBalance = account.Balance - amount
    if newBalance >= account.OverdraftLimit then
        Some { account with Balance = newBalance }
    else
        None

/// Get a string representation of the account
let toString (account: Account) =
    sprintf "Account for %s: Balance = $%.2f (Overdraft limit: $%.2f)" 
        account.Owner account.Balance (-account.OverdraftLimit)

/// Main function to demonstrate the bank account
[<EntryPoint>]
let main argv =
    // Create an account for Alice with $100 balance and $50 overdraft limit
    let aliceAccount = createAccount "Alice" 100m 50m
    
    // Print initial state
    printfn "%s" (toString aliceAccount)
    
    // Try some deposits
    let afterDeposit = deposit aliceAccount 50m
    printfn "After depositing $50:%s" (toString afterDeposit)
    
    // Try some withdrawals
    let afterWithdrawal = withdraw afterDeposit 30m
    match afterWithdrawal with
    | Some acc -> printfn "After withdrawing $30:%s" (toString acc)
    | None -> printfn "Withdrawal declined: would exceed overdraft limit"
    
    // Try overdraft
    let overLimit = withdraw (defaultArg afterWithdrawal aliceAccount) 130m
    match overLimit with
    | Some acc -> printfn "After withdrawing $130 (overdraft):%s" (toString acc)
    | None -> printfn "Withdrawal declined: would exceed overdraft limit"
    
    // Try excessive withdrawal
    let excessive = withdraw aliceAccount 1000m
    match excessive with
    | Some acc -> printfn "After withdrawing $1000:%s" (toString acc)
    | None -> printfn "Withdrawal declined: would exceed overdraft limit"
    
    0 // Return an exit code
```

## Building and Running

### Prerequisites

- [.NET SDK](https://dotnet.microsoft.com/download) (version 8.0 or later recommended)
- F# compiler (included with .NET SDK)

### Build

```bash
dotnet new console -n BankAccount --language F#
cd BankAccount
# Replace Program.fs with the code above
```

Or from the command line with the existing file:

```bash
dotnet fsi .\Bank.fs
```

### Run

```bash
dotnet run
```

Expected output:

```
Account for Alice: Balance = $100.00 (Overdraft limit: $50.00)
After depositing $50:Account for Alice: Balance = $150.00 (Overdraft limit: $50.00)
After withdrawing $30:Account for Alice: Balance = $120.00 (Overdraft limit: $50.00)
After withdrawing $130 (overdraft):Account for Alice: Balance = $-10.00 (Overdraft limit: $50.00)
Withdrawal declined: would exceed overdraft limit
```

## Design Decisions

1. **Overdraft as negative limit**: The overdraft limit is stored as a negative number (`-50`) so that the check `newBalance >= overdraftLimit` correctly allows withdrawals down to the overdraft limit.

2. **`withdraw` returns `Option<Account>`**: This functional pattern makes it explicit when a withdrawal is declined due to the overdraft rule, forcing the caller to handle the case.

3. **Immutable data with record updates**: Each operation returns a new `Account` record rather than mutating the existing one, following F# functional programming conventions.