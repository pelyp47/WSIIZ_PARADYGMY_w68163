let stringLengths list =
    list |> List.map String.length

printfn "String lengths: %A" (stringLengths ["FSharp"; "is"; "awesome"])
