let rec sortList list =
    match list with
    | [] -> []
    | x::xs -> 
        let smaller = xs |> List.filter (fun y -> y <= x)
        let larger = xs |> List.filter (fun y -> y > x)
        sortList smaller @ [x] @ sortList larger

printfn "Sorted list: %A" (sortList [5; 3; 8; 1; 4])