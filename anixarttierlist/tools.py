def add_url_to_file(url: str, path: str = './temp/urls.txt'):
    with open(path, 'a+') as file:
        file.write(url+'\n')
