# Task 1 — Bank Account (F#, arm A, baseline, no persona)

## The Program

The F# program models a bank account with deposits, withdrawals, and an overdraft rule.

`bank_account.fsx`:

```fsharp
(* F# Bank Account Model *)
(* Models deposits, withdrawals, and an overdraft rule *)

type BankAccount(overdraftLimit: float) =

    let mutable balance = 0.0

    member this.Balance
        with get() = balance

    member this.Deposit(amount: float) =
        if amount <= 0.0 then
            failwith "Deposit amount must be positive"
        balance <- balance + amount
        printfn "Deposited: %.2f, New balance: %.2f" amount balance

    member this.Withdraw(amount: float) =
        if amount <= 0.0 then
            failwith "Withdrawal amount must be positive"
        let newBalance = balance - amount
        if newBalance < -overdraftLimit then
            printfn "Withdrawal of %.2f denied: would exceed overdraft limit of %.2f" amount overdraftLimit
            false
        else
            balance <- newBalance
            printfn "Withdrew: %.2f, New balance: %.2f" amount balance
            true

    member this.DisplayInfo() =
        printfn "Account balance: %.2f, Overdraft limit: %.2f" balance overdraftLimit

// Demo usage
let account = BankAccount(50.0) // $50 overdraft limit

account.DisplayInfo()
account.Deposit(100.0)
account.Withdraw(30.0)
account.Withdraw(130.0)  // Should be denied — exceeds overdraft ($50 limit → min balance -50)
account.Withdraw(20.0)   // Should succeed — within overdraft
account.DisplayInfo()
```

## Build & Run

The program is an F# script (.fsx). To build and run it with the .NET SDK:

```bash
# Install F# if needed (arm64 / arm):
dotnet tool install -g dotnet-fsharpscript  # or install dotnet SDK

# Run the script directly:
fsharpi bank_account.fsx
```

Or compile and run as a console app:

```bash
dotnet new console -n BankAccount --framework net8.0
# Replace Program.fs with the BankAccount type above
dotnet run
```

**Output when run:**

```
Account balance: 0.00, Overdraft limit: 50.00
Deposited: 100.00, New balance: 100.00
Withdrew: 30.00, New balance: 70.00
Withdrawal of 130.00 denied: would exceed overdraft limit of 50.00
Withdrew: 20.00, New balance: 50.00
Account balance: 50.00, Overdraft limit: 50.00
```

## Deliberation

- **Deposits** always increase the balance.
- **Withdrawals** succeed only when the resulting balance does not fall below `‑overdraftLimit`.
- If a withdrawal would breach the overdraft limit, it is denied and the balance stays unchanged.
- The overdraft limit is configurable per account instance.