#setup.py 파일이 있으면 pip로 설치 가능하다.
from setuptools import setup

setup(
    name = "myapi", #이 이름으로 패키지가 설치
    version = "0.0.1",
    description = "my api lib" ,
    url = "https://github.com/sond40/api_project.git",
    author = "KJH",
    author_email= "skdltmdpdj7@hanmail.net",
    packages = ["my_api"],
    install_requires = [
        "requests"
    ]

)
