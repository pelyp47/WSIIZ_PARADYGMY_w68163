open System

let rec quickSort arr =
    match arr with
    | [] -> []
    | pivot :: rest ->
        let smaller = List.filter (fun x -> x < pivot) rest
        let larger = List.filter (fun x -> x >= pivot) rest
        (quickSort smaller) @ [pivot] @ (quickSort larger)

let arr = [3; 6; 8; 10; 1; 2; 1]
let sortedArr = quickSort arr



let quickSortIterative (arr: int list) : int list =
    let arr = arr |> List.toArray
    let stack = System.Collections.Generic.Stack<(int * int)>()

    stack.Push((0, arr.Length - 1))

    while stack.Count > 0 do
        let (low, high) = stack.Pop()

        if low < high then
            let pivotIndex = (low + high) / 2
            let pivot = arr.[pivotIndex]
            let mutable i = low
            let mutable j = high
            while i <= j do
                while arr.[i] < pivot do
                    i <- i + 1
                while arr.[j] > pivot do
                    j <- j - 1

                if i <= j then
                    let temp = arr.[i]
                    arr.[i] <- arr.[j]
                    arr.[j] <- temp
                    i <- i + 1
                    j <- j - 1
            if low < j then
                stack.Push((low, j))
            if i < high then
                stack.Push((i, high))
    arr |> Array.toList

let sortedArrIterative = quickSortIterative arr


printfn "Posortowana lista (rekurencyjnie): %A" sortedArr
printfn "Posortowana lista (iteracyjnie): %A" sortedArrIterative