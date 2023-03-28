# Strings Collections and Iteration

Collection types
### Strings
Sequence is immutable (can’t modify contents)
Multipline strings “”” 3 quotes
Bytes 
Sequences of bytes, used for raw binary data and fixed width
List 
Sequences of objects, mutable, a workhorse of python data sctructures
Mutable, heterogeneous sequences
Delimited by square brackets
Separated by commas
Access elements with square brackets
Dict
Fundamental data structure in python, maps keys to values, 
For loops


## Modularity

### Decomposition


 - naming special functions __ <- duncder- double underscore>
 - __name__ specially named variable allowing us to detect whether a module is run as a script or imported into another module

 - def is a statement. 
 - top-level functions are defined when a module is imported or run

 Python module - convenient import with API
 Python script - convenient execution from the command line

 - make simple scripts importable. 
 Python program - perhaps composed of many modules
 A module is executed once, on first import
 def is a stmt which binds code to a name


Docstrings
- literal strings which document functions, modules and classes. 
- They must be the first statement in the blocks for these constructs. 

help() can retrieve docstrings
modules can have docstrings

Shebang - program loader to determine which python to run
#!
 to have effect run 
 chmod +x words.py
 ./words.py http://sixty-north.com/c/t.txt


The python object model
named references to objects
- id() returns a unique integer identifier for an object that is constant for the life of the object. 
- is operator, 
- the assignment operator only ever assigns objects to names, it never copies an object by value. 
- a is b is true because same object (same box)


Mutable objects
- python doesn't have variables in the sense of boxes holding a value
- python has naed references to objects

value vs. identity equality
- fundamentally different concepts.
- comparison by value can be controlled programatically. 
- identity comparison is unalterably defined by language




passing arguments and returning values
- function arguments are transferred using pass-by-object-reference. 
- references to objects are copied, not the objects themselves. 
- arguments with default values must come after those without default values. 
- positional versus keyword argument
- always use immutable objects for default values. 

python's type system
- python will not generally perform implicit conversions between types
- python uses dynamic typing
- python has strong typing

scopes to limit name access
- 4 types
- 1 local - inside the current function
- 2 enclosing - inside enclosing functions
- 3 global - at the top level of the module
- 4 built-in - in the special builtins module

"Everything is an object"
- can access the name of a function or module with __name__
- docstrings can be accessed through __doc__


Collection types
Tuples 
- immutable sequences of arbitrary obejcts. use the trailing comma, to suggest the tupple type. 
- tuple unpacking - destructuring operation that unpacks data structures into named references: minmax(), 

Strings
- are immutable and cannot be modified in place. 
- prefer join method to create strings. concatenation with + results in temporaries. str.join() inserts a separator between a collection of strings. call join on the separator string. 
- to concatenate invoke join on empty text to create something from nothing. 
- partition() - returns a tuple. good for tuple unpacking. 
- format() - inserts text in position. can also insert math formats. 
- f strings - to insert value into a string. The result is in the string. not limited to simple references and can call functions. 

Range
- sequence representing an arithmetic progression of integers
- range does not support keyword arguments

Lists
- negative indices - index from the end of sequence using negative numbers, last element being -1
- slicing is a form of extended indexing for referring to a portion of a list or other sequence. Easy way to copy a list object[:] only refernces are copied
- all these techniques perform shallow copies
- deep copy use copy module (rare)
- to find element in list use list.index() method. It returns the index of the first list element which is equal to the argument. 
- remove elemens from a list using the keyword `del` a_list[index]
- list.insert() - inserts an item into a list. Accepts an item and the index of the new item. 
- list.reverse()
- list.sort()


Dictionaries
- dictionary copying is shallow, reference to objects no the objects themselves. 
- dict.update() - adds entries from one dictionary into another, call this on the dictionary that is to be updated. 
- dictionary iteration - dictionaries yield the next key on each iteration. Values can be retrieved using the square bracket operator. 
- dict.items() - iterates over keys and values in tandem. 
- pprint - without the "ass pp", the pprint function would mask the pprint module. This kind of duplicate naming is probably best avoided in your own APIs. 


Sets
- unordered collection of unique elements. Sets are mutable, but each elementin set is immutable. 
- set() constructor to create empty set. 
- set to remove duplicates
- discard to remove
- set algebra operations are most powerful. 
- union operation to check for 
- intersection to find both between sets
- difference operator
- symmetric_difference method() either or not both. 
- issubset() check all emlements in first set are present in second set. 
- issuperset() check all elements in second set are present in first set. 

Protocols
- a set of operations that a type must support to implement the protocol. 
- do not need to be defined as interfaces or base classes. 
- types only need to provide functioning implementations. 
Types
- container
- sized - len() on collection
- iterable - yield items one by one as they are requested. 
- sequence - 
- mutable sequence
- mutable set
- mutable mapping


# Exceptions

exceptions and control flow
- exception handling - mechanism for interrupting normal program flow and continuing in surrounding context
- Raising an exception - event of interrupting normal flow
- handling an exception - handling raised exception, control flow is transfered to the exception handler
- unhandled exceptions - exception propagates up the callstack to the start of the program, cause program to terminate
- exception object- contains info about where and why exceptional event occured is transported from the point it occured to exception handler


handling exceptions
exceptions and programmer

re-raising exceptions

exceptions are part of the API

exceptions and protocols
avoid explicit type checks
its easier to ask forgiveness 
cleanup actions



