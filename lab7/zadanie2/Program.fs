type BankAccount(accountNumber: string, initialBalance: decimal) =
    let mutable balance = initialBalance
    member this.AccountNumber = accountNumber
    member this.Balance = balance

    member this.Deposit(amount: decimal) =
        if amount <= 0m then
            printfn "Wpłata musi być większa od 0."
        else
            balance <- balance + amount
            printfn "Wpłacono %.2f. Nowe saldo: %.2f" amount balance


    member this.Withdraw(amount: decimal) =
        if amount <= 0m then
            printfn "Wypłata musi być większa od 0."
        elif amount > balance then
            printfn "Niewystarczające środki. Saldo: %.2f" balance
        else
            balance <- balance - amount
            printfn "Wypłacono %.2f. Nowe saldo: %.2f" amount balance

    member this.GetInfo() =
        sprintf "Numer konta: %s, Saldo: %.2f" this.AccountNumber this.Balance

type Bank() =
    let mutable accounts = Map.empty<string, BankAccount>

    member this.CreateAccount(accountNumber: string, initialBalance: decimal) =
        if accounts.ContainsKey(accountNumber) then
            printfn "Konto z numerem %s już istnieje." accountNumber
        else
            let account = BankAccount(accountNumber, initialBalance)
            accounts <- accounts.Add(accountNumber, account)
            printfn "Utworzono konto: %s z saldem %.2f" accountNumber initialBalance

    member this.GetAccount(accountNumber: string) =
        match accounts.TryFind(accountNumber) with
        | Some(account) -> Some(account)
        | None ->
            printfn "Konto z numerem %s nie istnieje." accountNumber
            None

    member this.UpdateAccount(accountNumber: string, action: BankAccount -> unit) =
        match this.GetAccount(accountNumber) with
        | Some(account) ->
            action(account)
        | None -> printfn "Nie można zaktualizować konta: %s" accountNumber

    member this.DeleteAccount(accountNumber: string) =
        if accounts.ContainsKey(accountNumber) then
            accounts <- accounts.Remove(accountNumber)
            printfn "Konto %s zostało usunięte." accountNumber
        else
            printfn "Konto z numerem %s nie istnieje." accountNumber

    member this.ListAccounts() =
        if accounts.IsEmpty then
            printfn "Brak kont w banku."
        else
            printfn "Lista kont w banku:"
            accounts |> Map.iter (fun _ account -> printfn "- %s" (account.GetInfo()))

[<EntryPoint>]
let main argv =
    let bank = Bank()

    bank.CreateAccount("12345", 1000m)
    bank.CreateAccount("67890", 500m)

    printfn "Stan kont w banku po utworzeniu:"
    bank.ListAccounts()

    bank.UpdateAccount("12345", fun account -> account.Deposit(200m))

    bank.UpdateAccount("12345", fun account -> account.Withdraw(300m))

    bank.UpdateAccount("12345", fun account -> account.Withdraw(2000m))

    bank.GetAccount("99999") |> ignore

    bank.DeleteAccount("67890")
    printfn "Stan kont w banku po usunięciu:"
    bank.ListAccounts()

    0
