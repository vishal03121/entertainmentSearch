import requests
import os
import webbrowser
def clear():
    os.system('cls')
cmd = 'color F0'
os.system(cmd)
def movieInfo():
    clear()
    wlcomeMsg = '<Welcome to ENTERTAINMENT FREAKS! Movie Section>'
    print(wlcomeMsg.center(100))
    print('Type -return- To Go Back To Main Menu')
    print('Type -quit- To Terminate')
    searchName = input('Enter Movie Name: ').lower()
    while len(searchName.strip()) == 0:
        clear()
        print(wlcomeMsg.center(100))
        print()
        print("Error No Name Provided".center(100, '*'))
        print()
        print('Type -return- To Go Back To Main Menu')
        print('Type -quit- To Terminate')
        searchName = input('Enter Movie Name: ').lower()
    if searchName == 'return':
        return True
    if searchName == 'quit':
        quit()
    else:
        url = 'http://www.omdbapi.com/?i=tt3896198&apikey=1bdb5c29'
        searchParam = {'s': searchName, 'type': 'movie'}
        searchResults = requests.get(url, params=searchParam)
        if searchResults.status_code != 200:
            return '404 File Not Found'
        else:
            movLst = searchResults.json()
            if movLst['Response'] == 'True':
                lst = [(movLst['Search'][i]['Title'],movLst['Search'][i]['Year']) for i in range(len(movLst['Search']))]
                if len(lst) > 0:
                    clear()
                    print('Movies Found!'.center(100, '*'))
                    print('option'.ljust(10), 'Name'.ljust(70), 'Year')
                    for i in range(len(lst)):
                        print(str(i).ljust(10), lst[i][0].ljust(70), lst[i][1])

                    while True:
                        print()
                        print('Type -return- To Go Back To Main Menu')
                        print('Type -quit- To Terminate')
                        print('To View Movie Details:')
                        movName = input("Enter Movie Option: ").lower()
                        if movName == 'return':
                            return True
                        if movName == 'quit':
                            quit()
                        else:
                            try:
                                movName = int(movName)
                                if movName < 0 or movName > len(lst):
                                    print()
                                    print("Input Value Must Be In Between Options Range".center(100, '*'))
                                    continue
                                break
                            except:
                                print()
                                print("Input Must be Intrger or 'return' only".center(100, '*'))
                                continue
                    clear()
                    print('Movie Selected: ', lst[int(movName)][0])
                    print()
                    param = {'t': lst[int(movName)][0], 'type': 'movie'}
                    results = requests.get(url, params=param)
                    if results.status_code != 200:
                        return '404 File Not Found'
                    else:
                        movInfo = results.json()
                        if movInfo['Response'] == 'True':
                            d = ['Title', 'Year', 'Rated', 'Released', 'Runtime','imdbRating', 'Production']
                            for key in d:
                                print(key.ljust(30), ':', movInfo[key])
                            rest = ['Genre', 'Director', 'Writer', 'Actors', 'Awards']
                            for key in rest:
                                print((key + ':').center(50, '-'))
                                i = 1
                                for value in movInfo[key].split(','):
                                    print(str(i).ljust(30), ':' + str(value.strip()))
                                    i = i + 1
                            print('Plot:'.center(50, '-'))
                            plot = movInfo['Plot'].split()
                            j = 0
                            for i in range(6, len(plot)-6 ,6):
                                print(' '.join(plot[j:i]).center(50,' '))
                                j = i
                            print(' '.join(plot[j:]).center(50, ' '))
                            print('Ratings:'.center(50, '-'))
                            for key in movInfo['Ratings']:
                                print(key['Source'].ljust(30), ':' + key['Value'].strip())
                            print()
                            k = input('Press enter To Go Back To Main Menu')
                            return True
                        else:
                            return '404 Movie Not Found'
            else:
                return '404 Movie Not Found'

def similarMovie():
    clear()
    wlcomeMsg = '<Welcome to ENTERTAINMENT FREAKS! Movie Similar Section>'
    print(wlcomeMsg.center(100))
    print('Type -return- To Go Back To Main Menu')
    print('Type -quit- To Terminate')
    searchName = input('Enter Movie Name: ').lower()
    while len(searchName.strip()) == 0:
        clear()
        print(wlcomeMsg.center(100))
        print()
        print("Error No Name Provided".center(100, '*'))
        print()
        print('Type -return- To Go Back To Main Menu')
        print('Type -quit- To Terminate')
        searchName = input('Enter Movie Name: ').lower()
    if searchName == 'return':
        return True
    if searchName == 'quit':
        quit()

    while True:
        n = input('Enter Required Results(1-50): ')
        try:
            n = int(n)
            if n <= 0 or n > 50:
                print()
                print('Input Must be in Between range- 0-50'.center(100, '*'))
                continue
            break
        except:
            print()
            print('Please Enter only Interger Value!'.center(100, '*'))
            print()
            continue
    url = 'https://tastedive.com/api/similar'
    param = {'q': searchName, 'type': 'movies', 'limit': n}
    results = requests.get(url, params=param)
    if results.status_code != 200:
        return '404 File Not Found!'
    else:
        res = results.json()
        clear()
        if len(res['Similar']['Results']) == 0:
            return 'No Match Found!'
        print('Match Found!'.center(100, '*'))
        print('Index'.ljust(10), 'Name')
        for i in range(len(res['Similar']['Results'])):
            print(str(i).ljust(10), res['Similar']['Results'][i]['Name'])
        print()
        k = input('Press enter To Go Back To Main Menu ')
        return True

