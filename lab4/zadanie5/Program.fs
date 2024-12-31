open System

type Litera = | X | O

type Wartosc =
  | Niesprecyzowane
  | Litera of Litera

type JedenDoTrzech = | Jeden | Dwa | Trzy

type Wiersz = Wartosc*Wartosc*Wartosc

type Plansza = Wiersz*Wiersz*Wiersz

let pustaPlansza =
  (Niesprecyzowane, Niesprecyzowane, Niesprecyzowane),
  (Niesprecyzowane, Niesprecyzowane, Niesprecyzowane),
  (Niesprecyzowane, Niesprecyzowane, Niesprecyzowane)

type Pozycja = {
  Kolumna: JedenDoTrzech
  Wiersz: JedenDoTrzech
}

type Ruch = {
  WPozycji: Pozycja
  Umieść: Litera
}

let wybierz (plansza: Plansza) (pozycja: Pozycja) =
  match plansza, pozycja with
    | ((x, _, _), _, _), { Wiersz=Jeden; Kolumna=Jeden } -> x
    | ((_, x, _), _, _), { Wiersz=Jeden; Kolumna=Dwa } -> x
    | ((_, _, x), _, _), { Wiersz=Jeden; Kolumna=Trzy } -> x
    | (_, (x, _, _), _), { Wiersz=Dwa; Kolumna=Jeden } -> x
    | (_, (_, x, _), _), { Wiersz=Dwa; Kolumna=Dwa } -> x
    | (_, (_, _, x), _), { Wiersz=Dwa; Kolumna=Trzy } -> x
    | (_, _, (x, _, _)), { Wiersz=Trzy; Kolumna=Jeden } -> x
    | (_, _, (_, x, _)), { Wiersz=Trzy; Kolumna=Dwa } -> x
    | (_, _, (_, _, x)), { Wiersz=Trzy; Kolumna=Trzy } -> x

let ustaw wartosc (plansza: Plansza) (pozycja: Pozycja) =
  match plansza, pozycja with
   | ((_, v2, v3), r2, r3), { Wiersz=Jeden; Kolumna=Jeden } -> (wartosc, v2, v3), r2, r3
   | ((v1, _, v3), r2, r3), { Wiersz=Jeden; Kolumna=Dwa } -> (v1, wartosc, v3), r2, r3
   | ((v1, v2, _), r2, r3), { Wiersz=Jeden; Kolumna=Trzy } -> (v1, v2, wartosc), r2, r3
   | (r1, (_, v2, v3), r3), { Wiersz=Dwa; Kolumna=Jeden } -> r1, (wartosc, v2, v3), r3
   | (r1, (v1, _, v3), r3), { Wiersz=Dwa; Kolumna=Dwa } -> r1, (v1, wartosc, v3), r3
   | (r1, (v1, v2, _), r3), { Wiersz=Dwa; Kolumna=Trzy } -> r1, (v1, v2, wartosc), r3
   | (r1, r2, (_, v2, v3)), { Wiersz=Trzy; Kolumna=Jeden } -> r1, r2, (wartosc, v2, v3)
   | (r1, r2, (v1, _, v3)), { Wiersz=Trzy; Kolumna=Dwa } -> r1, r2, (v1, wartosc, v3)
   | (r1, r2, (v1, v2, _)), { Wiersz=Trzy; Kolumna=Trzy } -> r1, r2, (v1, v2, wartosc)

let zmien f (plansza: Plansza) (pozycja: Pozycja) =
  ustaw (f (wybierz plansza pozycja)) plansza pozycja

let umiescPionekJesliMozna pionek = zmien (function | Niesprecyzowane -> Litera pionek | x -> x)

let wykonajRuch (plansza: Plansza) (ruch: Ruch) =
  if wybierz plansza ruch.WPozycji = Niesprecyzowane
  then Some <| umiescPionekJesliMozna ruch.Umieść plansza ruch.WPozycji
  else None

let drogiDoZwyciestwa =
  [
    { Wiersz=Jeden; Kolumna=Jeden }, { Wiersz=Jeden; Kolumna=Dwa }, { Wiersz=Jeden; Kolumna=Trzy }
    { Wiersz=Dwa; Kolumna=Jeden }, { Wiersz=Dwa; Kolumna=Dwa }, { Wiersz=Dwa; Kolumna=Trzy }
    { Wiersz=Trzy; Kolumna=Jeden }, { Wiersz=Trzy; Kolumna=Dwa }, { Wiersz=Trzy; Kolumna=Trzy }

    { Wiersz=Jeden; Kolumna=Jeden }, { Wiersz=Dwa; Kolumna=Jeden }, { Wiersz=Trzy; Kolumna=Jeden }
    { Wiersz=Jeden; Kolumna=Dwa }, { Wiersz=Dwa; Kolumna=Dwa }, { Wiersz=Trzy; Kolumna=Dwa }
    { Wiersz=Jeden; Kolumna=Trzy }, { Wiersz=Dwa; Kolumna=Trzy }, { Wiersz=Trzy; Kolumna=Trzy }

    { Wiersz=Jeden; Kolumna=Jeden }, { Wiersz=Dwa; Kolumna=Dwa }, { Wiersz=Trzy; Kolumna=Trzy }
    { Wiersz=Jeden; Kolumna=Trzy }, { Wiersz=Dwa; Kolumna=Dwa }, { Wiersz=Trzy; Kolumna=Jeden }
  ]

