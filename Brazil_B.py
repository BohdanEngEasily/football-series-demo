from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

champ = "Бразилія Б"

adrs = ['https://www.flashscore.ua/team/sport-recife/KIBeGAFO/',
        'https://www.flashscore.ua/team/vila-nova-fc/Y3E1Lrj3/',
        'https://www.flashscore.ua/team/sao-bernardo/Wp4nyhLR/',
        'https://www.flashscore.ua/team/athletic-club/INXlw5Bp/',
        'https://www.flashscore.ua/team/ec-juventude/GS36K259/',
        'https://www.flashscore.ua/team/operario-pr/CW8Nm1GL/',
        'https://www.flashscore.ua/team/atletico-go/8M0mP8nt/',
        'https://www.flashscore.ua/team/botafogo-sp/2yRUzy5N/',
        'https://www.flashscore.ua/team/ponte-preta/WlHjRvDk/',
        'https://www.flashscore.ua/team/america-mg/xUT0Bp8o/',
        'https://www.flashscore.ua/team/nautico/8ODJnCpa/',
        'https://www.flashscore.ua/team/fortaleza/42FbPIs2/',
        'https://www.flashscore.ua/team/goias/hfAZyE0t/',
        'https://www.flashscore.ua/team/novorizontino/4lOgZPQl/',
        'https://www.flashscore.ua/team/criciuma/48b7cubd/',
        'https://www.flashscore.ua/team/crb/QHa3bLrj/',
        'https://www.flashscore.ua/team/ceara/p0JrJCV5/',
        'https://www.flashscore.ua/team/cuiaba/zVvjqDOo/',
        'https://www.flashscore.ua/team/avai/rPzY7fWt/',
        'https://www.flashscore.ua/team/londrina/xdhbBEVA/']

draw = 6
a_1 = '.?.'

oodd = 13
a_2 = '.15-16.'

evenn = 11
a_3 = '.12.'

over_25 = 12
a_4 = '.13.'

under_25 = 14
a_5 = '.?.'

both_scores = 12
a_6 = '.13-14.'

both_no_scores = 11
a_7 = '.11-12.'

od_ev = 13
a_11 = '.17.'

ev_od = 13
a_12 = '.15-16.'

und25_ovr25 = 10
a_13 = '.10.'

ovr25_und25 = 11
a_14 = '.?.'

both_noboth = 10
a_15 = '.12.'

noboth_both = 10
a_16 = '.11-12.'

odod_evev = 5
odd_odd__evn_evn = 5
b_1 = '.6.'
b_11 = '.6.'

evev_odod = 5
evn_evn__odd_odd = 5
b_2 = '.6.'
b_22 = '.6 - 6+'

unun_ovov_25 = 5
undund_ovrovr_25 = 5
b_3 = '.6.'
b_33 = '.6.'

ovov_unun_25 = 5
ovrovr_undund_25 = 5
b_4 = '.6.'
b_44 = '.6.'

Bt_Bt_NoBt_NoBt = 5
bth_bth_NoBt_NoBt = 5
b_5 = '.5+.'
b_55 = '.5+.'

NoBt_NoBt_Bt_Bt = 5
NoBt_NoBt_bth_bth = 5
b_6 = '.6.'
b_66 = '.6.'


def draws(x):
    if len(x) < 2:
        return
    count = 0
    for i in x:
        if (i == '0 : 0' or i == '1 : 1' or i == '2 : 2' or i == '3 : 3' or i == '4 : 4'
                or i == '5 : 5' or i == '6 : 6' or i == '7 : 7'):
            count += 1
        else:
            break
    if count >= draw:
        print(f'\033[1;34m{next_game_3}   ({next_games_1})   {champ:20} {team:20} нічиїх = {count}   ..{a_1}\033[0m')


