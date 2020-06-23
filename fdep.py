# fdep.py
#   Start point of this app. Process arguments, configs.

# Libraries
import os
import argparse
import configparser


# Config file processing
config = configparser.ConfigParser()
config.read("fdep.conf")


# Argument processing

## Positional arguments
parser = argparse.ArgumentParser() # Parser object
parser.add_argument("template", type=str, help="Project template to use")
parser.add_argument("project" , type=str, help="Project") 
parser.add_argument("path"    , type=str, help="Project path, create one in current directory if empty.", nargs="?", default=os.getcwd()) # Default to current working directory, if none wwas specified

## Optional arguments
parser.add_argument("-v", "--version", action="version", version='%(prog)s '+config["FDep"]["Version"])
parser.add_argument("-y", "--yes", action="store_true", help="Say yes to everything, one word can change everything") #It's a reference to Yes Man, if you didn't get it
parser.add_argument("-g", "--git", action="store_true", help="Create git repo")
args = parser.parse_args() # Parse args


# Arguments verifying

## Template check: Look for templates, and then verify the setting and content is correct.
if args.template:
    if os.path.isdir(config["DEFAULT"]["TemplateDirectory"]+args.template) is False:
        print("Template \"" + args.template + "\" doesn't exist or isn't a directory")
        exit(1)  # Exit with error code 1
        # TODO: Verify configs and contents of template

## Path Check: Make sure the path exists.
if args.path:
    if os.path.isdir(args.path) is False:
        print("Path \"" + args.path + "\" doesn't exist or isn't a directory")
        exit(1) # Exit with error code 1

## Project name Check: Check if the project already exists in the target directory.
if args.project:
    check_path = args.path + ("" if args.path[-1]=="/" else "/") + args.project
    if os.path.isdir(args.path + "/" + args.project):
        print("A directory or file already exists as \"" + args.path + "/" + args.project + "\"")
        exit(1)


# Print out datas to verify
print("FDep starts\n")
print("Template: " + args.template)
print("Project:  " + args.project)
print("Path:     " + args.path)
print("") # Keep this line so the output looks good.


# Ask user if they want to proceed

## If "-y" or "--yes" is in the arguments
if args.yes:
    print("Argument \"--yes\" or \"-y\" is provided, default all prompt to yes.")

## If "-y" or "--yes" is not in the arguments
else:
    proceed = [] # It should be a str, as you can see in the if statement below. So give it a type randomly other than str will do
    while True:
        proceed = input("Confirm to proceed? (Y/n): ")
        if type(proceed) is not str: # No input detected
            continue # Ask again
        elif proceed.lower() == "y": # "Y" or "y" detected
            break
        elif proceed.lower() == "n": # "N" or "n" detected
            print("Abort")
            exit(0) # Close without error


# Start deploying project
print("Start deploying project")
# TODO: Maybe write a class and pass arguments there? Haven't decide how to write it.


