# F# Invoice Validation and Totaling — Task 2 Repeat 2

## Overview

This deliverable demonstrates an F# program that validates an invoice and totals it. The program was built using the .NET 8 F# toolchain and follows the [fsharp-lang.SKILL.md](home/hatch/workspace/persona-null-paper/skills/fsharp-lang.SKILL.md) canonical skill requirements.

## F# Program

The program is located at `/home/hatch/workspace/persona-null-paper/runs/fsharp-lang/C/task2_r2_dir/InvoiceValidator/Program.fs` and implements:

- **`LineItem` record** - Immutable record with `ItemName`, `Quantity`, and `UnitPrice` fields
- **`LineItem.Create` factory method** - Validates that quantity is positive and unit price is non-negative
- **`ValidationResult` discriminated union** - `Valid of string * decimal` or `Invalid of string`
- **`validateItem` function** - Validates a line item using quantity and price checks
- **`lineTotal` function** - Calculates the total for a line item (quantity * unit price)
- **`validateAndTotal` function** - Validates and totals a list of invoice line items, returning validation results and total
- **`printInvoice` function** - Prints a formatted invoice summary
- **Discriminated union for validation results** - `Valid of string * decimal` / `Invalid of string`

### Key Features

1. **Discriminated unions** for transaction types and validation results
2. **Immutable record types** with functional updates
3. **Exhaustive pattern matching** on validation results
4. **Input validation** at function boundaries (factory method, individual checks)
5. **Explicit error handling** with descriptive messages
6. **Pure functions** with IO pushed to the edge via the `printInvoice` function

### Validation Logic

- **`checkQuantity`**: Returns `Valid` if quantity > 0, else `Invalid`
- **`checkPrice`**: Returns `Valid` if unit price >= 0, else `Invalid`
- **`validateItem`**: Combines quantity and price checks; returns the first invalid message, or `Valid ": ok"` if both pass
- **`validateAndTotal`**: Maps `validateItem` over all items; if any are invalid, returns the first error message with a count of valid/invalid items and the total. If all valid (or empty), returns `Valid message total`.

### Example Usage

The `main` function demonstrates three scenarios:

1. **Invoice 1** - Three valid line items (Widget, Gadget, Doohickey): validates successfully and prints the invoice summary with total
2. **Invoice 2** - Two invalid line items (Item A with quantity 0, Item B with negative price): validation fails with the first error message
3. **Invoice 3** - Empty list: returns `Valid "No items"` with total 0

## Build and Run Commands

```bash
# Navigate to the project directory
cd /home/hatch/workspace/persona-null-paper/runs/fsharp-lang/C/task2_r2_dir/InvoiceValidator

# Build the project
dotnet build

# Run the program
dotnet run
```

Expected build output (exit code 0):
```
Preserving main entry point from Program.fs
Compiling InvoiceValidator 100%
```

## Expected Output

The program produces the following output when run:

```
=== Invoice Summary ===
  Widget x 5 @ 19.99 = 99.95
  Gadget x 3 @ 29.50 = 88.50
  Doohickey x 10 @ 5.75 = 57.50
---------------------
Total: 245.95
======================

Validation: (2 valid, 0 invalid) total: 245.95

Invoice 2 items:
  Item A x 0 @ 10.00
  Item B x 2 @ -5.00
Validation: Item A quantity must be positive

=== Invoice Summary ===
---------------------
Total: 0.00
======================

Validation: No items
```