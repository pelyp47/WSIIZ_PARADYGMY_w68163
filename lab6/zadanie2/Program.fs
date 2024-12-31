open System

let isPalindrome (text: string) =
    let cleanText = text.Replace(" ", "").ToLower()
    cleanText = new string(cleanText.ToCharArray() |> Array.rev)

[<EntryPoint>]
let main argv =
    printfn "Podaj tekst:"
    let inputText = Console.ReadLine()
    if isPalindrome inputText then
        printfn "Ciąg jest palindromem."
    else
        printfn "Ciąg nie jest palindromem."
    0