def similarSongs():
    clear()
    wlcomeMsg = '<Welcome to ENTERTAINMENT FREAKS! Similar Songs Section>'
    print(wlcomeMsg.center(100))
    print('Type -return- To Go Back To Main Menu')
    print('Type -quit- To Terminate')
    searchName = input('Enter Artist Name: ').lower()
    while len(searchName.strip()) == 0:
        clear()
        print(wlcomeMsg.center(100))
        print()
        print("Error No Name Provided".center(100, '*'))
        print()
        print('Type -return- To Go Back To Main Menu')
        print('Type -quit- To Terminate')
        searchName = input('Enter Artist Name: ').lower()
    if searchName == 'return':
        return True
    if searchName == 'quit':
        quit()

    while True:
        n = input('Enter Required Results(1-50): ')
        try:
            n = int(n)
            if n <= 0 or n > 50:
                print()
                print('Input Must be in Between range- 0-50'.center(100, '*'))
                print()
                continue
            break
        except:
            print()
            print('Please Enter only Interger Value!'.center(100, '*'))
            print()
            continue
    url = 'https://tastedive.com/api/similar'
    param = {'q': searchName, 'type': 'music', 'limit': n}
    results = requests.get(url, params=param)
    if results.status_code != 200:
        return '404 File Not Found!'
    else:
        res = results.json()
        clear()
        if len(res['Similar']['Results']) == 0:
            return 'No Match Found!'
        print('Match Found!'.center(100, '*'))
        print('Index'.ljust(10), 'Name')
        for i in range(len(res['Similar']['Results'])):
            print(str(i).ljust(10), res['Similar']['Results'][i]['Name'])
        print()
        k = input('Press enter To Go Back To Main Menu ')
        return True

def songLyrics():
    clear()
    wlcomeMsg = '<Welcome to ENTERTAINMENT FREAKS! Songs Lyrics Section>'
    print(wlcomeMsg.center(100))
    print('Type -return- To Go Back To Main Menu')
    print('Type -quit- To Terminate')
    searchName = input('Enter Song Name: ').lower()
    while len(searchName.strip()) == 0:
        clear()
        print(wlcomeMsg.center(100))
        print()
        print("Error No Name Provided".center(100, '*'))
        print()
        print('Type -return- To Go Back To Main Menu')
        print('Type -quit- To Terminate')
        searchName = input('Enter Song Name: ').lower()
    if searchName == 'return':
        return True
    if searchName == 'quit':
        quit()
    url = "https://genius.p.rapidapi.com/search"
    querystring = {"q": searchName}
    headers = {
        'x-rapidapi-host': "genius.p.rapidapi.com",
        'x-rapidapi-key': "b8f002b95fmshe4809d7a869cf0fp1d82fdjsna87bae548749"
    }
    results = requests.request("GET", url, headers=headers, params=querystring)
    info = results.json()
    if len(info['response']['hits']) < 0:
        return 'No Match Found!'
    print('Option'.ljust(10), 'Name')
    for i in range(len(info['response']['hits'])):
        print(str(i).ljust(10), info['response']['hits'][i]['result']['full_title'])
    while True:
        print()
        print('Type -return- To Go Back To Main Menu')
        print('Type -quit- To Terminate')
        print('To View Song Lyrics:')
        songName = input("Enter Song Option: ").lower()
        if songName == 'return':
            return True
        if songName == 'quit':
            quit()
        else:
            try:
                songName = int(songName)
                if songName < 0 or songName > len(info['response']['hits']):
                    print()
                    print("Input Value Must Be In Between Options Range".center(100, '*'))
                    continue
                break
            except:
                print()
                print("Input Must be Intrger or 'return' only".center(100, '*'))
                continue
    webbrowser.open_new(info['response']['hits'][songName]['result']['url'])
    print((info['response']['hits'][songName]['result']['full_title']+' Lyrics Opened!').center(100, '*'))
    k = input('Press enter To Go Back To Main Menu')
    return True