def odd(x):
    if len(x) < 2:
        return
    count = 0
    for i in x:
        if (i != '0 : 0' and i != '1 : 1' and i != '2 : 2' and i != '3 : 3'
                and i != '4 : 4' and i != '5 : 5' and i != '6 : 6' and i != '7 : 7'
                and i != '0 : 6' and i != '6 : 0'
                and i != '1 : 5' and i != '5 : 1' and i != '1 : 7' and i != '7 : 1'
                and i != '2 : 0' and i != '0 : 2' and i != '2 : 4' and i != '4 : 2'
                and i != '2 : 6' and i != '6 : 2'
                and i != '3 : 1' and i != '1 : 3' and i != '3 : 5' and i != '5 : 3'
                and i != '4 : 6' and i != '6 : 4' and i != '4 : 0' and i != '0 : 4'
                and i != '7 : 3' and i != '3 : 7' and i != '5 : 7' and i != '7 : 5'
                and i != '8 : 2' and i != '2 : 8'):
            count += 1
        else:
            break
    if count >= oodd:
        print(f'\033[1;34m{next_game_3}   ({next_games_1})   {champ:20} {team:20} НЕ_парн. = {count}   ..{a_2}\033[0m')


def even(x):
    if len(x) < 2:
        return
    count = 0
    for i in x:
        if (i == '0 : 0' or i == '1 : 1' or i == '2 : 2' or i == '3 : 3'
                or i == '4 : 4' or i == '5 : 5' or i == '6 : 6' or i == '7 : 7'
                or i == '0 : 6' or i == '6 : 0'
                or i == '1 : 5' or i == '5 : 1' or i == '1 : 7' or i == '7 :1 '
                or i == '2 : 0' or i == '0 : 2' or i == '2 : 4' or i == '4 : 2'
                or i == '2 : 6' or i == '6 : 2'
                or i == '3 : 1' or i == '1 : 3' or i == '3 : 5' or i == '5 : 3'
                or i == '4 : 6' or i == '6 : 4' or i == '4 : 0' or i == '0 : 4'
                or i == '7 : 3' or i == '3 : 7' or i == '5 : 7' or i == '7 : 5'
                or i == '8 : 2' or i == '2 : 8'):
            count += 1
        else:
            break
    if count >= evenn:
        print(f'\033[1;34m{next_game_3}   ({next_games_1})   {champ:20} {team:20} парн. = {count}   ..{a_3}\033[0m')


def over_2_5(x):
    if len(x) < 2:
        return
    count = 0
    for i in x:
        if (i != '0 : 0' and i != '1 : 1' and i != '1 : 0'
                and i != '0 : 1' and i != '2 : 0' and i != '0 : 2'):
            count += 1
        else:
            break
    if count >= over_25:
        print(f'\033[1;34m{next_game_3}   ({next_games_1})   {champ:20} {team:20} Б 2.5 = {count}   ..{a_4}\033[0m')


def under_2_5(x):
    if len(x) < 2:
        return
    count = 0
    for i in x:
        if (i == '0 : 0' or i == '1 : 1' or i == '1 : 0'
                or i == '0 : 1' or i == '2 : 0' or i == '0 : 2'):
            count += 1
        else:
            break
    if count >= under_25:
        print(f'\033[1;34m{next_game_3}   ({next_games_1})   {champ:20} {team:20} М 2.5 = {count}   ..{a_5}\033[0m')


def both_score(x):
    if len(x) < 2:
        return
    count = 0
    for i in x:
        if (i != '0 : 0' and i != '1 : 0' and i != '0 : 1' and i != '2 : 0'
                and i != '0 : 2' and i != '0 : 3' and i != '3 : 0' and i != '4 : 0'
                and i != '0 : 4' and i != '0 : 5' and i != '5 : 0' and i != '0 : 6'
                and i != '6 : 0'):
            count += 1
        else:
            break
    if count >= both_scores:
        print(f'\033[1;34m{next_game_3}   ({next_games_1})   {champ:20} {team:20} обидві зaбили = {count}   ..{a_6}\033[0m')


