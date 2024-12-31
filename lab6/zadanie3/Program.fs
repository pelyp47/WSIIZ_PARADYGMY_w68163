open System

let removeDuplicates (words: string list) =
    words |> List.distinct

[<EntryPoint>]
let main argv =
    printfn "Podaj słowa oddzielone spacjami:"
    let inputText = Console.ReadLine()

    let words = inputText.Split(' ') |> List.ofArray

    let uniqueWords = removeDuplicates words
    printfn "Lista unikalnych słów:"
    uniqueWords |> List.iter (printfn "%s")
    0
