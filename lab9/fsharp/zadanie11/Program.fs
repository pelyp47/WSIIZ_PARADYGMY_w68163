let rec powerSet list =
    match list with
    | [] -> [[]]
    | x::xs ->
        let rest = powerSet xs
        rest @ (rest |> List.map (fun subset -> x :: subset))

printfn "Power set: %A" (powerSet [1; 2; 3])
