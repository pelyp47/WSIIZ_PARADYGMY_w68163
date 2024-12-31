open System

let rec hanoi n fromPeg toPeg auxPeg =
    match n with
    | 0 -> []
    | 1 -> [(fromPeg, toPeg)]
    | _ ->
        let firstMove = hanoi (n - 1) fromPeg auxPeg toPeg
        let secondMove = [(fromPeg, toPeg)]
        let thirdMove = hanoi (n - 1) auxPeg toPeg fromPeg
        firstMove @ secondMove @ thirdMove

let moves = hanoi 3 "A" "C" "B"
printfn "Ruchy: %A" moves


let hanoiIterative n fromPeg toPeg auxPeg =
    let totalMoves = int (Math.Pow(2.0, float n) - 1.0)
    let mutable moves = []
    let mutable pegs = [(fromPeg, toPeg, auxPeg)]
    
    for i in 1 .. totalMoves do
        let moveFrom, moveTo = 
            if i % 3 = 1 then (fromPeg, toPeg)
            elif i % 3 = 2 then (fromPeg, auxPeg)
            else (auxPeg, toPeg)
        moves <- (moveFrom, moveTo) :: moves
        
    moves |> List.rev
let movesIterative = hanoiIterative 3 "A" "C" "B"

printfn "Ruchy (iteracyjnie): %A" movesIterative
