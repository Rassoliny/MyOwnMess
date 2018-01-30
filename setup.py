from setuptools import setup
from glob import glob
 
setup(name = "myownmessenger",
      version = "0.1",
      description = "My first messenger",
      include_package_data=True,
      author = "Rassoliny",
      author_email = "dimo120@yandex.ru",
      url = "https://github.com/Rassoliny/MyOwnMess",
      packages=["my_own_server", "my_own_jim", "my_own_repo", "my_own_logs", "my_own_messenger"],
      package_data={
        'my_own_messenger': [
            'my_own_messenger/my_own_client/*',
            'my_own_messenger/*',
        ],
      },
      python_requires='>=3.6',
      install_requires=[
            'PyQt5>=5.9', 'SQLAlchemy>=1.1.15'
      ],
      entry_points={
        'gui_scripts': [
            'MyOwnMessenger = my_own_messenger.messenger:main',
        ],
        'console_scripts': [
            'MyOwnServer = my_own_server.server:main',
        ]
    },
    )