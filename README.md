# Farlight84 iOS SDK
Farlight 84 iOS SDK is a comprehensive dump of the Unreal Engine v4.25 game, specifically designed for Apple iOS ARM 64-bit.

#### Global Offsets as of 29 December 2023 v15.1.9
```
Apple iOS Arm64 - Farlight 84 global offsets
Farlight 84 - Version 15.1.9
==========================
    #define GWORLD 0x107C43908
    #define NAMEPOOL 0x1079C9600
    #define GENGINE 0x107C42160

```

# Key Features:
## 'ida_funcs.py' Python Script: This SDK includes 'ida_funcs.py,' a Python script that facilitates the analysis of the SolarlandClient
executable in IDA. By utilizing the scripts.json file, this script imports function names and addresses into IDA, streamlining the
analysis process.

##### Before the Import of included Json
![Alt text](https://github.com/silentninjabee/Farlight84_iOS_SDK/blob/main/farlight_IdaBeforeFunctionsImport.jpg "Before Import Json Functions")

##### After the Import of included Json
![Alt text](https://github.com/silentninjabee/Farlight84_iOS_SDK/blob/main/farlight_IdaAfterFunctionsImport.jpg "After Import Json Functions")

# ZIP File Contents

### headers_dump
C++ headers that you can use in your source, however, the headers might not compile directly without a change

### FullDump.hpp
An all-in-one dump file

### logs.txt
Logfile containing dump process logs

### objects_dump.txt
ObjObjects dump

### script.json
If you are familiar with Il2cppDumper script.json, this is similar
It contains a json array of function names and addresses

## Dumping Method:
The provided dump was created using a modified version of the iOS_UE4Dumper available at https://github.com/MJx0/iOS_UE4Dumper

## For Steam and Windows Offsets check out: https://github.com/Fer3on07/Farlight84-SDK

# Update Log:
- 29/12/2023: Update new season. v15.1.9 update.
- 02/12/2023: Update new season. v15.6.2 update.
- 10/11/2023: Major game Updated. v15.2.1 Update Global Offsets, 
- 27/09/2023: New Season Game Update. v14.4.8. Update to Global Offsets and some minor offsets
- 03/09/2023: Update to Global Offsets. New dump with the latest uploaded, teamID offset changed
- 01/09/2023: Update to Global Offsets. New dump with the latest uploaded.
- 27/08/2023: Update to Global Offsets. New Major game update. majority of internal offsets are the same. Updated new global offsets.
- 15/08/2023: Included python IDA scri[t to import the script.json symbols for IDA v7.7 (python3)
- 27/7/2023: Major game update. Team information has been moved into a new class.
- 16/6/2023: New Version for iOS is being pushed out with Update to the Global Offsets
- 03/6/2023: Fixed the ida_funcs.py script. Confirmed working with "IDA - The Interactive Disassembler (Version 7.0.170914 macOSx86_64)"
