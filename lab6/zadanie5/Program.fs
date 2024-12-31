open System

let findLongestWord (input: string) =
    let words = input.Split([|' '; '\n'; '\r'; '\t'|], StringSplitOptions.RemoveEmptyEntries)
    let longestWord = 
        words 
        |> Array.maxBy (fun word -> word.Length)
    longestWord, longestWord.Length

[<EntryPoint>]
let main argv =
    printfn "Wprowadź tekst:"
    let input = Console.ReadLine()
    let word, length = findLongestWord input
    printfn "Najdłuższe słowo: %s" word
    printfn "Długość najdłuższego słowa: %d" length
    
    0