def both_no_score(x):
    if len(x) < 2:
        return
    count = 0
    for i in x:
        if (i == '0 : 0' or i == '1 : 0' or i == '0 : 1' or i == '2 : 0' or i == '0 : 2'
                or i == '0 : 3' or i == '3 : 0' or i == '4 : 0' or i == '0 : 4'
                or i == '0 : 5' or i == '5 : 0' or i == '0 : 6' or i == '6 : 0'
                or i == '0 : 7' or i == '7 : 0'):
            count += 1
        else:
            break
    if count >= both_no_scores:
        print(f'\033[1;34m{next_game_3}   ({next_games_1})   {champ:20} {team:20} НЕобидві зaбили = {count}   ..{a_7}'
              f'\033[0m')


def Odd_Even(x):
    if len(x) < 2:
        return
    count = 0
    olimp = []
    for i in x:
        if (i != '0 : 0' and i != '1 : 1' and i != '2 : 2' and i != '3 : 3' and i != '4 : 4'
                and i != '5 : 5' and i != '2 : 0' and i != '0 : 2' and i != '1 : 3'
                and i != '3 : 1' and i != '4 : 2' and i != '2 : 4' and i != '3 : 5'
                and i != '5 : 3' and i != '4 : 6' and i != '6 : 4' and i != '4 : 0'
                and i != '0 : 4' and i != '1 : 5' and i != '5 : 1' and i != '2 : 6'
                and i != '6 : 2' and i != '3 : 7' and i != '7 : 3' and i != '0 : 6'
                and i != '6 : 0' and i != '1 : 7' and i != '7 : 1' and i != '2 : 8'
                and i != '8 : 2'):
            olimp.append("+")
        else:
            olimp.append("-")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1

    if count >= od_ev:
        print(f'\033[1;32m{next_game_3}   ({next_games_1})   {champ:20} {team:20} НЕ_парн._парн. = {count}   ..{a_11}'
              f'\033[0m')


def Even_Odd(x):
    if len(x) < 2:
        return
    count = 0
    olimp = []
    for i in x:
        if (i != '0 : 0' and i != '1 : 1' and i != '2 : 2' and i != '3 : 3'
                and i != '4 : 4' and i != '5 : 5' and i != '2 : 0' and i != '0 : 2'
                and i != '1 : 3' and i != '3 : 1' and i != '4 : 2' and i != '2 : 4'
                and i != '3 : 5' and i != '5 : 3' and i != '4 : 6' and i != '6 : 4'
                and i != '4 : 0' and i != '0 : 4' and i != '1 : 5' and i != '5 : 1'
                and i != '2 : 6' and i != '6 : 2' and i != '3 : 7' and i != '7 : 3'
                and i != '0 : 6' and i != '6 : 0' and i != '1 : 7' and i != '7 : 1'
                and i != '2 : 8' and i != '8 : 2'):
            olimp.append("-")
        else:
            olimp.append("+")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
    if count >= ev_od:
        print(f'\033[1;32m{next_game_3}   ({next_games_1})   {champ:20} {team:20} парн._НЕ_парн. = {count}   ..{a_12}'
              f'\033[0m')


def under25_over25(x):
    if len(x) < 2:
        return
    count = 0
    olimp = []
    for i in x:
        if (i == '0 : 0' or i == '1 : 1' or i == '1 : 0'
                or i == '0 : 1' or i == '2 : 0' or i == '0 : 2'):
            olimp.append("+")
        else:
            olimp.append("-")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
    if count >= und25_ovr25:
        print(f'\033[1;32m{next_game_3}   ({next_games_1})   {champ:20} {team:20} М_Б 2.5 = {count}   ..{a_13}\033[0m')


def over25_under25(x):
    if len(x) < 2:
        return
    count = 0
    olimp = []
    for i in x:
        if (i == '0 : 0' or i == '1 : 1' or i == '1 : 0'
                or i == '0 : 1' or i == '2 : 0' or i == '0 : 2'):
            olimp.append("-")
        else:
            olimp.append("+")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1
    if count >= ovr25_und25:
        print(f'\033[1;32m{next_game_3}   ({next_games_1})   {champ:20} {team:20} Б_М 2.5 = {count}   ..{a_14}\033[0m')


