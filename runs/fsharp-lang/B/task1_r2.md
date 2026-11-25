# F# Bank Account Model - Task 1 Repeat 2

This deliverable demonstrates an F# program modeling a bank account with deposits, withdrawals, and an overdraft rule.

## The F# Program

```fsharp
(* Bank account module with deposit, withdrawal, and overdraft rule *)
module BankAccount

    type Account = {
        Owner: string
        Balance: decimal
        OverdraftLimit: decimal
    }

    let create owner initialBalance overdraftLimit = {
        Owner = owner
        Balance = initialBalance
        OverdraftLimit = overdraftLimit
    }

    let deposit (acc: Account) amount =
        if amount <= 0m then
            failwith "Deposit amount must be positive"
        { acc with Balance = acc.Balance + amount }

    let withdraw (acc: Account) amount =
        if amount <= 0m then
            failwith "Withdrawal amount must be positive"
        let newBalance = acc.Balance - amount
        if newBalance < acc.OverdraftLimit then
            failwith(sprintf "Insufficient funds: attempted to withdraw %s from overdraft-protected account with limit %s" (String of decimal amount) (String of decimal acc.OverdraftLimit))
        { acc with Balance = newBalance }

    let letOverdraft (acc: Account) amount =
        (* Allow withdrawal even if it goes below overdraft limit, for comparison *)
        { acc with Balance = acc.Balance - amount }

    let printAccount (acc: Account) =
        printf "Account Owner: %s\n" acc.Owner
        printf "Current Balance: %s\n" (String of decimal acc.Balance)
        printf "Overdraft Limit: %s\n" (String of decimal acc.OverdraftLimit)
        printf "-----------------------------\n"

    // Example usage
    let example () =
        let acc = create "Alice" 100m (-50m)
        printf "=== Initial State ===\n"
        printAccount acc

        let accAfterDeposit = deposit acc 50m
        printf "=== After Depositing 50 ===\n"
        printAccount accAfterDeposit

        let accAfterValidWithdrawal = withdraw accAfterDeposit 30m
        printf "=== After Withdrawing 30 ===\n"
        printAccount accAfterValidWithdrawal

        try
            let accOverdrawn = withdraw accAfterValidWithdrawal 200m
            printAccount accOverdrawn
        with
        | :? System.Exception as e ->
            printf "=== Withdrawal Failed: %s ===\n" e.Message

        printf "=== Allowing withdrawal beyond overdraft (for comparison) ===\n"
        let accBeyondOverdraft = letOverdraft accAfterValidWithdrawal 200m
        printAccount accBeyondOverdraft

    [<EntryPoint>]
    let main argv = example 0