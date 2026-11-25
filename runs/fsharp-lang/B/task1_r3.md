# F# Bank Account - Task 1, Repeat 3

## Overview

This project models a bank account with deposits, withdrawals, and an overdraft rule using F#.

## The F# Program

Create a file named `bank_account.fsx` with the following content:

```fsharp
// bank_account.fsx - F# Bank Account Model

type Account = {
    Owner: string
    Balance: decimal
    OverdraftLimit: decimal
}

let createAccount owner initialBalance overdraftLimit = {
    Owner = owner
    Balance = initialBalance
    OverdraftLimit = -(float overheadLimit)  // stored as negative number
}

/// Deposit money into the account
let deposit (account: Account) amount = 
    if amount <= 0m then
        printfn "Error: Deposit amount must be positive"
        account
    else
        let newBalance = account.Balance + amount
        { account with Balance = newBalance }
        |> printfn "Deposited %A, new balance: %A" amount

/// Withdraw money from the account, respecting overdraft rule
let withdraw (account: Account) amount = 
    if amount <= 0m then
        printfn "Error: Withdrawal amount must be positive"
        account
    elif account.Balance - amount < account.OverdraftLimit then
        printfn "Error: Insufficient funds. Overdraft limit is %A" account.OverdraftLimit
        account
    else
        let newBalance = account.Balance - amount
        { account with Balance = newBalance }
        |> printfn "Withdrew %A, new balance: %A" amount

/// Check if withdrawal is allowed
let canWithdraw (account: Account) amount = 
    account.Balance - amount >= account.OverdraftLimit

/// Display account info
let displayAccount account = 
    printfn "Account: %s" account.Owner
    printfn "Balance: %A" account.Balance
    printfn "Overdraft Limit: %A" account.OverdraftLimit
    printfn "-------------------"

[<EntryPoint>]
let main argv = 
    // Create a new account for "Alice" with $100 balance and -$50 overdraft limit
    let aliceAccount = createAccount "Alice" 100m (-50m)
    
    printfn "=== Initial Account State ==="
    displayAccount aliceAccount
    
    // Test deposits
    printfn "=== Making Deposits ==="
    let afterDeposit = deposit aliceAccount 50m
    
    printfn "=== Making Withdrawals ==="
    // Valid withdrawal within balance
    let afterWithdraw1 = withdraw afterDeposit 30m
    
    // Withdrawal that goes to overdraft limit
    let afterWithdraw2 = withdraw afterWithdraw1 100m  // Should fail: would go below -50
    
    // Smaller withdrawal after the failed one
    let afterWithdraw3 = withdraw afterWithdraw1 20m
    
    printfn "=== Final Account State ==="
    displayAccount afterWithdraw3
    
    0 // return an integer exit code
```

## Building and Running

### Using .NET SDK

1. Install the .NET 8 SDK or later from https://dotnet.microsoft.com/download
2. Save the F# code above to `bank_account.fsx`
3. Run the script with:
   ```bash
   dotnet run --project bank_account.fsx
   ```
   Or using `fsharpi`:
   ```bash
   fsharpi bank_account.fsx
   ```

### Expected Output

```
=== Initial Account State ===
Account: Alice
Balance: 100
Overdraft Limit: -50
-------------------
=== Making Deposits ===
Deposited 50, new balance: 150
=== Making Withdrawals ===
Withdrew 30, new balance: 120
Error: Insufficient funds. Overdraft limit is -50
Withdrew 20, new balance: 100
=== Final Account State ===
Account: Alice
Balance: 100
Overdraft Limit: -50
-------------------
```