def seriesInfo():
    clear()
    wlcomeMsg = '<Welcome to ENTERTAINMENT FREAKS! Series Section>'
    print(wlcomeMsg.center(100))
    print('Type -return- To Go Back To Main Menu')
    print('Type -quit- To Terminate')
    searchName = input('Enter Series Name: ').lower()
    while len(searchName.strip()) == 0:
        clear()
        print(wlcomeMsg.center(100))
        print()
        print("Error No Name Provided".center(100, '*'))
        print()
        print('Type -return- To Go Back To Main Menu')
        print('Type -quit- To Terminate')
        searchName = input('Enter Series Name: ').lower()
    if searchName == 'return':
        return True
    if searchName == 'quit':
        quit()
    else:
        url = 'http://www.omdbapi.com/?i=tt3896198&apikey=1bdb5c29'
        searchParam = {'s': searchName, 'type': 'series'}
        searchResults = requests.get(url, params=searchParam)
        if searchResults.status_code != 200:
            return '404 File Not Found'
        else:
            movLst = searchResults.json()
            if movLst['Response'] == 'True':
                lst = [(movLst['Search'][i]['Title'], movLst['Search'][i]['Year']) for i in
                       range(len(movLst['Search']))]
                if len(lst) > 0:
                    clear()
                    print('Series Found!'.center(100, '*'))
                    print('option'.ljust(10), 'Name'.ljust(70), 'Year')
                    for i in range(len(lst)):
                        print(str(i).ljust(10), lst[i][0].ljust(70), lst[i][1])

                    while True:
                        print()
                        print('Type -return- To Go Back To Main Menu')
                        print('Type -quit- To Terminate')
                        print('To View Series Details:')
                        movName = input("Enter Series Option: ").lower()
                        if movName == 'return':
                            return True
                        if movName == 'quit':
                            quit()
                        else:
                            try:
                                movName = int(movName)
                                if movName < 0 or movName > len(lst):
                                    print()
                                    print("Input Value Must Be In Between Options Range".center(100, '*'))
                                    continue
                                break
                            except:
                                print()
                                print("Input Must be Intrger or 'return'/'quit' only".center(100, '*'))
                                continue
                    clear()
                    print('Series Selected: ', lst[int(movName)][0])
                    print()
                    param = {'t': lst[int(movName)][0], 'type': 'series'}
                    results = requests.get(url, params=param)
                    if results.status_code != 200:
                        return '404 File Not Found'
                    else:
                        movInfo = results.json()
                        if movInfo['Response'] == 'True':
                            d = ['Title', 'Year', 'Rated', 'Released', 'Runtime', 'Language', 'Country', 'totalSeasons', 'imdbRating']
                            for key in d:
                                print(key.ljust(30), ':', movInfo[key])
                            rest = ['Genre', 'Director', 'Writer', 'Actors', 'Awards']
                            for key in rest:
                                print((key + ':').center(50, '-'))
                                i = 1
                                for value in movInfo[key].split(','):
                                    print(str(i).ljust(30), ':' + str(value.strip()))
                                    i = i + 1
                            print('Plot:'.center(50, '-'))
                            plot = movInfo['Plot'].split()
                            j = 0
                            for i in range(6, len(plot) - 6, 6):
                                print(' '.join(plot[j:i]).center(50, ' '))
                                j = i
                            print(' '.join(plot[j:]).center(50, ' '))
                            print('Ratings:'.center(50, '-'))
                            for key in movInfo['Ratings']:
                                print(key['Source'].ljust(30), ':' + key['Value'].strip())
                            print()
                            k = input('Press enter To Go Back To Main Menu')
                            return True
                        else:
                            return '404 Series Not Found'
            else:
                return '404 Series Not Found'





def main():
    clear()
    print('ENTERTAINMENT FREAKS!'.center(100, '*'),'\n')
    wlcomeMsg = '<Welcome to ENTERTAINMENT FREAKS! select the following options.>'
    options = """0 -- Finding Movie Info
1 -- Search Similar Movies
2 -- Search Similar Song Artists
3 -- Search Song Lyrics
4 -- Finding Series Info"""
    while True:
        print(wlcomeMsg.center(100))
        print()
        print('Type -quit- To Terminate')
        print(options)
        option = input("Enter Choice (0-4/quit): ")
        if option == 'quit':
            quit()
        try:
            option = int(option)
            if option < 0 or option > 4:
                clear()
                print("Sorry, no numbers below zero or greater than options provided!".center(100, '*'))
                print()
                continue
        except:
            clear()
            print('Please Enter only Interger Value!'.center(100, '*'))
            print()
            continue
        if option == 0:
            val = movieInfo()
            if val == True:
                clear()
                continue
            else:
                clear()
                print(val.center(100, '*'))
                print()
        elif option == 1:
            val = similarMovie()
            if val == True:
                clear()
                continue
            else:
                clear()
                print(val.center(100, '*'))
                print()
        elif option == 2:
            val = similarSongs()
            if val == True:
                clear()
                continue
            else:
                clear()
                print(val.center(100, '*'))
                print()
        elif option == 3:
            val = songLyrics()
            if val == True:
                clear()
                continue
            else:
                clear()
                print(val.center(100, '*'))
                print()
        elif option == 4:
            val = seriesInfo()
            if val == True:
                clear()
                continue
            else:
                clear()
                print(val.center(100, '*'))
                print()

if __name__ == '__main__':
    main()
