from setuptools import find_packages, setup
from typing import List

def get_requirements () -> List[str]:
    """
    Return list of requirements 
    """
    requirement_list : List[str] = []
    try : 
        #Open and read requirements file 
        with open("requirements.txt", "r") as reqs :
            lines = reqs.readlines()
            for line in lines : 
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print ("requirements.txt file not found.")
    
    return requirement_list

print (get_requirements) 
setup(
    name = "AI-TRAVEL-PLANNER",
    version = "0.0.1",
    author = "Hamza Hajjini",
    author_email = "hajjinihamza2@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)




