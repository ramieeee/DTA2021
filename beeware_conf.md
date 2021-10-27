[toc]



**This is a tutorial steps shown by beeware.

The original tutorials could be cound at : https://docs.beeware.org/en/latest/tutorial/tutorial-0.html

# Beeware configuration

# 1. Computer

## 1) pre-setting

```
# virtual env setting

C:\...>md beeware-tutorial
C:\...>cd beeware-tutorial
C:\...>py -m venv beeware-venv
C:\...>beeware-venv\Scripts\activate.bat
```

```
(beeware-venv)C:\...>python -m pip install briefcase
(beeware-venv) C:\...>briefcase new

Formal Name
App Name
Bundle
Project Name
Description
Autho
Author's email
URL
License
GUI framework - default is Toga
```

```
# to run in developer mode
(beeware-venv) C:\...>cd helloworld
(beeware-venv) C:\...>briefcase dev
```



## 2). Packaging

```
(beeware-venv) C:\...>briefcase create

[helloworld] Generating application template...
Using app template: https://github.com/beeware/briefcase-windows-msi-template.git
...
[helloworld] Installing support package...
...
[helloworld] Installing dependencies...
...
[helloworld] Installing application code...
...
[helloworld] Installing application resources...
...
[helloworld] Created windows\Hello World
```



```
(beeware-venv) C:\...>briefcase create android

[helloworld] Generating application template...
Using app template: https://github.com/beeware/briefcase-android-gradle-template.git
...
[helloworld] Installing support package...
...
[helloworld] Installing dependencies...
...
[helloworld] Installing application code...
...
[helloworld] Installing application resources...
...
[helloworld] Application created.
```

## 3). Building application

* Compiling. Binary compilation to be run in the targeted platform

```
(beeware-venv) C:\...>briefcase build

[helloworld] Built windows\Hello World
```

```
(beeware-venv) C:\...>briefcase build android
[helloworld] Building Android APK...
Starting a Gradle Daemon
...
BUILD SUCCESSFUL in 1m 1s
28 actionable tasks: 17 executed, 11 up-to-date
[helloworld] Built android\Hello World\app\build\outputs\apk\debug\app-debug.apk
```



## 4). Building installer

```
(beeware-venv) C:\...>briefcase package

[helloworld] Building MSI...
...
[helloworld] Created windows\Hello_World-0.0.1.msi
```



## 5). Update

```
# when code is changed
(beeware-venv) C:\...>briefcase update

[helloworld] Updating application code...
Installing src/helloworld...

[helloworld] Application updated.

# or run and update in one step

(beeware-venv) C:\...>briefcase run -u

[helloworld] Updating application code...
Installing src/helloworld...

[helloworld] Application updated.

[helloworld] Starting app...
```



# 2. Android

## 1) pre-setting

```
# virtual env setting

C:\...>md beeware-tutorial
C:\...>cd beeware-tutorial
C:\...>py -m venv beeware-venv
C:\...>beeware-venv\Scripts\activate.bat
```

```
(beeware-venv)C:\...>python -m pip install briefcase
(beeware-venv) C:\...>briefcase new

Formal Name
App Name
Bundle
Project Name
Description
Autho
Author's email
URL
License
GUI framework - default is Toga
```

```
# to run in developer mode
(beeware-venv) C:\...>cd helloworld
(beeware-venv) C:\...>briefcase dev
```



## 2). Packaging

```
(beeware-venv) C:\...>briefcase create android

[helloworld] Generating application template...
Using app template: https://github.com/beeware/briefcase-android-gradle-template.git
...
[helloworld] Installing support package...
...
[helloworld] Installing dependencies...
...
[helloworld] Installing application code...
...
[helloworld] Installing application resources...
...
[helloworld] Application created.
```



## 3). Building application

* Compiling. Binary compilation to be run in the targeted platform

```
(beeware-venv) C:\...>briefcase build android
[helloworld] Building Android APK...
Starting a Gradle Daemon
...
BUILD SUCCESSFUL in 1m 1s
28 actionable tasks: 17 executed, 11 up-to-date
[helloworld] Built android\Hello World\app\build\outputs\apk\debug\app-debug.apk
```



## 4). Run app on virtual device

```
(beeware-venv) C:\...>briefcase run android

Select device:

  1) Create a new Android emulator

>
```



## 5). Update

```
# when code is changed
(beeware-venv) C:\...>briefcase update

[helloworld] Updating application code...
Installing src/helloworld...

[helloworld] Application updated.

# or run and update in one step

(beeware-venv) C:\...>briefcase run -u

[helloworld] Updating application code...
Installing src/helloworld...

[helloworld] Application updated.

[helloworld] Starting app...


# then rebuild the app

(beeware-venv)C:\...>briefcase build

# and run the app

(beeware-venv)C:\...>briefcase run
```

## 6). Updating dependencies

* pyproject.toml indicates information as below

```
[tool.briefcase.app.hello-world]
formal_name = "Hello World"
description = "A Tutorial app"
icon = "src/hello_world/resources/hello-world"
sources = ['src/hello_world']

# requires is the section where library list is contained.
requires = [
    "httpx", "pandas"
]
```

- A specific library version (e.g., `"httpx==0.19.0"`);
- A range of library versions (e.g., `"httpx>=0.19"`);
- A path to a git repository (e.g., `"git+https://github.com/encode/httpx"`); or
- A local file path (However - be warned: if you give your code to someone else, this path probably won’t exist on their machine!)

