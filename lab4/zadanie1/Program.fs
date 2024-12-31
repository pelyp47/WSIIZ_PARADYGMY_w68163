open System
type Uzytkownik = { Waga: float; Wzrost: float }

let obliczBMI (waga: float) (wzrost: float) : float =
    let wzrostMetry = wzrost / 100.0
    waga / (wzrostMetry * wzrostMetry)

let okreslKategorieBMI bmi : string =
    if bmi < 18.5 then "Niedowaga"
    elif bmi >= 18.5 && bmi < 24.9 then "Prawidłowa masa ciała"
    elif bmi >= 25.0 && bmi < 29.9 then "Nadwaga"
    else "Otyłość"
[<EntryPoint>]
let main argv =
    printfn "Podaj swoją wagę w kg:"
    let waga = Console.ReadLine() |> float

    printfn "Podaj swój wzrost w cm:"
    let wzrost = Console.ReadLine() |> float

    let uzytkownik = { Waga = waga; Wzrost = wzrost }

    let bmi = obliczBMI uzytkownik.Waga uzytkownik.Wzrost

    let kategoria = okreslKategorieBMI bmi

    printfn "Twoje BMI wynosi: %.2f" bmi
    printfn "Kategoria: %s" kategoria

    0