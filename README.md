# sciekipolskie
Here my solution for trial task of Scieki Polskie

1.Instrukcja:
Jako właściciel firmy chcę mieć możliwość wejścia na stronę główną, na której zobaczę listę
wszystkich moich pracowników. Chcę, aby obok listy wyświetlał się przycisk otwierający
modal pozwalający na dodanie nowego pracownika.
Chcę mieć możliwość kliknięcia na jednego z pracowników dostępnych na liście, co
spowoduje wyświetlenie strony z informacją o danym pracowniku wraz z listą zadań
przypisanych do tego pracownika. Każde zadanie musi zawierać opis, status, kategorie,
oraz planowaną datę wykonania zadania. Przy każdym z zadań chcę widzieć przyciski
pozwalające na usunięcie zadania oraz na oznaczenie jako wykonane, naciśnięcie którego
wykona akcję bez przeładowania strony. Chcę widzieć przycisk otwierający modal
zawierający formularz dodający nowe zadanie dla danego pracownika.
Na liście z zadaniami pracownika chcę mieć możliwość filtrowania zadań po statusie lub
dacie.
2. Zadania dla chętnych:
„*”
- w DRF przygotuj endpoint zwracający listę wszystkich pracowników wraz z ich zadaniami
na dziś
- na stronie z listą zadań pracownika dodaj możliwość exportu zadań do pliku CSV
„**”
- dodaj możliwość uruchomienia za pomocą docker-compose (zdokeryzuj apke!)
„***”
- na stronie głównej dodaj możliwość asynchronicznego importowania pracowników
wykorzystując Celery
- przygotuj opis endpoint’u używając aplikacji swagger
