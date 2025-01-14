let isPrime n =
    if n < 2 then false
    else [2..int(sqrt(float n))] |> List.forall (fun x -> n % x <> 0)

printfn "Is the number prime: %b" (isPrime 13)