def both_noboth_score(x):
    if len(x) < 2:
        return
    count = 0
    olimp = []
    for i in x:
        if (i != '0 : 0' and i != '1 : 0' and i != '0 : 1'
                and i != '2 : 0' and i != '0 : 2' and i != '0 : 3'
                and i != '3 : 0' and i != '4 : 0' and i != '0 : 4'
                and i != '0 : 5' and i != '5 : 0' and i != '0 : 6'
                and i != '6 : 0' and i != '0 : 7' and i != '7 : 0'
                and i != '0 : 8' and i != '8 : 0'):
            olimp.append("+")
        else:
            olimp.append("-")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1

    if count >= both_noboth:
        print(f'\033[1;32m{next_game_3}   ({next_games_1})   {champ:20} {team:20} обидві_НЕобидві забили = {count}   ..{a_15}'
              f'\033[0m')


def noboth_both_score(x):
    if len(x) < 2:
        return
    count = 0
    olimp = []
    for i in x:
        if (i != '0 : 0' and i != '1 : 0' and i != '0 : 1' and i != '2 : 0'
                and i != '0 : 2' and i != '0 : 3' and i != '3 : 0'
                and i != '4 : 0' and i != '0 : 4' and i != '0 : 5'
                and i != '5 : 0' and i != '0 : 6' and i != '6 : 0'
                and i != '0 : 7' and i != '7 : 0'):
            olimp.append("-")
        else:
            olimp.append("+")

    if olimp[0] == '+':
        count += 1
        if len(olimp) >= 2 and olimp[1] == '-':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '+':
                count += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        count += 1
                        if len(olimp) >= 6 and olimp[5] == '-':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '+':
                                count += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        count += 1
                                        if len(olimp) >= 10 and olimp[9] == '-':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                count += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        count += 1
                                                        if len(olimp) >= 14 and olimp[13] == '-':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        count += 1
                                                                        if len(olimp) >= 18 and olimp[17] == '-':
                                                                            count += 1

    if count >= noboth_both:
        print(f'\033[1;32m{next_game_3}   ({next_games_1})   {champ:20} {team:20} НЕобидві_обидві забили = {count}   '
              f'..{a_16}\033[0m')


def Od_Od_Ev_Ev(x):
    if len(x) < 2:
        return
    count = 0
    olimp = []
    for i in x:
        if (i != '0 : 0' and i != '1 : 1' and i != '2 : 2' and i != '3 : 3' and i != '4 : 4'
                and i != '5 : 5' and i != '2 : 0' and i != '0 : 2' and i != '1 : 3'
                and i != '3 : 1' and i != '4 : 2' and i != '2 : 4' and i != '3 : 5'
                and i != '5 : 3' and i != '4 : 6' and i != '6 : 4' and i != '4 : 0'
                and i != '0 : 4' and i != '1 : 5' and i != '5 : 1' and i != '2 : 6'
                and i != '6 : 2' and i != '3 : 7' and i != '7 : 3' and i != '0 : 6'
                and i != '6 : 0' and i != '1 : 7' and i != '7 : 1' and i != '2 : 8'
                and i != '8 : 2'):
            olimp.append("+")
        else:
            olimp.append("-")

    if olimp[0] == '+':
        if len(olimp) >= 2 and olimp[1] == '+':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '-':
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        if len(olimp) >= 6 and olimp[5] == '+':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '-':
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        if len(olimp) >= 10 and olimp[9] == '+':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '-':
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        if len(olimp) >= 14 and olimp[13] == '+':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '-':
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        if len(olimp) >= 18 and olimp[17] == '+':
                                                                            count += 1

    if count >= odod_evev:
        print(f'\033[1;35m{next_game_3}   ({next_games_1})   {champ:20} {team:20} НЕ_парн.-НЕ_парн.__парн.-парн. = {count}   .'
              f'.{b_1}\033[0m')

    cnt = 0
    if olimp[0] == '-':
        if len(olimp) >= 2 and olimp[1] == '+':
            if len(olimp) >= 3 and olimp[2] == '+':
                cnt += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    if len(olimp) >= 5 and olimp[4] == '-':
                        cnt += 1
                        if len(olimp) >= 6 and olimp[5] == '+':
                            if len(olimp) >= 7 and olimp[6] == '+':
                                cnt += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    if len(olimp) >= 9 and olimp[8] == '-':
                                        cnt += 1
                                        if len(olimp) >= 10 and olimp[9] == '+':
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                cnt += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    if len(olimp) >= 13 and olimp[12] == '-':
                                                        cnt += 1
                                                        if len(olimp) >= 14 and olimp[13] == '+':
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    if len(olimp) >= 17 and olimp[16] == '-':
                                                                        count += 1

    if cnt >= odd_odd__evn_evn:
        print(f'\033[1;35m{next_game_3}   ({next_games_1})   {champ:20} {team:20} парн. + НЕ_парн.-НЕ_парн.__парн.-парн. = {cnt}'
              f'   ..{b_11}\033[0m')


