let rec permute list =
    match list with
    | [] -> [[]] 
    | head :: tail ->
        let tailPermutations = permute tail
        [ for perm in tailPermutations do
            for i in 0 .. List.length perm do
                yield (List.take i perm) @ [head] @ (List.skip i perm) ]

let numbers = [1; 2; 3]
let allPermutations = permute numbers

printfn "Permutacje: %A" allPermutations

