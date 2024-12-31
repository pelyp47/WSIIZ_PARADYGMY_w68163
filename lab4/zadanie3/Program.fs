open System
open System.Linq

let liczbaSlow (tekst: string) : int =
    tekst.Split([|' '; '\n'; '\t'; ','; '.'; '!'|], StringSplitOptions.RemoveEmptyEntries)
    |> Array.length

let liczbaZnakowBezSpacji (tekst: string) : int =
    tekst.Replace(" ", "").Length

let najczesciejWystepujaceSlowo (tekst: string) : string option =
    let slowa = tekst.Split([|' '; '\n'; '\t'; ','; '.'; '!'|], StringSplitOptions.RemoveEmptyEntries)
    let mapa = 
        slowa
        |> Array.groupBy id
        |> Array.map (fun (slowo, wystapienia) -> (slowo, wystapienia.Length))
        |> Array.sortByDescending snd
    match mapa |> Array.tryHead with
    | Some(slowo, _) -> Some(slowo)
    | None -> None

[<EntryPoint>]
let main argv =
    printfn "Podaj tekst do analizy:"
    let tekst = Console.ReadLine()

    let liczbaSlow = liczbaSlow tekst
    printfn "Liczba słów: %d" liczbaSlow

    let liczbaZnakow = liczbaZnakowBezSpacji tekst
    printfn "Liczba znaków (bez spacji): %d" liczbaZnakow

    match najczesciejWystepujaceSlowo tekst with
    | Some(slowo) -> printfn "Najczęściej występujące słowo: %s" slowo
    | None -> printfn "Brak słów w tekście."

    0
