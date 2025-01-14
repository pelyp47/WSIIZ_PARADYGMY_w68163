let generateReport studentGrades =
    studentGrades
    |> List.iter (fun (student, grade) -> printfn "%s: %d" student grade)

let students = [("John", 5); ("Anna", 4); ("Kate", 3)]
generateReport students