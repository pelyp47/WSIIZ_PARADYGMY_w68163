// Struktura danych: Lista łączona
type LinkedList<'T> =
    | Empty
    | Node of 'T * LinkedList<'T>

// Moduł operacji na liście łączonej
module LinkedList =

    // Tworzenie listy łączonej z listy standardowej
    let rec fromList lst =
        match lst with
        | [] -> Empty
        | x :: xs -> Node(x, fromList xs)

    // Wyświetlanie elementów listy
    let rec printList linkedList =
        match linkedList with
        | Empty -> printfn "Koniec listy."
        | Node(value, next) ->
            printf "%A " value
            printList next

    // Sumowanie elementów listy
    let rec sumList linkedList =
        match linkedList with
        | Empty -> 0
        | Node(value, next) -> value + sumList next

    // Odwracanie listy
    let reverse linkedList =
        let rec reverseHelper lst acc =
            match lst with
            | Empty -> acc
            | Node(value, next) -> reverseHelper next (Node(value, acc))
        reverseHelper linkedList Empty

    // Sprawdzanie obecności elementu
    let rec contains linkedList element =
        match linkedList with
        | Empty -> false
        | Node(value, next) -> value = element || contains next element

    // Znajdowanie indeksu elementu
    let findIndex linkedList element =
        let rec findHelper lst idx =
            match lst with
            | Empty -> None
            | Node(value, next) ->
                if value = element then Some(idx)
                else findHelper next (idx + 1)
        findHelper linkedList 0

    // Zliczanie wystąpień elementu
    let rec countOccurrences linkedList element =
        match linkedList with
        | Empty -> 0
        | Node(value, next) ->
            let count = if value = element then 1 else 0
            count + countOccurrences next element

    // Łączenie dwóch list łączonych
    let rec concat list1 list2 =
        match list1 with
        | Empty -> list2
        | Node(value, next) -> Node(value, concat next list2)

    // Filtrowanie elementów
    let filter linkedList predicate =
        let rec helper lst =
            match lst with
            | Empty -> Empty
            | Node(value, next) ->
                if predicate value then
                    Node(value, helper next)
                else
                    helper next
        helper linkedList

    // Usuwanie duplikatów
    let removeDuplicates linkedList =
        let rec helper lst seen =
            match lst with
            | Empty -> Empty
            | Node(value, next) ->
                if Set.contains value seen then
                    helper next seen
                else
                    Node(value, helper next (Set.add value seen))
        helper linkedList Set.empty

    // Dzielenie listy na dwie części
    let partition linkedList predicate =
        let rec helper lst (yes, no) =
            match lst with
            | Empty -> (reverse yes, reverse no)
            | Node(value, next) ->
                if predicate value then
                    helper next (Node(value, yes), no)
                else
                    helper next (yes, Node(value, no))
        helper linkedList (Empty, Empty)

    // Punkt 8: Łączenie dwóch list łączonych
    let combineLists list1 list2 = concat list1 list2

    // Punkt 9: Porównywanie dwóch list
    let compareLists list1 list2 =
        let rec compareHelper l1 l2 =
            match (l1, l2) with
            | (Empty, Empty) -> []
            | (Node(v1, n1), Node(v2, n2)) ->
                (v1 > v2) :: compareHelper n1 n2
            | _ -> failwith "Listy mają różne długości."
        compareHelper list1 list2

    // Punkt 10: Filtrowanie elementów spełniających warunek
    let filterCondition linkedList predicate = filter linkedList predicate

    // Punkt 11: Usuwanie duplikatów
    let removeDuplicatesFromList linkedList = removeDuplicates linkedList

    // Punkt 12: Dzielenie listy
    let splitList linkedList predicate = partition linkedList predicate

