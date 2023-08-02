# Farlight84 iOS SDK
Farlight 84 iOS SDK is a comprehensive dump of the Unreal Engine v4.25 game, specifically designed for Apple iOS ARM 64-bit.

#### Global Offsets as of 27th July 2023 

    UObjects = 0x724EAC8
    GWorld - 0x72D8908
    FNamePool = 0x6FB1300


## Key Features:
**'ida_funcs.py'** Python Script: This SDK includes 'ida_funcs.py,' a Python script that facilitates the analysis of the SolarlandClient
executable in IDA. By utilizing the scripts.json file, this script imports function names and addresses into IDA, streamlining the
analysis process.

##### Before the Import of included Json
![Alt text](https://github.com/silentninjabee/Farlight84_iOS_SDK/blob/main/farlight_IdaBeforeFunctionsImport.jpg "Before Import Json Functions")

##### After the Import of included Json
![Alt text](https://github.com/silentninjabee/Farlight84_iOS_SDK/blob/main/farlight_IdaAfterFunctionsImport.jpg "After Import Json Functions")


## Dumping Method:
The provided dump was created using a modified version of the iOS_UE4Dumper available at https://github.com/MJx0/iOS_UE4Dumper.

## Update Log:
- 27/7/2023: Major game update. Team information has been moved into a new class.

- 16/6/2023: New Version for iOS is being pushed out with Update to the Global Offsets

- 03/6/2023: Fixed the ida_funcs.py script. Confirmed working with "IDA - The Interactive Disassembler (Version 7.0.170914        
macOSx86_64)"
