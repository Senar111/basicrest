#Projekt Rest Api przy użyciu Frameworku Flask
 
Prosty projekt pokazujący możliwości Rest Api w frameworku Flask

## Opis

Projekt opiera się o baze danych zleceń serwisowych
Posiadający 3 Tabele: Klient,Usluga,Zlecenie
Klient <string>"klientName",<string>"klient_adres"
Usluga <string>"uslug_id",<string>"uslug_name",<float>"uslug_cost"
Zlecenie <int>"zlec_id",<string>"zlec_klient",<string>"zlec_uslug"
 Tabela zlecenie łączy tabele klient i usluga w nastepujący sposób
    "zlec_klient" = "klientName","zlec_uslug" = "uslug_id",
 zlec_id robi się według algorytmu RRMMDDx gdzie x to numer kolejnego zlecenia np "211201001" pierwsze zlecenie dnia 1 Grudnia 2021 Roku 

### Zależności

* Projekt został wykonany na Win 10 PRO
* Python 3.10.0
* Flask 1.1.2
* Flask_restful 0.3.8

### Instalacja

* Pobrać wszystkie pliki do tego samego folderu

### Testowanie

Projekt został przetestowany przy użyciu usługi "Postman" oraz własnych programów testowych

### Użycie

Program po uruchumieniu nasłuchuje na http://127.0.0.1:5000/
Niestety nie ma głównej strony
Serwis obsługuje metode Get dla url http://127.0.0.1:5000/klient
                                    http://127.0.0.1:5000/klient/<klientName>
                                    http://127.0.0.1:5000/usluga
                                    http://127.0.0.1:5000/usluga/<uslug_id>
                                    http://127.0.0.1:5000/zlecenie
                                    http://127.0.0.1:5000/zlecenie/<zlec_id>
                                    
                       Post dla url http://127.0.0.1:5000/klient/<klientName>,{"klient_adres":<adres Klienta>}
                                    http://127.0.0.1:5000/usluga/<uslug_id>,{"uslug_name":<nazwa uslugi>,"uslug_cost":<Koszt uslugi}
                                    http://127.0.0.1:5000/zlecenie/<zlec_id>,["zlec_klient":<klientName>,"zlec_uslug":<uslug_id>}
                        
                        Put dla url http://127.0.0.1:5000/klient/<klientName>,{"klient_adres":<adres Klienta>}
                                    http://127.0.0.1:5000/usluga/<uslug_id>,{"uslug_name":<nazwa uslugi>,"uslug_cost":<Koszt uslugi}
                                    http://127.0.0.1:5000/zlecenie/<zlec_id>,["zlec_klient":<klientName>,"zlec_uslug":<uslug_id>}
                     
                     Delete dla url http://127.0.0.1:5000/klient/<klientName>
                                    http://127.0.0.1:5000/usluga/<uslug_id>           
                                    http://127.0.0.1:5000/zlecenie/<zlec_id>
                                    
Metody Delete obsługują sprawdzenie integralności danych dla klienta i uslugi
Metody Post Put obsługują sprawdzenie integralności danych dla wszystkich klas

## Pomoc

W razie problemów lub pytań zapraszam do kontaktu

## Autor

Senar111

## Inspiracja

Stackoverflow.com
Dokumentacja Flask