let komorki =
  List.ofSeq <|
    seq {
      for wiersz in [Jeden; Dwa; Trzy] do
      for kolumna in [Jeden; Dwa; Trzy] do
      yield { Wiersz=wiersz; Kolumna=kolumna }
    }

let ``mapuj 3`` f (a, b, c) = f a, f b, f c

let zwyciestwo (plansza: Plansza) =
  let sciezkiDoZwyciestwa = List.map (``mapuj 3`` (wybierz plansza)) drogiDoZwyciestwa

  if List.contains (Litera X, Litera X, Litera X) sciezkiDoZwyciestwa
  then Some X
  else if List.contains (Litera O, Litera O, Litera O) sciezkiDoZwyciestwa
  then Some O
  else None

let pozostaleMiejsca (plansza: Plansza) =
  List.exists ((=) Niesprecyzowane << wybierz plansza) komorki

type Wynik =
  | BrakJeszcze
  | Zwycięzca of Litera
  | Remis

let wynik (plansza: Plansza) =
  match zwyciestwo plansza, pozostaleMiejsca plansza with
    | Some zwyciezca, _ -> Zwycięzca zwyciezca
    | None, false -> Remis
    | _ -> BrakJeszcze

let renderujWartosc = function
  | Niesprecyzowane -> " "
  | Litera X -> "X"
  | Litera O -> "O"

let innyGracz = function
  | X -> O
  | O -> X

let renderuj ((a, b, c), (d, e, f), (g, h, i)) =
  sprintf
    """%s|%s|%s
-----
%s|%s|%s
-----
%s|%s|%s"""
    (renderujWartosc a) (renderujWartosc b) (renderujWartosc c)
    (renderujWartosc d) (renderujWartosc e) (renderujWartosc f)
    (renderujWartosc g) (renderujWartosc h) (renderujWartosc i)

type StanGry = { Plansza: Plansza; TuraGracza: Litera }

let poczatkowyStanGry = { Plansza=pustaPlansza; TuraGracza=X }

let parsujJedenDoTrzech = function
  | "1" -> Some Jeden
  | "2" -> Some Dwa
  | "3" -> Some Trzy
  | _ -> None

let parsujRuch (surowy: string) =
  match surowy.Split [|' '|] with
    | [|r; c|] ->
      match parsujJedenDoTrzech r, parsujJedenDoTrzech c with
        | Some wiersz, Some kolumna -> Some { Wiersz=wiersz; Kolumna=kolumna }
        | _ -> None
    | _ -> None

let losowyRuch (plansza: Plansza) =
  let wolnePozycje = komorki |> List.filter (fun p -> wybierz plansza p = Niesprecyzowane)
  if wolnePozycje.Length > 0 then Some (List.head wolnePozycje)
  else None

let rec przeczytajRuchWejscie litera plansza =
  match litera with
  | X ->
      match parsujRuch <| System.Console.ReadLine () with
      | Some pozycja -> { WPozycji=pozycja; Umieść=litera }
      | None -> 
        printfn "Błędny ruch! Wprowadź numery wiersza i kolumny"
        przeczytajRuchWejscie litera plansza
  | O ->
      match losowyRuch plansza with
      | Some pozycja -> { WPozycji=pozycja; Umieść=litera }
      | None -> failwith "Brak możliwych ruchów"

let rec nastepnyRuchWejscie plansza litera =
  match wykonajRuch plansza <| przeczytajRuchWejscie litera plansza with
  | Some nowaPlansza -> nowaPlansza
  | _ ->
    printfn "Błędny ruch! Pozycja jest zajęta."
    nastepnyRuchWejscie plansza litera

let rec grajWejscie { Plansza=plansza; TuraGracza=aktualnyGracz } =
  printfn "%A tura" aktualnyGracz
  printfn "%s" (renderuj plansza)

  printfn ""
  let nowaPlansza = nastepnyRuchWejscie plansza aktualnyGracz
  printfn ""

  match wynik nowaPlansza with
    | Zwycięzca litera ->
      printfn "%A wygrywa!!!" litera
      printfn "%s" (renderuj nowaPlansza)
    | Remis ->
      printfn "Remis!"
    | BrakJeszcze -> 
        grajWejscie { Plansza=nowaPlansza; TuraGracza=innyGracz aktualnyGracz }

grajWejscie poczatkowyStanGry