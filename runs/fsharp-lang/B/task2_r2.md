# Run spec — fsharp-lang, arm B (one-line label), task 2, repeat 2

## The F# Invoice Validation and Totaling Program

This deliverable shows an F# program that validates an invoice and totals it, along with instructions for building and running it.

### The F# Program

Create a file named `invoice.fsx` with the following content:

```fsharp
(* invoice.fsx - F# invoice validation and totaling *)

// Define invoice data structure
type Invoice = {
    CustomerName: string
    Items: { Description: string; Quantity: int; Price: float } list
    IssueDate: System.DateTime
}

// Validate an invoice
let validateInvoice (invoice: Invoice) =
    if String.IsNullOrWhiteSpace invoice.CustomerName then
        failwith "Customer name is required"
    if invoice.Items.length = 0 then
        failwith "Invoice must have at least one item"
    if invoice.Items |> List.exists (fun item -> item.Quantity <= 0) then
        failwith "Quantity must be positive"
    if invoice.Items |> List.exists (fun item -> item.Price <= 0.0) then
        failwith "Price must be positive"
    if invoice.IssueDate > System.DateTime.Now then
        failwith "Issue date cannot be in the future"
    printfn "Invoice validation passed"

// Calculate total amount
let calculateTotal (invoice: Invoice) =
    invoice.Items
    |> List.sumBy (fun item -> float item.Quantity * item.Price)
    |> printfn "Total: $%.2f"

// Example usage
let main () =
    let sampleInvoice = {
        CustomerName = "Acme Corp"
        Items = [
            { Description = "Widget"; Quantity = 3; Price = 19.99 }
            { Description = "Gadget"; Quantity = 2; Price = 29.99 }
        ]
        IssueDate = System.DateTime.Now
    }

    validateInvoice sampleInvoice
    calculateTotal sampleInvoice

if System.Diagnostics.Debugger.IsAttached then
    main()
```

### Building and Running

#### Option 1: Using `fsharpi` (F# interactive script)

```bash
fsharpi invoice.fsx
```

#### Option 2: Using .NET SDK

1. Create a project file `invoice.fsproj`:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
  </PropertyGroup>
</Project>
```

2. Build and run:

```bash
dotnet run
```

### Expected Output

```
Invoice validation passed
Total: $99.95
```

### Program Logic

1. **`Invoice` type** - Defines the structure with customer name, items, and issue date
2. **`validateInvoice`** - Checks that customer name is not empty, there's at least one item, quantities and prices are positive, and the issue date is not in the future
3. **`calculateTotal`** - Multiplies quantity by price for each item and sums the results
4. **`main`** - Creates a sample invoice, validates it, and calculates the total