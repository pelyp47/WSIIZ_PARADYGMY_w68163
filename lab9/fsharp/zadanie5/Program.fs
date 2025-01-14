open System.IO

let countWords path =
    let text = File.ReadAllText(path).ToLower()
    let words = text.Split([|' '; '\n'; '\r'; ','; '.'; '!'|], System.StringSplitOptions.RemoveEmptyEntries)
    words
    |> Seq.groupBy id
    |> Seq.map (fun (word, occurrences) -> (word, Seq.length occurrences))
    |> Seq.iter (fun (word, count) -> printfn "%s: %d" word count)

countWords "file.txt"