Link do pobrania gita:
https://git-scm.com/download

Inicjalizacja repozytorium lokalnie w otwartym folderze:
```shell
git init
```

Połączenie lokalnego repozytorium z repozytorium zdalnym na GitHubie:
```shell
git remote add origin https://github.com/USER/REPO_NAME.git
```

Klonowanie istniejącego repozytorium zdalnego do lokalnego:
```shell
git clone https://github.com/USER/REPO_NAME.git
```

Dodanie pliku do "śledzenia" przez repozytorium:
```shell
git add file
```

Dodanie wszystkich plików w repozytorium do następnego commita:
```shell
git add .
```

Dodanie commita (wpisu do historii zmian w repozytorium):
```shell
git commit -m "message"
```

Przeglądanie statustu repozytorium:
```shell
git status
```

Przeglądanie historii commitów:
```shell
git log
```

Przeglądanie ładnej historii commitów w postaci grafu:
```shell
git log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short
```

Pobieranie zmian ze zdalnego repozytorium na Githubie:
```shell
git pull
```