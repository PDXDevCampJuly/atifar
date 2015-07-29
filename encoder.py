import argparse

from random import randint

# This class encodes a message and writes the secret message into a file
class Encoder():
    """ Entry class of the encoder module.
    """

    def __init__(self):
        """ Initialize message, secret_filename and strong_encode attributes from command line arguments.
        Initialize secret_message attribute with empty string.
        :return:None
        """
        # Configure command line argument parser
        parser = argparse.ArgumentParser()
        parser.add_argument("-m", "--message", help="message to encode", required=True)
        parser.add_argument("-f", "--outputfile", help="output file name", required=True)
        parser.add_argument("-s", "--secure", help="use more secure code", action="store_true")
        args = parser.parse_args()
        # Initialize class attributes
        self.message = args.message
        self.secret_file_name = args.outputfile
        self.strong_encode = args.secure
        self.secret_message = ""

    def transform(self):
        """ Encode input message into the secret message using simple substitution.
        :return:secret_message:string
        """
        # Perform substitution
        self.secret_message = " ".join([str(ord(c)) for c in self.message])
        # Return secret message
        return self.secret_message

    def generate_padding(self):
        """ Generate two-tuple of padding strings for use in transform_hard().
        Each string is a random two-digit number in string representation.
        :return:padding:two-tuple of string
        """
        padding1 = str(randint(10, 99))
        padding2 = str(randint(10, 99))
        return (padding1, padding2)

    def transform_hard(self, padding):
        """ Encode input message into the secret message using a harder-to-break scheme.
        :param:padding:two-tuple of string
        :return:secret_message:string
        """
        # Perform transformation
        for c in self.message:
            control = str(len(str(ord(c))))
            code = control + padding[0] + str(ord(c)) + padding[1] + " "
            self.secret_message += code
        self.secret_message  = self.secret_message.rstrip()
        # Return secret message
        return self.secret_message

    def make_secret(self):
        """ Create secret output file and write secret message into it.
        :return:secret_file_name:file
        """
        # Create text file, write secret message into it, then close file
        with open(self.secret_file_name, "w") as secret_file:
            secret_file.write(self.secret_message)

if __name__ == "__main__":
    enc = Encoder()
    if enc.strong_encode:
        padding = enc.generate_padding()
        enc.transform_hard(padding)
    else:
        enc.transform()
    enc.make_secret()
    print("Done encoding '{}' and writing the secret message to '{}'.".format(enc.message, enc.secret_file_name))
    # print("Secret message is '", enc.secret_message, "'", sep="")