def Ev_Ev_Od_Od(x):
    if len(x) < 2:
        return
    count = 0
    olimp = []
    for i in x:
        if (i != '0 : 0' and i != '1 : 1' and i != '2 : 2' and i != '3 : 3'
                and i != '4 : 4' and i != '5 : 5' and i != '2 : 0' and i != '0 : 2'
                and i != '1 : 3' and i != '3 : 1' and i != '4 : 2' and i != '2 : 4'
                and i != '3 : 5' and i != '5 : 3' and i != '4 : 6' and i != '6 : 4'
                and i != '4 : 0' and i != '0 : 4' and i != '1 : 5' and i != '5 : 1'
                and i != '2 : 6' and i != '6 : 2' and i != '3 : 7' and i != '7 : 3'
                and i != '0 : 6' and i != '6 : 0' and i != '1 : 7' and i != '7 : 1'
                and i != '2 : 8' and i != '8 : 2'):
            olimp.append("-")
        else:
            olimp.append("+")

    if olimp[0] == '+':
        if len(olimp) >= 2 and olimp[1] == '+':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '-':
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        if len(olimp) >= 6 and olimp[5] == '+':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '-':
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        if len(olimp) >= 10 and olimp[9] == '+':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '-':
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        if len(olimp) >= 14 and olimp[13] == '+':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '-':
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        if len(olimp) >= 18 and olimp[17] == '+':
                                                                            count += 1

    if count >= evev_odod:
        print(f'\033[1;35m{next_game_3}   ({next_games_1})   {champ:20} {team:20} парн.-парн.__НЕ_парн.-НЕ_парн. = {count}   ..{b_2}')

    cnt = 0
    if olimp[0] == '-':
        if len(olimp) >= 2 and olimp[1] == '+':
            if len(olimp) >= 3 and olimp[2] == '+':
                cnt += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    if len(olimp) >= 5 and olimp[4] == '-':
                        cnt += 1
                        if len(olimp) >= 6 and olimp[5] == '+':
                            if len(olimp) >= 7 and olimp[6] == '+':
                                cnt += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    if len(olimp) >= 9 and olimp[8] == '-':
                                        cnt += 1
                                        if len(olimp) >= 10 and olimp[9] == '+':
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                cnt += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    if len(olimp) >= 13 and olimp[12] == '-':
                                                        cnt += 1
                                                        if len(olimp) >= 14 and olimp[13] == '+':
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    if len(olimp) >= 17 and olimp[16] == '-':
                                                                        count += 1

    if cnt >= evn_evn__odd_odd:
        print(f'\033[1;35m{next_game_3}   ({next_games_1})   {champ:20} {team:20} НЕ_парн. + парн.-парн.__НЕ_парн.-НЕ_парн. = {cnt}'
              f'   ..{b_22}\033[0m')


