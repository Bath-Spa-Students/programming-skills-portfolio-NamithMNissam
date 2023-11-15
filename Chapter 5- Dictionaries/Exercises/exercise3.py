#Create a glossay with programming words and their meanings
glossary = {
    "Variable": "A specific place in memory designated for data storage.",
    "Function": "A section of code that may be executed to carry out a certain action or function.",
    "Loop": "A a control structure that, if a certain condition is satisfied, repeats a series of assertions.",
    "Conditional Statement": "A statement that allows for different code to be executed depending on a condition.",
    "List": "A sorted assortment of objects, which may represent many data kinds.",
    "Dictionary": "A collection of key-value pairs with data storage and retrieval capabilities.",
    "Tuple": "A set of components that are arranged in a fixed order.",
    "String": "A string of letters surrounded by one or more quotations.",
    "Boolean": "A form of data that may express values as True or False.",
    "Method": "A process linked to a particular object or data type."
}

#Print each word and its meaning neatly formatted with a loop
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")