# Prevent, Mitigate, and Recover (PMR) Insight Collective Knowledge System (PICK) Tool

## Date: February 2020

### Resources

## Overview

## Motivation

## Related Work

## Our Approach

## Explaining PICK Tool to Users

## Notes to Developers

### Directory Structure

The directory structure used herein to manage documents and program-code files is as follows:

At the top level, files describing the project meant for users to read: **README.md**. The only other files that would be expected here is a **.gitignore** file, listing files and/or folders which Git should ignore and a **.git** file, containing git metadata. There are four subdirectories of this structure: **doc**, **src**, **target**, and **test**.

The **doc** directory shall contain all information material for documenting the project.

The **src** directory shall contain all source material for building the project.

The **target** directory shall contain all output material from building/running the program.

The **test** directory shall contain all unit test material (including test artifacts and test code) for testing software components in the project.

### Software Best Practices

Software best practices for this project include:

* One-line Docstrings in each function
* Single spaces between commas
* Up to 100 characters per line
* roduction-Style variable & function names
* Time-relevant & culturally-appropraite memes in project documentation
* No trailing whitespace

Note: All other Python best practices not mentioned herein shall be dictated by the python linting file that Visual Studio Code (VSCode) uses to perform static code analysis.

### Naming Conventions

The naming conventions expected by Team404 for all source material is as follows.

Naming conventions for all source material shall be short and descriptive of the contents therein. This includes the names of classes, objects, files, and variables. This convention is explored in more detail below. Note: All other Python naming conventions not mentioned herein shall be dictated by the python linting file that VSCode uses to perform static code analysis.

**The following applies to file names:**

Naming conventions for files within the /doc, /target directory shall follow CamelCase or CapWords naming convention
i.e. **KnownErrors.md, InstallGuide.md, FebruaryClientPresentation.pptx**

**The following applies to code written in Python:**

Files and module names shall be lowercased, without underscores

* i.e. **weblayout.py, trainsession.py, myfile.py**

Class names shall:

* Follow the CamelCase or CapWords naming convention
  * i.e. **Node, Vector, EventConfiguration, MyClass**

Method and Function names shall:

* Use all lowercase letters
* Use underscores ( _ ) to string together multiple words, as needed
  * i.e.

```python
  def generate_vector():
    # Words are strung together
  ```

Use a single leading underscore ( _ ) in the method name to indicate the method is private

* i.e.

```python
def _generate_vector():
    # This is private method
```

Class Methods shall have their first argument named cls
i.e.

```python
class Hooman:
    gender = “male”
    name = “Carter”

    @classmethod
    def get_gender(cls):
        ‘‘‘Access a class attribute via cls keyword’’’
        return(cls.gender)
```

Instance Methods shall have their first argument named self

* i.e.

```python
class Hooman:
    gender = “male”
    name = “Carter”

    def set_birthday(self):
        ‘‘‘Create instance attribute via self keyword’’’
        self.birthday = “August 8, 1998”
        print(self.name)
        print(self.birthday)

    # Note: The notable difference between cls and self is the method type
```

Variable names shall:

* Use all lowercase letters
* Avoid the use of single variable character names; the exception to this convention includes common language naming practices
  * i.e. **i, j** for indexes of arrays/loops/lists
* Use underscores ( _ ) to string together multiple words, as needed
  * i.e.

    ```python
    file_location = "C://Path/to/file"
    learning_rate = 1e-4
    mnist_classifier = get_mnist_model(file_location)
    ```

Use a double leading underscore ( __ ) in the variable to indicate the variable is private

* i.e.

```python
  __secondary_learning_rate = 1e-4
  # This is a private variable
  ```

Constant names shall:

* Use all uppercase letters
* Use underscores ( _ ) to string together multiple words, as needed
  * i.e.

  ```python
  KILOMETER = 1, ACRE_SIZE = 1, HOURS_PER_DAY = 24
  ```

### Project Dependencies

The dependencies for this project are as follows:

1. PyQt5

### Warnings & Known Issues

1. Partial devlopment for this project was done on Microsoft Visual Studo Code (*VSCode*).
2. If developing in VSCode, **DO NOT ENABLE *Microsoft Python Language Server* or *Microsoft Python Language Server (preview)***
    * Enabling the language server will render all python code unusable.
        * If enabled by accident, there are two known solutions to remedy (either option should fix the issue):
            1. Bypass the language server by reverting ```python.jediEnabled``` to ```true```.
            2. Reinstall VSCode

### Developed with ❤️ in The City of the 9-1-5
