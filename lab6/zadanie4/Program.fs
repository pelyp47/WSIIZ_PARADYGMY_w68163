open System

let transformFormat (input: string) =
    let parts = input.Split(';') |> Array.map (fun s -> s.Trim())
    if parts.Length = 3 then
        let firstName = parts.[0]
        let lastName = parts.[1]
        let age = parts.[2]
        sprintf "%s, %s (%s lat)" lastName firstName age
    else
        "Niepoprawny format danych"

let processEntries () =
    printfn "Wprowadź dane w formacie 'imię; nazwisko; wiek'. Aby zakończyć, wprowadź pustą linię."

    let mutable entries = []
    let mutable continueLooping = true
    while continueLooping do
        let input = Console.ReadLine()
        if String.IsNullOrWhiteSpace(input) then
            continueLooping<-false
        else
            let transformed = transformFormat input
            entries <- transformed :: entries

    printfn "\nPrzetworzone dane:"
    entries |> List.rev |> List.iter (printfn "%s")

[<EntryPoint>]
let main argv =
    processEntries ()
    0
