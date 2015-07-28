from sys import argv, exit
from getopt import getopt, GetoptError

# Encodes a message and writes the secret message into a file

class Encoder():
    """ Entry class of the encoder module.
    """

    def __init__(self, message=None, file_name=None):
        """ Initializes message, secret_message and secret_filename.
        :param message:string
        :return:None
        """
        if message is None:
            self.message = input("Provide the message to encode: ")
        else:
            self.message = message

        if file_name is None:
            self.secret_file_name = input("What is the output file name? ")
        else:
            self.secret_file_name = file_name
        self.secret_message = ""

    def transform(self):
        """ Encodes input message into the secret message
        :return:secret_message:string
        """
        # Put transformation code here.
        self.secret_message = " ".join([str(ord(c)) for c in self.message])

        # Return secret message
        return self.secret_message

    def make_secret(self):
        """ Creates secret output file and writes secret message to it.
        :return:secret_file_name:file
        """
        with open(self.secret_file_name, "w") as secret_file:
            secret_file.write(self.secret_message)

if __name__ == "__main__":
    enc = Encoder()
    enc.transform()
    enc.make_secret()
    print("Done encoding '{}' and writing the secret message to '{}'.".format(enc.message, enc.secret_file_name))
