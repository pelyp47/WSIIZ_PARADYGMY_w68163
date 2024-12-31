open System

let kursyWymiany = 
    Map [
        ("USD", 1.0);
        ("EUR", 0.92);
        ("GBP", 0.76);
        ("PLN", 4.33)
    ]

let konwertujWalute (kwota: float) (walutaZrodlowa: string) (walutaDocelowa: string) : float =
    match kursyWymiany.TryFind(walutaZrodlowa), kursyWymiany.TryFind(walutaDocelowa) with
    | Some(kursZrodlowy), Some(kursDocelowy) ->
        let kwotaWUSD = kwota / kursZrodlowy
        kwotaWUSD * kursDocelowy
    | _ -> 
        printfn "Nieznana waluta."
        -1.0

[<EntryPoint>]
let main argv =
    printfn "Podaj kwotę do przeliczenia:"
    let kwota = Console.ReadLine() |> float

    printfn "Podaj walutę źródłową (np. USD, EUR, GBP):"
    let walutaZrodlowa = Console.ReadLine()

    printfn "Podaj walutę docelową (np. USD, EUR, GBP):"
    let walutaDocelowa = Console.ReadLine()

    let przeliczonaKwota = konwertujWalute kwota walutaZrodlowa walutaDocelowa

    if przeliczonaKwota >= 0.0 then
        printfn "Przeliczona kwota: %.2f %s" przeliczonaKwota walutaDocelowa
    0