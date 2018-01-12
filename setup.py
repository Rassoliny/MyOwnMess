from setuptools import setup
 
setup(name = "myownmessenger_test",
      version = "0.1.1",
      description = "My first messenger",
      author = "Rassoliny",
      author_email = "dimo120@yandex.ru",
      url = "https://github.com/Rassoliny/MyOwnMess",
      packages=["my_own_server", "my_own_jim", "my_own_repo", "my_own_logs", "my_own_client", "my_own_messenger"],
      python_requires='>=3.6',
      install_requires=[
            'PyQt5==5.9', 'SQLAlchemy==1.1.15'
      ],
      )