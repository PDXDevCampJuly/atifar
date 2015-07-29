import argparse

from random import randint
from sys import exit

# This class decodes a secret message from a file and prints the decoded message
class Decoder():
    """ Entry class of the decoder module.
    """

    def __init__(self):
        """ Initialize secret_file_name and strong_decode attributes from command
        line arguments. Initialize message and secret message attributes with empty string.
        :return:None
        """
        # Configure command line argument parser
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--inputfile", help="input file name", required=True)
        parser.add_argument("-s", "--secure", help="use more secure code", action="store_true")
        args = parser.parse_args()
        # Initialize class attributes
        self.secret_file_name = args.inputfile
        self.strong_decode = args.secure
        self.secret_message = ""
        self.message = ""

    def detransform(self):
        """ Decode secret message using simple substitution and store it in message attribute.
        :return:None
        """
        # Perform substitution
        self.message = "".join([chr(int(symbol)) for symbol in self.secret_message.split()])

    def detransform_hard(self):
        """ Decode secret message and store it in message attribute.
        :return:None
        """
        # Perform reverse transformation
        for symbol in self.secret_message.split():
            if int(symbol[0]) == 2:
                char = str(chr(int(symbol[3:5])))
            else:
                char = str(chr(int(symbol[3:6])))
            self.message += char
        self.message  = self.message.rstrip()

    def read_secret_file(self):
        """ Reads secret from input file and assigns it to secret message attribute.
        :return:None
        """
        # Open input file and read secret message into class attribute, then close file
        with open(self.secret_file_name, "r") as secret_file:
            self.secret_message = secret_file.read()

    def is_incorrect_decode_type_slected(self):
        """ Check if the secret message contains simple or secure encoded symbols. Generate
        error if selected decoding type is inappropriate.
        :return:incorrect:Boolean
        """
        # Check the length of the first symbol in the secret message
        symbol = self.secret_message.split()[0]
        symbol_length = len(symbol)
        # Return True if the incorrect decode type was specified
        return (symbol_length <= 3 and self.strong_decode) or (symbol_length > 3 and not self.strong_decode)

if __name__ == "__main__":
    dec = Decoder()
    dec.read_secret_file()
    # Check if the secret message contains simple or secure encoded symbols. Generate
    # error if selected decoding type is inappropriate
    if dec.is_incorrect_decode_type_slected():
        if dec.strong_decode:
            print("The '{}' file was encoded using the basic encoding scheme. Run the decoder script without the '-s' option!".format(dec.secret_file_name))
        else:
            print("The '{}' file was encoded using the secure encoding scheme. Run the decoder script with the '-s' option!".format(dec.secret_file_name))
        exit()
    if dec.strong_decode:
        dec.detransform_hard()
    else:
        dec.detransform()
    print("Done decoding '{}'.".format(dec.secret_file_name))
    print("Decoded message is '", dec.message, "'", sep="")
