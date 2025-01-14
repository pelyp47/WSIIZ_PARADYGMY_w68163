let rec gcd a b =
    if b = 0 then a
    else gcd b (a % b)

printfn "GCD: %d" (gcd 48 18)