def Un_Un_Ov_Ov_25(x):
    if len(x) < 2:
        return
    count = 0
    olimp = []
    for i in x:
        if (i == '0 : 0' or i == '1 : 1' or i == '1 : 0'
                or i == '0 : 1' or i == '2 : 0' or i == '0 : 2'):
            olimp.append("+")
        else:
            olimp.append("-")

    if olimp[0] == '+':
        if len(olimp) >= 2 and olimp[1] == '+':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '-':
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        if len(olimp) >= 6 and olimp[5] == '+':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '-':
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        if len(olimp) >= 10 and olimp[9] == '+':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '-':
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        if len(olimp) >= 14 and olimp[13] == '+':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '-':
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        if len(olimp) >= 18 and olimp[17] == '+':
                                                                            count += 1

    if count >= unun_ovov_25:
        print(f'\033[1;35m{next_game_3}   ({next_games_1})   {champ:20} {team:20} М-М__Б-Б 2.5 = {count}   ..{b_3}'
              f'\033[0m')

    cnt = 0
    if olimp[0] == '-':
        if len(olimp) >= 2 and olimp[1] == '+':
            if len(olimp) >= 3 and olimp[2] == '+':
                cnt += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    if len(olimp) >= 5 and olimp[4] == '-':
                        cnt += 1
                        if len(olimp) >= 6 and olimp[5] == '+':
                            if len(olimp) >= 7 and olimp[6] == '+':
                                cnt += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    if len(olimp) >= 9 and olimp[8] == '-':
                                        cnt += 1
                                        if len(olimp) >= 10 and olimp[9] == '+':
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                cnt += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    if len(olimp) >= 13 and olimp[12] == '-':
                                                        cnt += 1
                                                        if len(olimp) >= 14 and olimp[13] == '+':
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    if len(olimp) >= 17 and olimp[16] == '-':
                                                                        count += 1
    if cnt >= undund_ovrovr_25:
        print(f'\033[1;35m{next_game_3}   ({next_games_1})   {champ:20} {team:20} Б + М-М__Б-Б 2.5 = {cnt}   ..{b_33}'
              f'\033[0m')


def Ov_Ov_Un_Un_25(x):
    if len(x) < 2:
        return
    count = 0
    olimp = []
    for i in x:
        if (i == '0 : 0' or i == '1 : 1' or i == '1 : 0'
                or i == '0 : 1' or i == '2 : 0' or i == '0 : 2'):
            olimp.append("-")
        else:
            olimp.append("+")

    if olimp[0] == '+':
        if len(olimp) >= 2 and olimp[1] == '+':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '-':
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        if len(olimp) >= 6 and olimp[5] == '+':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '-':
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        if len(olimp) >= 10 and olimp[9] == '+':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '-':
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        if len(olimp) >= 14 and olimp[13] == '+':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '-':
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        if len(olimp) >= 18 and olimp[17] == '+':
                                                                            count += 1

    if count >= ovov_unun_25:
        print(f'\033[1;35m{next_game_3}   ({next_games_1})   {champ:20} {team:20} Б-Б__М-М 2.5 = {count}   ..{b_4}'
              f'\033[0m')

    cnt = 0
    if olimp[0] == '-':
        if len(olimp) >= 2 and olimp[1] == '+':
            if len(olimp) >= 3 and olimp[2] == '+':
                cnt += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    if len(olimp) >= 5 and olimp[4] == '-':
                        cnt += 1
                        if len(olimp) >= 6 and olimp[5] == '+':
                            if len(olimp) >= 7 and olimp[6] == '+':
                                cnt += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    if len(olimp) >= 9 and olimp[8] == '-':
                                        cnt += 1
                                        if len(olimp) >= 10 and olimp[9] == '+':
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                cnt += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    if len(olimp) >= 13 and olimp[12] == '-':
                                                        cnt += 1
                                                        if len(olimp) >= 14 and olimp[13] == '+':
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    if len(olimp) >= 17 and olimp[16] == '-':
                                                                        count += 1

    if cnt >= ovrovr_undund_25:
        print(f'\033[1;35m{next_game_3}   ({next_games_1})   {champ:20} {team:20} М + Б-Б__М-М 2.5 = {cnt}   ..{b_44}'
              f'\033[0m')


