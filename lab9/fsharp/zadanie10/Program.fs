open System.Data

let evaluateExpression (expression:string) =
    let result = (new DataTable()).Compute(expression, null)
    result

printfn "Result: %A" (evaluateExpression "3 + (2 * 4) - 7")
