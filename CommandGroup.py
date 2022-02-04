from Command import Command
from os.path import exists

class CommandGroup:
    """
    """
    fName = ""
    commands = []


    def __init__(self, filename:str):
        """Creates a new CommandGroup object. 

        Args:
            filename (str): An existing file path and file name for a CommandGroup to be stored in.
        """
        self.fName = filename
        if (exists(self.fName)):
            raise NotImplementedError("Cannot read old files yet.")
        
        

    def addCommand(self, command:Command):
        """Adds an Command to the CommandGroup, this method adds to the end of the CommandGroup

        Args:
            Command (Command): The Command to add to the CommandGroup. Must be a valid Command object.
        """
        if (not isinstance(command, Command)):
            raise TypeError("command must be of type Command")
        self.commands.append(command)

    def addCommand(self, command:Command, location:int):
        """Adds an Command to the CommandGroup at the specified location.

        Args:
            Command (Command): The Command to be added to the CommandGroup. must be a valid Command object
            location (int): the location to add the Command to. location must be >= 0 and <len(CommandGroup)
        """
        if (not isinstance(command, Command)):
            raise TypeError("command must be of type Command")
        if (location >=len(self) or location < 0):
            raise ValueError("invalid index")
        self.commands.insert(location, command)
        pass

    def removeCommandMatch(self, command:Command):
        """removes an Command by finding a matching Command. This cycles through all Commands in the CommandGroup 
        and performs an equality check, for better performance, use with an integer for better performance

        Args:
            Command (Command): the Command to delete. must be a valid Command object
        """
        if (not isinstance(command, Command)):
            raise TypeError("command must be of type Command")
        if (command in self.commands):
            self.commands.remove(command)
        pass
    
    def removeCommandLocation(self, location:int):
        """removes an Command by location.

        Args:
            location (int): The location of the Command to be removed. must be >= 0 and < len(CommandGroup)
        """
        if (location >=len(self) or location < 0):
            raise ValueError("invalid index")
        del self.commands[location]
        pass

    def writeToFile(self):
        """This saves the CommandGroup to disk in a form that is readable to the [module name].
        """
        
        with open(self.fName, "wb") as f:
            for i in self.commands:
                f.write(hex(i))
        pass
    
    def __iadd__(self, x:Command):
        """this functions identically to the add function.

        Args:
            x (Command): The Command to add to the end of this CommandGroup
        """
        self = self + x

    def __add__(self, x:Command):
        """adds to the end of a CommandGroup

        Args:
            x (Command): In the case of Command, adds the Command to the end of the CommandGroup.
        """
        pass

    def __isub__(self, x):
        """functions the same as removeCommandLocation or removeCommandMatch, depending on argument type

        Args:
            x (Int or Command): same as removeCommandLocation or removeCommandMatch, depending on argument type
        """
        self = self - x
    
    def __sub__(self, x:int):
        """functions the same as removeCommandLocation or removeCommandMatch, depending on argument type

        Args:
            x (Int or Command): same as removeCommandLocation or removeCommandMatch, depending on argument type
        """
        pass

    def __str__(self)->str:
        """creates a string representation of the CommandGroup, good for visualizations. 
        CAUTION: this is not the machine readable output. sending this to a cubedOS device will result in unexpected behaviour
        """
        pass

    def __hex__(self)->str:
        """this generates a hex dump of the CommandGroup, and will represent the actual bytes going to the file that will contain the CommandGroup. 
        this is not the same as the hex value for the string conversion
        """
        pass

    def __getitem__(self, x:int)->Command:
        """Gets the Command specified by the number in the array.

        Args:
            x (int): the location of the Command to get. must be >=0 and <len(self)

        Returns:
            Command: the Command that is at the specified location.
        """
        pass
    
