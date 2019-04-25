TODO
- 

- Rozpoczyna dowolny gracz (Qlearning/greedy/human)
    - Generować tabelę dla wszystkich stanów (obustronnie)
- Sprawdzić jakość na różnych agentac (random/qlearn). Vs. human może być niewiarygodne
- Można dodać heurystyczna ocene stanu gry jako nagrodę
    - nagroda za zajecie pola środkowego
    - nagroda za uniemożliwienie wygranej przeciwnikowi (gdy ma 2 w rzędzie)
- Przemyslec rozwiazanie z wyk. uczenia nadzorowanego



TODO:
- random agent
- framework do testow
- ewentualnie opcja rozpoczynania gry nie przez Qlearning


https://stats.stackexchange.com/questions/250807/tic-tac-toe-ai-with-machine-learning


propozycja rozwiazania na podst. ucz. nadz
- uwzglednienie symetrii, zadany stan jest obracany i odbijany, a nastepnie oceny rozgrywek dla tych stanow sa usredniane i zwaracane
- ekstrakcja cech: wybieramy cechy stanu gry i przypisujemy im prawdopodobienstwo wygranej na podstawie przeprowadzonych rozgrywek
- 

Rozw. 1:
1) generuj wszystkie stany końcowe gry z etykieta wygrana-przegrana
2) zbuduj drzewo decyzyjne (zakladajac w kazdym polu mozliwe 3 wartosci/wartosci ciagle)
3) w trakcie gry stan niepełny jest wprowadzany do klasyfikatora i otrzymujemy klasę (win/lose) oraz wartość pewności klasyfikacji danego węzła


Rozw. 2:
1) Tablica z wszystkimi stanami (zaczyna zawsze X)
2) Przeprowadzenie rozgrywek z losowymi agentami (jakimi?)
3) Po rozgrywce uzupełnienie tabeli stanów z informacją win/lose i ilośc rozegranych gier dająca prawdopodobieństwo wygranej (np. X)
4) Agent będzie używał tablicy do oceny stanu gry (z jakim prawdopodobieństwem wygra)

możliwe usprawnienia: wykorzystanie symetrii lub ekstrakcji cech (np. ilość symboli na diagonali/w rzędzie) aby zmniejszyć wielkość tablicy,
symetria pozwala zwiekszyć precyzję prawdopodobieństwa, ponieważ uśredniamy p ze stanów symetrycznych do podanego