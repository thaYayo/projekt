'''Hashtool module for ITHS projekt. 
Takes arguments(hash) through cli when running script
and matches sha256 until password is found 
'''
import argparse
import itertools
import string
import hashlib


def brute_force(target_password):
    '''Funtion for cracking hashed passwords'''
    charcters = string.ascii_lowercase + string.digits


    for reps in range(1, 10):
        for guess in itertools.product(charcters,repeat=reps):
            guess = ''.join(guess)
            print(f"Checking: {guess}")
            hash_object = hashlib.sha256()
            hash_object.update(guess.encode())
            guess_hash_value = hash_object.hexdigest()

            if guess_hash_value == target_password:
                print(f"password found: {guess}")
                return guess
    return None

def main():
    '''function for handling arguments for cli commmands'''

    parser = argparse.ArgumentParser(description="knäcka hashade lösenord")
    parser.add_argument("hash", help="ange lösenords hash ")


    args = parser.parse_args()

    if valid_hex(args.hash) is True:
        brute_force(args.hash)
    else:
        print("Ogiltig sha256 hash")

def valid_hex(hex_string: str) -> bool:
    """Check if a string is a valid hex."""
    try:
        bytes.fromhex(hex_string)
        return True
    except ValueError:
        return False


if __name__=="__main__":
    main()