def Bt_Bt_NoBt_NoBt_score(x):
    if len(x) < 2:
        return
    count = 0
    olimp = []
    for i in x:
        if (i != '0 : 0' and i != '1 : 0' and i != '0 : 1'
                and i != '2 : 0' and i != '0 : 2' and i != '0 : 3'
                and i != '3 : 0' and i != '4 : 0' and i != '0 : 4'
                and i != '0 : 5' and i != '5 : 0' and i != '0 : 6'
                and i != '6 : 0' and i != '0 : 7' and i != '7 : 0'
                and i != '0 : 8' and i != '8 : 0'):
            olimp.append("+")
        else:
            olimp.append("-")

    if olimp[0] == '+':
        if len(olimp) >= 2 and olimp[1] == '+':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '-':
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        if len(olimp) >= 6 and olimp[5] == '+':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '-':
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        if len(olimp) >= 10 and olimp[9] == '+':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '-':
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        if len(olimp) >= 14 and olimp[13] == '+':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '-':
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        if len(olimp) >= 18 and olimp[17] == '+':
                                                                            count += 1

    if count >= Bt_Bt_NoBt_NoBt:
        print(f'\033[1;35m{next_game_3}   ({next_games_1})   {champ:20} {team:20} обидві-обидві__НЕобидві-НЕобидві забили = {count} '
              f'  ..{b_5}\033[0m')

    cnt = 0
    if olimp[0] == '-':
        if len(olimp) >= 2 and olimp[1] == '+':
            if len(olimp) >= 3 and olimp[2] == '+':
                cnt += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    if len(olimp) >= 5 and olimp[4] == '-':
                        cnt += 1
                        if len(olimp) >= 6 and olimp[5] == '+':
                            if len(olimp) >= 7 and olimp[6] == '+':
                                cnt += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    if len(olimp) >= 9 and olimp[8] == '-':
                                        cnt += 1
                                        if len(olimp) >= 10 and olimp[9] == '+':
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                cnt += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    if len(olimp) >= 13 and olimp[12] == '-':
                                                        cnt += 1
                                                        if len(olimp) >= 14 and olimp[13] == '+':
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    if len(olimp) >= 17 and olimp[16] == '-':
                                                                        count += 1

    if cnt >= bth_bth_NoBt_NoBt:
        print(f'\033[1;35m{next_game_3}   ({next_games_1})   {champ:20} {team:20}   Необидві + обидві-обидві__НЕобидві-НЕобидві забили = {cnt} '
              f'  ..{b_55}')


