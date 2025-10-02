import requests
from datetime import datetime

# demo_list = [0, 1, 3, 4, 5, 6, 7, 8, 9]

# try:
#     result = demo_list[0] + demo_list[10]
# except IndexError as exp:
#     print(f"Error {exp}")
#     result = 0
# else:
#     print(result)
# finally:
#     print("Completed")

# #############

class BadLink(Exception):
    def __init__(self, msg = "This link is not file"):
        self.message = msg
        super().__init__(self.message)


def get_file_name(input):
    if len(input) > 110:
        return f"{input.split("/")[11]}.jpg"
    else:
        return f"{str(datetime.now()).split(".")}.jpg"




def get_file(url: str) -> None:

    try:
        response = requests.get(url)
    except requests.exceptions.MissingSchema:
        print(f"{url} - is not link")
        return
    
    if response.status_code == 200:
        dump = response.content
    else:
        print("No data")
        return

    file_name = (
        url.split("/")[-1] 
        if len(url.split("/")[-1]) < 5 
        else get_file_name(url)
    )
    
    try:
        with open(file_name, "wb") as f:
            f.write(dump)
    except FileNotFoundError:
        with open("empty_file_name", "wb") as f:
            f.write(dump)
        raise BadLink() 
    finally:
        print("File writed")


if __name__ == "__main__":
    URL1 = "https://www.ixbt.com/img/n1/news/2023/6/4/IMG_0826_large.JPG"
    URL2 = "https://www.ixbt.com/img/n1/news/2023/6/4/IMG_0828_large.JPG"
    URL3 = "https://www.ixbt.com/img/n1/news/2023/6/4/IMG_0829_large.JPG"
    URL4 = "https://habrastorage.org/r/w1560/getpro/habr/upload_files/1fa/427/efe/1fa427efe4a774170c4e3a14fb2e390a.png"
    URL5 = "https://habr.com/ru/companies/otus/articles/951406/"

    URL6 = "532262362" 

    urls = (URL1, URL3, URL2, URL6, URL5, URL4, URL1,)

    for url in urls:
        try:
            get_file(url)
        except BadLink as e:
            print(f"Not Data {e}")    
        # get_file(url)