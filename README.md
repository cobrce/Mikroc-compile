# Mikroc-compile
A script that helps using Mikroc command line, aimed to be used with VS Code + Code Runner

## How to use

### Config
open settings.py and adjust "compiler" variable to point to mikroCPIC1618.exe (absolute path)

add to "cmdlnLIBS" the libraries you want to be used

### Standalone execution
execute the following

`python3 mkc_compile.py <program_to_be_compiled>`

you can use either absolute path or relative (should execute from the same directory)

### With VS Code
Install [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)

in File -> Preferences -> Settings -> USER SETTINGS add this
```
"code-runner.executorMap": {
        "c":"cd $dir && python3 \"<mkc_compile.py>\" $fileName",
    }
```

<mkc_compile.py> to be replaced by the absolute path of mkc_compile.py

Back to your program's tab then CTRL+ALT+N