def NoBt_NoBt_Bt_Bt_score(x):
    if len(x) < 2:
        return
    count = 0
    olimp = []
    for i in x:
        if (i != '0 : 0' and i != '1 : 0' and i != '0 : 1'
                and i != '2 : 0' and i != '0 : 2' and i != '0 : 3'
                and i != '3 : 0' and i != '4 : 0' and i != '0 : 4'
                and i != '0 : 5' and i != '5 : 0' and i != '0 : 6'
                and i != '6 : 0' and i != '0 : 7' and i != '7 : 0'
                and i != '0 : 8' and i != '8 : 0'):
            olimp.append("-")
        else:
            olimp.append("+")

    if olimp[0] == '+':
        if len(olimp) >= 2 and olimp[1] == '+':
            count += 1
            if len(olimp) >= 3 and olimp[2] == '-':
                if len(olimp) >= 4 and olimp[3] == '-':
                    count += 1
                    if len(olimp) >= 5 and olimp[4] == '+':
                        if len(olimp) >= 6 and olimp[5] == '+':
                            count += 1
                            if len(olimp) >= 7 and olimp[6] == '-':
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    count += 1
                                    if len(olimp) >= 9 and olimp[8] == '+':
                                        if len(olimp) >= 10 and olimp[9] == '+':
                                            count += 1
                                            if len(olimp) >= 11 and olimp[10] == '-':
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    count += 1
                                                    if len(olimp) >= 13 and olimp[12] == '+':
                                                        if len(olimp) >= 14 and olimp[13] == '+':
                                                            count += 1
                                                            if len(olimp) >= 15 and olimp[14] == '-':
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    count += 1
                                                                    if len(olimp) >= 17 and olimp[16] == '+':
                                                                        if len(olimp) >= 18 and olimp[17] == '+':
                                                                            count += 1

    if count >= NoBt_NoBt_Bt_Bt:
        print(f'\033[1;35m{next_game_3}   ({next_games_1})   {champ:20} {team:20} НЕобидві-НЕобидві__обидві-обидві забили = {count}'
              f'   ..{b_6}\033[0m')

    cnt = 0
    if olimp[0] == '-':
        if len(olimp) >= 2 and olimp[1] == '+':
            if len(olimp) >= 3 and olimp[2] == '+':
                cnt += 1
                if len(olimp) >= 4 and olimp[3] == '-':
                    if len(olimp) >= 5 and olimp[4] == '-':
                        cnt += 1
                        if len(olimp) >= 6 and olimp[5] == '+':
                            if len(olimp) >= 7 and olimp[6] == '+':
                                cnt += 1
                                if len(olimp) >= 8 and olimp[7] == '-':
                                    if len(olimp) >= 9 and olimp[8] == '-':
                                        cnt += 1
                                        if len(olimp) >= 10 and olimp[9] == '+':
                                            if len(olimp) >= 11 and olimp[10] == '+':
                                                cnt += 1
                                                if len(olimp) >= 12 and olimp[11] == '-':
                                                    if len(olimp) >= 13 and olimp[12] == '-':
                                                        cnt += 1
                                                        if len(olimp) >= 14 and olimp[13] == '+':
                                                            if len(olimp) >= 15 and olimp[14] == '+':
                                                                count += 1
                                                                if len(olimp) >= 16 and olimp[15] == '-':
                                                                    if len(olimp) >= 17 and olimp[16] == '-':
                                                                        count += 1

    if cnt >= NoBt_NoBt_bth_bth:
        print(f'\033[1;35m{next_game_3}   ({next_games_1})   {champ:20} {team:20} обидві + НЕобидві-НЕобидві__обидві-обидві забили ='
              f' {cnt}   ..{b_66}\033[0m')


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

for url in adrs:

    driver.get(url)

    time.sleep(8)

    text = driver.find_element(By.TAG_NAME, "body").text

    lines = text.split("\n")

    results = []

    for i in range(len(lines) - 2):

        if lines[i].isdigit() and lines[i + 1].isdigit():

            results.append(
                f"{lines[i]} : {lines[i + 1]}"
            )

    full_time = results[:20]

    future_games = []

    flag = False

    for line in lines:

        if line == "Заплановані":
            flag = True
            continue

        if flag:

            if "." in line and ":" in line:
                future_games.append(line)

    next_games_1 = len(future_games)

    if future_games:
        next_game_3 = future_games[0]
    else:
        next_game_3 = "Немає"

    team = url.split("/team/")[1].split("/")[0]
    team = team.replace("-", " ").title()

    draws(full_time)
    odd(full_time)
    even(full_time)
    over_2_5(full_time)
    under_2_5(full_time)
    both_score(full_time)
    both_no_score(full_time)

    Odd_Even(full_time)
    Even_Odd(full_time)
    under25_over25(full_time)
    over25_under25(full_time)
    both_noboth_score(full_time)
    noboth_both_score(full_time)

    Od_Od_Ev_Ev(full_time)
    Ev_Ev_Od_Od(full_time)
    Un_Un_Ov_Ov_25(full_time)
    Ov_Ov_Un_Un_25(full_time)
    Bt_Bt_NoBt_NoBt_score(full_time)
    NoBt_NoBt_Bt_Bt_score(full_time)

driver.quit()
print(f"{champ} : завершено о {time.strftime('%H:%M:%S')}")
