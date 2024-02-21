import os
import requests

def get_extension(url:str)-> str|None:
    extensions:list[str]= ['.jpeg', '.jpg', '.gif', '.png', '.svg']
    for ext in extensions:
        if ext in url:
            return ext
        
def download_image(image_url:str, name:str, folder:str = None):
    if ext := get_extension(image_url):
        if folder:
            image_name:str = f'{folder}/{name}{ext}'
        else:
            image_name:str = f'{name}{ext}'
    else:
        raise Exception('Image extension could not be located')
    
    if os.path.isfile(image_name):
        raise Exception('File already exists')
    
    
    try:
        image_content:bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.wrie(image_content)
            print(f'Image file succesfully downloaded:{image_name}')
    
    except Exception as e:
        print(f'Error:{e}')
        
        
if __name__ == '__main__':
    input_url:str = input('Enter a url')
    input_name:str =  input('Enter a file name')
    
    print('Downloading')
    download_image(input_url, name=input_name, folder='images')
    
        