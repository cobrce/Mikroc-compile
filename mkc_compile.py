from settings import settings,compiler
import sys
import os
import configparser
from subprocess import Popen



def get_project_file(file_name:str) -> str:
    file_name = os.path.abspath(file_name)
    if file_name.endswith(".mcppi"):
        return file_name

    file_base,_ = os.path.splitext(os.path.basename(file_name))
    file_dir = os.path.dirname(file_name)    
    files = [file_ for file_ in os.listdir(file_dir) if file_.endswith(".mcppi")]
    if len(files):
        for file_ in files:
            if os.path.splitext(os.path.basename(file_))[0] ==  file_base:
                return os.path.join(file_dir,file_)
        return os.path.join(file_dir,files[0])
    else:
        raise FileNotFoundError(".mcppi")

def main(argc,argv):
    if (argc != 2):
        print("python3 mkc_compile.py <fileName>")
    else:
        file_name = argv[1]
        try:
            if os.path.exists(file_name):
                project_file = get_project_file(file_name)
                cfg = configparser.ConfigParser()
                cfg.read(project_file)
                try:
                    cmdln0 = settings["cmdln0"].format(
                        compiler = compiler,
                        filename =([value  for key,value in cfg["FILES"].items() if key.startswith("file")] or [None])[0] or os.path.basename(file_name),
                        device = cfg["DEVICE"]["Name"],
                        clock =  cfg["DEVICE"]["clock"][:-6],
                        project = project_file,
                    )

                    def format_path_dictionary(format:str,dictionary:dict)->str:
                        return " ".join([format.format(path = value) for key,value in dictionary.items() if key.startswith("path")])

                    cmdlnSP = format_path_dictionary(settings["cmdlnSP"],cfg["SEARCH_PATH"])
                    cmdlnIP = format_path_dictionary(settings["cmdlnIP"],cfg["HEADER_PATH"])
                    cmdln = " ".join((cmdln0,cmdlnSP,cmdlnIP,settings["cmdlnLIBS"]))
                    Popen(cmdln)
                except KeyError:
                    print("Key not found, invalid project file")
                except:
                    print("Some exception occured")
            else:
                raise FileNotFoundError("argv[1]")
        except FileNotFoundError as e:
            print(f"File not found : {e.args[0] or ''}")

if __name__=="__main__":
    main(len(sys.argv),[*sys.argv])