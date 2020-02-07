# Prevent, Mitigate, and Recover (PMR) Insight Collective Knowledge System (PICK) Tool

## Overview

**Date: 07 February 2020**</br>
**Version: [0.1.2](doc/ReleaseNotes.md)**</br>
**Known Errors: [Current Release](doc/KnownErrors.md)**

## Motivation

The following is an excerpt from [[3](#resources)], which defines the scope and motivation of PICK Tool:

"The Lethality, Survivability, and HSI Directorate (LSH) recognizes the complexity and the time it takes to analyze the applicable logs, observation notes, and other artifacts gathered from an adversarial assessment from the red, blue, and white teams and generate a report that presents the events that took place during the adversarial assessment. They want a system that would aid their analysts in correlating [the] red team’s activities to [the] blue team’s responses and represent the events that took place during an adversarial assessment graphically. 

"The University of Texas at El Paso (UTEP) and LSH are collaborating to develop Prevent, Mitigate, and Recover (PMR) Insight Collective Knowledge System (PICK) that will provide the ability to correlate red team’s activities to blue team’s responses and graphically represent the events that took place during an adversarial assessment.

## Our Approach

## Explaining PICK Tool to Users

## Notes to Developers

### Directory Structure

The directory structure used herein to manage documents and program-code files is as follows:

At the top level, files describing the project meant for users to read: ```README.md```. The only other files that would be expected here is a ```.gitignore``` file, listing files and/or folders which Git should ignore, a ```.travis.yml``` file, assisting with project-related software testing, and a ```.git``` file, containing git metadata. There are five subdirectories of this structure: ```/doc```, ```/src```, ```/target```, ```/test```.

The ```/build``` directory shall contain all scripts/tools needed for building the project.

The ```/doc``` directory shall contain all information material for documenting the project.

The ```/src``` directory shall contain all source material for building the project. At the top level of this directory, the only file that would be expected here is a ```picktool.py``` file, which is the main executable file for this project.

The ```/target``` directory shall contain all output material from building/running the program.

The ```/test``` directory shall contain all unit test material (including test artifacts and test code) for testing software components in the project.

### Software Best Practices

Software best practices for this project include:

* One-line Docstrings in each function
* Single spaces between commas
* Up to 100 characters per line
* production-Style variable & function names
* No trailing whitespace

**Note**: All other Python best practices not mentioned herein shall be dictated by the python linting file that Visual Studio Code (VSCode) uses to perform static code analysis.

### Naming Conventions

The naming conventions expected by Team404 for all source material is as follows.

Naming conventions for all source material shall be short and descriptive of the contents therein. This includes the names of classes, objects, files, and variables. This convention is explored in more detail below.

**Note**: All other Python naming conventions not mentioned herein shall be dictated by the python linting file that VSCode uses to perform static code analysis.

**The following applies to file names:**

Naming conventions for files within the /doc, /target directory shall follow CamelCase or CapWords naming convention
i.e. ```KnownErrors.md```, ```InstallGuide.md```, ```FebruaryClientPresentation.pptx```

**The following applies to code written in Python:**

Files and module names shall be lowercased, without underscores

* i.e. ```weblayout.py```, ```trainsession.py```, ```myfile.py```

Class names shall:

* Follow the CamelCase or CapWords naming convention
 * i.e. ```Node```, ```Vector```, ```EventConfiguration```, ```MyClass```

Method and Function names shall:

* Use all lowercase letters
* Use underscores ```_``` to string together multiple words, as needed, i.e.

```python
 def generate_vector():
 # Words are strung together
 ```

Use a single leading underscore ```_```in the method name to indicate the method is private, i.e.

```python
def _generate_vector():
 # This is private method
```

Class Methods shall have their first argument named ```cls```, i.e.

```python
class Hooman:
 gender = “male”
 name = “Carter”

 @classmethod
 def get_gender(cls):
 ‘‘‘Access a class attribute via cls keyword’’’
 return(cls.gender)
```

Instance Methods shall have their first argument named ```self```, i.e.

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
 * i.e. ```i```, ```j``` for indexes of arrays/loops/lists
* Use underscores ```_``` to string together multiple words, as needed
 * i.e.

 ```python
 file_location = "C://Path/to/file"
 learning_rate = 1e-4
 mnist_classifier = get_mnist_model(file_location)
 ```

Use a double leading underscore ```__``` in the variable to indicate the variable is private, i.e.

```python
 __secondary_learning_rate = 1e-4
 # This is a private variable
 ```

Constant names shall:

* Use all uppercase letters
* Use underscores ```_``` to string together multiple words, as needed, i.e.

 ```python
 KILOMETER = 1, ACRE_SIZE = 1, HOURS_PER_DAY = 24
 ```

### Merging & Pull Requests

To ensure that a functional, quality application is built by Team404, all contributors are required to open a pull request if any of the following conditions are met:

* When a contributor wishes to merge a _componant_ branch into a _feature_ branch
* When a contributor wishes to merge a _feature_ branch into the _master_ branch

Pull Requests may be assigned to any other Team404 member to review. No individual may review and/or approve their own Pull Request. It is the responsibility of the reviewer to ensure:

1. The originating contributor is merging the correct branches
2. There are no merge conflicts
3. Any new code contained in the pull request works as intended on a Kali Linux-based machine (this can include a virtual machine)
4. Any new code follows the naming conventions and style guide listed in the [Team404 SCM Document](doc/Team6Team404SCMPlan.doc)

Should any issues exist in the Pull Request, the reviewer shall:

1. Leave a comment or change request (as defined in the Team404 SCM Document)
2. Request changes from the originating contributor.

Upon a successful review of the Pull Request, the reviewer shall:

1. Leave the comment, "lgtm" (shorthand for _looks good to me_)
2. Approve the Pull Request
3. Merge the intended branches
4. Inform all other Team404 members that a ```git pull``` of the merged branch is required on their local machine

### Project Dependencies

The dependencies for this project are as follows:

1. PyQt5

### Warnings & Known Issues

1. Installing PyQt5 on macOS Catalina & Ubuntu 18.04 may result in the following error:

 ```text
 python setup.py egg_info" failed with error code 1 in /tmp/pip-build-2hg9eeu7/pyqt5/
 ```

 **Resolution:** install PyQt5 by running the following command:

 ```text
 sudo apt-get install python3-pyqt5
 ```

2. Partial development for this project was done on Microsoft Visual Studio Code (*VSCode*).
* If developing in VSCode, **DO NOT ENABLE *Microsoft Python Language Server* or *Microsoft Python Language Server (preview)***
* Enabling the language server will render all python code unusable.
 ***Resolution(s)** (Select one):
    1. Bypass the language server by reverting ```python.jediEnabled``` to ```true```.
    2. Reinstall VSCode

## Resources

* [1] O. Perez et al, Requirements Definition Document, Lethality, Survivability and HSI Directorate, 2019.
* [2] “Components and Containers in AWT”. Internet: https://www.cs.utexas.edu/~mitra/csSpring2009/cs313/lectures/GUIComponents.html, 2009 [Jan. 28, 2019]
* [3] E. Tai-Ramirez & S. Roach, SRS_v7. Internet: https://github.com/CS4311-spring-2020/pick-tool-team06-team-404/blob/master/doc/SRSv7.pdf, 2020 (Jan. 30, 2020)
