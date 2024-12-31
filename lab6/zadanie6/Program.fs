open System

let replaceWord (input: string) (oldWord: string) (newWord: string) =
    input.Replace(oldWord, newWord)

[<EntryPoint>]
let main argv =
    printfn "Wprowadź tekst:"
    let input = Console.ReadLine()
    
    printfn "Wprowadź słowo, które chcesz wyszukać:"
    let oldWord = Console.ReadLine()
    
    printfn "Wprowadź słowo, na które chcesz je zamienić:"
    let newWord = Console.ReadLine()
    
    let modifiedText = replaceWord input oldWord newWord
    
    printfn "Zmodyfikowany tekst:"
    printfn "%s" modifiedText
    
    0