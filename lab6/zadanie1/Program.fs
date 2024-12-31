open System

let countWords (text: string) =
    text.Split([|' '; '\n'; '\t'|], System.StringSplitOptions.RemoveEmptyEntries)
    |> Array.length

let countChars (text: string) =
    text.Replace(" ", "").Length

[<EntryPoint>]
let main argv =
    printfn "Podaj tekst:"
    let inputText = Console.ReadLine()

    let wordCount = countWords inputText
    let charCount = countChars inputText
    printfn "Liczba słów: %d" wordCount
    printfn "Liczba znaków (bez spacji): %d" charCount
    0