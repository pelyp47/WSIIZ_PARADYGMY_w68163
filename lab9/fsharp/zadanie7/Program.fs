open System
let toUpperCase (list: string list) =
   list |> List.map (fun s-> s.ToUpper())

printfn "Uppercase words: %A" (toUpperCase ["abc"; "def"; "ghi"])
