*** Settings ***
Library  ../nettilotto.py  WITH NAME  NettiLotto

*** Test Cases ***

Testaa 7 Oikein
    ${voitto} =    NettiLotto.Tarkista Voitto    1 2 3 4 5 6 7    1 2 3 4 5 6 7    8    1.0
    Should Be Equal As Numbers    ${voitto}    1000000

Testaa 6 Oikein + Lisänumero
    ${voitto} =    NettiLotto.Tarkista Voitto    1 2 3 4 5 6 8    1 2 3 4 5 6 7    8    1.0
    Should Be Equal As Numbers    ${voitto}    100000

Testaa 6 Oikein
    ${voitto} =    NettiLotto.Tarkista Voitto    1 2 3 4 5 6 9    1 2 3 4 5 6 7    8    1.0
    Should Be Equal As Numbers    ${voitto}    2000

Testaa 5 Oikein
    ${voitto} =    NettiLotto.Tarkista Voitto    1 2 3 4 5 10 11    1 2 3 4 5 6 7    8    1.0
    Should Be Equal As Numbers    ${voitto}    50

Testaa 4 Oikein
    ${voitto} =    NettiLotto.Tarkista Voitto    1 2 3 4 12 13 14    1 2 3 4 5 6 7    8    1.0
    Should Be Equal As Numbers    ${voitto}    10

Testaa 3 Oikein + Lisänumero
    ${voitto} =    NettiLotto.Tarkista Voitto    1 2 3 8 12 13 14    1 2 3 4 5 6 7    8    1.0
    Should Be Equal As Numbers    ${voitto}    2

Testaa Pelkkä Lisänumero
    ${voitto} =    NettiLotto.Tarkista Voitto    8 10 11 12 13 14 15    1 2 3 4 5 6 7    8    1.0
    Should Be Equal As Numbers    ${voitto}    5

Testaa Panoksen Vaikutus
    ${voitto} =    NettiLotto.Tarkista Voitto    1 2 3 4 5 10 11    1 2 3 4 5 6 7    8    2.0
    Should Be Equal As Numbers    ${voitto}    100
