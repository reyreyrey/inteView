#! /usr/bin/python
import addressbook_pb2
import sys
import addressbook_pb2
person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phone.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME

def write(person):
    address_book = addressbook_pb2.AddressBook()

    # Read the existing address book.
    try:
        f = open(sys.argv[1], "rb")
        address_book.ParseFromString(f.read())
        f.close()
    except IOError:
        print
        sys.argv[1] + ": Could not open file.  Creating a new one."

    # Add an address.

    # Write the new address book back to disk.
    f = open(sys.argv[1], "wb")
    f.write(address_book.SerializeToString())
    f.close()
