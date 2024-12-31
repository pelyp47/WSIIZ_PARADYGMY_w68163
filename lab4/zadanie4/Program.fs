open System

type Konto = { NumerKonta: string; Saldo: float }

let mutable konta: Map<string, Konto> = Map.empty

let utworzKonto numerKonta =
    if konta.ContainsKey(numerKonta) then
        printfn "Konto o numerze %s już istnieje!" numerKonta
    else
        let noweKonto = { NumerKonta = numerKonta; Saldo = 0.0 }
        konta <- konta.Add(numerKonta, noweKonto)
        printfn "Konto o numerze %s zostało utworzone." numerKonta

let depozyt numerKonta kwota =
    match konta.TryFind(numerKonta) with
    | Some(konto) ->
        let noweSaldo = konto.Saldo + kwota
        let noweKonto = { konto with Saldo = noweSaldo }
        konta <- konta.Add(numerKonta, noweKonto)
        printfn "Na konto %s dodano %.2f. Nowe saldo: %.2f" numerKonta kwota noweSaldo
    | None -> printfn "Konto o numerze %s nie istnieje." numerKonta

let wyplata numerKonta kwota =
    match konta.TryFind(numerKonta) with
    | Some(konto) when konto.Saldo >= kwota ->
        let noweSaldo = konto.Saldo - kwota
        let noweKonto = { konto with Saldo = noweSaldo }
        konta <- konta.Add(numerKonta, noweKonto)
        printfn "Z konta %s wypłacono %.2f. Nowe saldo: %.2f" numerKonta kwota noweSaldo
    | Some(konto) -> printfn "Brak wystarczających środków na koncie %s." numerKonta
    | None -> printfn "Konto o numerze %s nie istnieje." numerKonta

let pokazSaldo numerKonta =
    match konta.TryFind(numerKonta) with
    | Some(konto) -> printfn "Saldo konta %s: %.2f" numerKonta konto.Saldo
    | None -> printfn "Konto o numerze %s nie istnieje." numerKonta

[<EntryPoint>]
let main argv =
    let rec menu () =
        printfn "\nWybierz operację:"
        printfn "1. Utwórz nowe konto"
        printfn "2. Depozyt"
        printfn "3. Wypłata"
        printfn "4. Pokaż saldo"
        printfn "5. Wyjście"
        let wybor = Console.ReadLine()
        
        match wybor with
        | "1" ->
            printf "Podaj numer konta: "
            let numerKonta = Console.ReadLine()
            utworzKonto numerKonta
            menu ()
        | "2" ->
            printf "Podaj numer konta: "
            let numerKonta = Console.ReadLine()
            printf "Podaj kwotę do depozytu: "
            let kwota = float (Console.ReadLine())
            depozyt numerKonta kwota
            menu ()
        | "3" ->
            printf "Podaj numer konta: "
            let numerKonta = Console.ReadLine()
            printf "Podaj kwotę do wypłaty: "
            let kwota = float (Console.ReadLine())
            wyplata numerKonta kwota
            menu ()
        | "4" ->
            printf "Podaj numer konta: "
            let numerKonta = Console.ReadLine()
            pokazSaldo numerKonta
            menu ()
        | "5" -> 
            printfn "Dziękujemy za korzystanie z aplikacji!"
            0
        | _ ->
            printfn "Niepoprawny wybór. Spróbuj ponownie."
            menu ()

    menu ()