// Funkcje interfejsu użytkownika
module Program =
    let displayMenu () =
        printfn "\nMenu:"
        printfn "1. Tworzenie listy"
        printfn "2. Wyświetlanie listy"
        printfn "3. Sumowanie elementów"
        printfn "4. Odwracanie listy"
        printfn "5. Sprawdzanie obecności elementu"
        printfn "6. Znajdowanie indeksu elementu"
        printfn "7. Zliczanie wystąpień elementu"
        printfn "8. Łączenie dwóch list"
        printfn "9. Porównywanie dwóch list"
        printfn "10. Filtrowanie listy"
        printfn "11. Usuwanie duplikatów"
        printfn "12. Dzielenie listy"
        printfn "0. Wyjście"
        printf "Wybierz opcję: "

    let rec mainLoop linkedList =
        displayMenu ()
        match System.Console.ReadLine() |> int with
        | 1 ->
            printf "Podaj elementy listy oddzielone spacją: "
            let input = System.Console.ReadLine().Split(' ') |> Array.toList |> List.map int
            let newList = LinkedList.fromList input
            printfn "Lista została utworzona."
            mainLoop newList
        | 2 ->
            printf "Elementy listy: "
            LinkedList.printList linkedList
            mainLoop linkedList
        | 3 ->
            let sum = LinkedList.sumList linkedList
            printfn "Suma elementów: %d" sum
            mainLoop linkedList
        | 4 ->
            let reversed = LinkedList.reverse linkedList
            printfn "Lista odwrócona:"
            LinkedList.printList reversed
            mainLoop reversed
        | 5 ->
            printf "Podaj element do wyszukania: "
            let element = int (System.Console.ReadLine())
            let found = LinkedList.contains linkedList element
            printfn "Element %s w liście." (if found then "znaleziono" else "nie znaleziono")
            mainLoop linkedList
        | 6 ->
            printf "Podaj element: "
            let element = int (System.Console.ReadLine())
            match LinkedList.findIndex linkedList element with
            | Some(idx) -> printfn "Indeks elementu: %d" idx
            | None -> printfn "Element nie znaleziony."
            mainLoop linkedList
        | 7 ->
            printf "Podaj element: "
            let element = int (System.Console.ReadLine())
            let count = LinkedList.countOccurrences linkedList element
            printfn "Element występuje %d razy." count
            mainLoop linkedList
        | 8 ->
            printf "Podaj elementy drugiej listy oddzielone spacją: "
            let input = System.Console.ReadLine().Split(' ') |> Array.toList |> List.map int
            let newList = LinkedList.fromList input
            let combined = LinkedList.combineLists linkedList newList
            printfn "Połączone listy: "
            LinkedList.printList combined
            mainLoop combined
        | 9 ->
            printf "Podaj elementy drugiej listy oddzielone spacją: "
            let input = System.Console.ReadLine().Split(' ') |> Array.toList |> List.map int
            let newList = LinkedList.fromList input
            try
                let comparison = LinkedList.compareLists linkedList newList
                printfn "Porównanie list: %A" comparison
            with ex ->
                printfn "Błąd: %s" ex.Message
            mainLoop linkedList
        | 10 ->
            printf "Podaj warunek (np. > 5): "
            let threshold = int (System.Console.ReadLine())
            let filtered = LinkedList.filterCondition linkedList (fun x -> x > threshold)
            printfn "Elementy spełniające warunek: "
            LinkedList.printList filtered
            mainLoop linkedList
        | 11 ->
            let unique = LinkedList.removeDuplicatesFromList linkedList
            printfn "Lista bez duplikatów: "
            LinkedList.printList unique
            mainLoop unique
        | 12 ->
            printf "Podaj wartość podziału: "
            let pivot = int (System.Console.ReadLine())
            let (yes, no) = LinkedList.splitList linkedList (fun x -> x > pivot)
            printfn "Część spełniająca warunek: "
            LinkedList.printList yes
            printfn "Część niespełniająca warunku: "
            LinkedList.printList no
            mainLoop linkedList
        | 0 -> printfn "Koniec programu."
        | _ ->
            printfn "Nieprawidłowa opcja. Spróbuj ponownie."
            mainLoop linkedList

// Uruchomienie programu
[<EntryPoint>]
let main _ =
    Program.mainLoop LinkedList.Empty
    0
