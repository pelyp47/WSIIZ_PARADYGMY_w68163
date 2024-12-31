type Book(title: string, author: string, pages: int) =
    member this.Title = title
    member this.Author = author
    member this.Pages = pages
    member this.GetInfo() =
        sprintf "Tytuł: %s, Autor: %s, Liczba stron: %d" this.Title this.Author this.Pages

type User(name: string) =
    let mutable borrowedBooks = []
    member this.Name = name

    member this.BorrowBook(book: Book) =
        borrowedBooks <- book :: borrowedBooks
        printfn "%s wypożyczył książkę: %s" this.Name book.Title

    member this.ReturnBook(book: Book) =
        borrowedBooks <- borrowedBooks |> List.filter (fun b -> b <> book)
        printfn "%s zwrócił książkę: %s" this.Name book.Title

    member this.ListBorrowedBooks() =
        if borrowedBooks.IsEmpty then
            printfn "%s nie wypożyczył żadnych książek." this.Name
        else
            printfn "%s wypożyczył książki:" this.Name
            borrowedBooks |> List.iter (fun b -> printfn "- %s" b.Title)

type Library() =
    let mutable books = []
    member this.AddBook(book: Book) =
        books <- book :: books
        printfn "Dodano książkę: %s" book.Title

    member this.RemoveBook(book: Book) =
        books <- books |> List.filter (fun b -> b <> book)
        printfn "Usunięto książkę: %s" book.Title

    member this.ListBooks() =
        if books.IsEmpty then
            printfn "Biblioteka jest pusta."
        else
            printfn "Książki w bibliotece:"
            books |> List.iter (fun b -> printfn "- %s" b.Title)

[<EntryPoint>]
let main argv =
    let book1 = Book("W pustyni i w puszczy", "Henryk Sienkiewicz", 500)
    let book2 = Book("Lalka", "Bolesław Prus", 400)
    let book3 = Book("Pan Tadeusz", "Adam Mickiewicz", 300)

    let library = Library()

    library.AddBook(book1)
    library.AddBook(book2)
    library.AddBook(book3)

    let user = User("Jan Kowalski")

    user.BorrowBook(book1)
    user.BorrowBook(book2)

    user.ListBorrowedBooks()

    printfn "Stan biblioteki po wypożyczeniu książek:"
    library.ListBooks()

    user.ReturnBook(book1)

    printfn "Stan biblioteki po zwróceniu książki:"
    library.ListBooks()

    user.ListBorrowedBooks()

    library.RemoveBook(book3)

    printfn "Stan biblioteki po usunięciu książki:"
    library.ListBooks()

    0