let sumFrom1ToN n = 
    [1..n] |> List.sum

printfn "Sum from 1 to n: %d" (sumFrom1ToN 10)