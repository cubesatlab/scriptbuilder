from Address import Address
from Args import Args
from CubedOSTime import CubedOSTime


class Command:
    

    def __init__(self, addr:Address, args:Args, time:CubedOSTime):
        """Creates a new Command

        Args:
            addr (Address): The address that the command is addressed to
            args (Args): The arguments to the command
            time (CubedOSTime): The time to commit the command.
        """
        pass

    def changeArgs(self, args:Args):
        """Method to change the arguments to a command

        Args:
            args (Args): The arguments to replace the old arguments
        """
        pass

    def changeTime(self, time:CubedOSTime):
        """Changes the time that the command will be run

        Args:
            time (CubedOSTime): The new time to run the message
        """
        pass
    
    def changeAddress(self, address:Address):
        """Changes the address that the command will be sent to

        Args:
            address (Address): The new address to send the command to
        """
        pass

    def getArgs(self)->Args:
        """Returns the arguments to be used while running the command

        Returns:
            Args: The arguments that the command will run with
        """
        pass

    def getAddress(self)->Address:
        """Returns the address that the command will be sent to

        Returns:
            Address: The address that the command will be sent to
        """
        pass

    def getTime(self)->CubedOSTime:
        """returns the time that the command will be run at

        Returns:
            CubedOSTime: The tme that the command will be run at
        """
        pass

    def __str__()->str:
        """generates a human readable string representation of the command

        Returns:
            str: The human readable string
        """
        pass

    def __hex__()->str:
        """returns a machine readable string representation of the command

        Returns:
            str: The machine readable string
        """
        pass

    def __eq__(self, __o: Command) -> bool:
        """Compares to another Command. if Address, Time, and Args are all matching, then the two objects are equal

        Args:
            __o (Command): The other Command to be checked against

        Returns:
            bool: If the two Commands are equal
        """
        pass

    