let rec fibonacci n =
    match n with
    | 0 -> 0
    | 1 -> 1
    | _ -> fibonacci (n - 1) + fibonacci (n - 2)

let fibonacciTailRecursive n =
    let rec fibTailRec a b n =
        match n with
        | 0 -> a
        | _ -> fibTailRec b (a + b) (n - 1)
    fibTailRec 0 1 n

printfn "%A" (fibonacci 10)
printfn "%A" (fibonacciTailRecursive 10)
