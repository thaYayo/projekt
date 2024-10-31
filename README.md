# ITHS Projekt

![License](https://img.shields.io/github/license/thaYayo/ithsprojekt)
![Issues](https://img.shields.io/github/issues/thaYayo/ithsprojekt)
![Stars](https://img.shields.io/github/stars/thaYayo/ithsprojekt)

This projekt is a very basic toolbox for pentesting purposes. the projekt is written in python and consists of a main menu aswell as 3 tools.
- hashtool - for cracking unsalted hashes
- apifuzz - fuzzes through enpoints of given api
- cryptotool - encrypts and decrypts file with generated key or password.


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

To install and set up this project locally, follow these steps:

1. Clone the repository:
   ```git clone https://github.com/thaYayo/ithsprojekt.git ```
2. install requirements:
```pip install -r requirements.txt```
3. Run the script:
``` python mainmenu.py```

## Usage
You can use Toolbox to start the menu that binds the 3 tools together by running the comands: 

```python Toolbox.py```

### API fuzzer:
You can use apifuzzer to fuzz through possible api endpoints by running the comands: 

```python Toolbox.py``` and selecting it through the menu or ``python apifuzzer.py [apiurl]```

#### Known limitations:
1. The pattern recognition for api urls is set to accept the current format: ex. https://api.sr.se/api/v2/.  
Feel free to provide own pattern if you would like to fuzz through other urls.

2. The endpoints used to fuzz: https://gist.github.com/yassineaboukir/8e12adefbd505ef704674ad6ad48743d  
Feel free to provide your own list or enpoints, if you would like other endpoints or feel like something is missing.
3. Only tested on windows 10

### hashtool
Use apifuzzer to fuzz through possible api endpoints by running the comands: 

```python Toolbox.py``` and selecting it through the menu or ``python hashtool.py [sha256 hash]```

### known limitations:
- Only cracks unsalted sha256 hashes
- Unoptimized. Takes long time and lots of cpu/gpu resources.
- Only tested on windows 10

### crypto_tool
You can use crypto_tool.py through by running the comands: 

```python Toolbox.py``` and selecting it through the menu or ``python crypto_tool.py```

### Encrypt file:
To encrypt a file:
```python crypto_tool.py encrypt [FILE] -p [PASSWORD] -k [KEYFILE]```
- ```file```: Required file to encrypt
- ```-p, --password```: Optional encryption with password key derivation
- ```-k, --key```: Optional key derivation

### Encrypt file:
To encrypt a file:
```python crypto_tool.py decrypt [FILE] -p [PASSWORD] -k [KEYFILE]```
- ```file```: Required file to decrypt
- ```-p, --password```: Optional encryption with password key derivation
- ```-k, --key```: Optional key derivation

### Generate key:
To generate a fernet key:
```python crypto_tool.py generate -o [path\filename]``
- ```-o, --output```: Optional path/filename where key is to be stored.

### known limitations:
Only tested on windows 10

## Features
- API fuzzer
- Encryption/Decryption tool
- Hashbreaking tool

## Contributing
**For contributions:**
1. Clone the repo
2. Create your feature branch (git checkout -b feature/something) 
3. Commit your changes (git commit -m 'add something')
4. Push to the branch (git push origin feature/something)
5. Open a pull request

## License 
Distributed under the MIT License. See LICENSE for more information.

