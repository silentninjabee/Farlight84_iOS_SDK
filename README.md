# Farlight84 iOS SDK

The Farlight 84 iOS SDK is a comprehensive package designed for the game built on the Unreal Engine v4.25 for Apple iOS ARM-64 platform. 
This SDK provides critical tools and resources tailored for developers working with Farlight84 on iOS devices.

## Global Offsets (as of 18th September 2024)
**Apple iOS ARM64 - Farlight 84 Global Offsets**

```cpp
/* 
iOS current version globals as of 30 September 2024

*/

iOS current version globals

const long GWORLD = 0x10839C1F8;
const long FNAMEPOOL = 0x10818ca00;
const long GUOBJECTARRAY = 0x108322e20;


```

## Key Features

### IDA/Ghidra Function Naming Python Script
Included in this SDK is a Python script that enhances the decompilation and analysis of the games executable in Ghidra or IDA Pro. These python scripts leverage the `scripts.json` file included in the zipped package, simplifying the importing of function names and addresses into IDA or Ghidra, greatly streamlining your analysis efforts.

ghidra_funcs.py = support all current versions of Ghidra

ida_funcs.py = IDA v7.2 and lower (python2 script)

ida_funcs_python3.py = IDA v7.2+ (python3 script)

#### Visual Guide to Importing UFunctions Using `ida_funcs.py`
- **Before Importing the Included JSON**
  - ![Before Loading Dump Script](https://github.com/silentninjabee/Farlight84_iOS_SDK/blob/main/farlight_IdaBeforeFunctionsImport.jpg)
- **After Importing the Included JSON**
  - ![After Loading Dump Script](https://github.com/silentninjabee/Farlight84_iOS_SDK/blob/main/farlight_IdaAfterFunctionsImport.jpg)

## ZIP File Contents

### Headers [folder]
Contains C++ headers Group by UE Reflection System Types, split into seperate .h files for Enums, Classes, and Structs. Note: These headers may require modifications to compile successfully.

- `AIOHeader.hpp`: An all-in-one header file encapsulating the entire dump.

### Log Files
- `logs.txt`: Log file containing details of the dump process and global offset information.

### Object Dumps
- `ObjectsDump.txt`: Dump of ObjObjects.

### JSON Script
- `script.json`: This file contains a JSON array detailing UFunction's that get called by the game logic typically marked as "Exec", there names and inheritance, and addresses. This is for importing this usefull infomation into IDA Pro, or Ghidra for static analysis of the games executable Macho file.

## Dumping Method
The dump included in this SDK was generated using a modified version of the iOS_UE4Dumper. For more information and access to the tool, visit:
[GitHub - iOS_UE4Dumper](https://github.com/MJx0/iOS_UE4Dumper)

## Additional Resources
For SDK information pertaining to Steam and Windows platforms, please visit:
[GitHub - Farlight84 SDK for Steam and Windows](https://github.com/Fer3on07/Farlight84-SDK)


```
                    __      __        __     =--------=    __        __        __                     
                   /_/\    /_/\      /\_\                 /_/\      /\_\      /\_\                    
                   ) ) )   ) ) )    / ( (                 ) ) \    ( ( (     ( ( (                    
                  /_/ /   /_/ /    /   \_\               /_/   \    \ \_\     \ \_\                   
 _    _    _      ) ) )   ) ) )    \   / /               \ \   /    ( ( (     ( ( (     _    _    _   
/_/\ /_/\ /_/\   / / /   / / /      \ (_(                 )_) /      \ \ \     \ \ \   /_/\ /_/\ /_/\ 
\_\/ \_\/ \_\/   \/_/    \/_/        \/_/                 \_\/        \_\/      \_\/   \_\/ \_\/ \_\/ 
```                                                                                                   


### Update Log*: 
 {dd/mm/yyyy}:
- 30/09/2024 Minor update to the global offsets, the SDK appears to be the same.
- 16/09/2024 Major game update to "HiBUddy". Updated global offsets and new dump zip file.
  * Included new Farlight.hpp GameProfile for [GitHub - iOS_UE4Dumper](https://github.com/MJx0/iOS_UE4Dumper)
- 26/07/2024: Major game update. Updated global offsets and new dump zip file.
- 07/07/2024: Major game update v2.3.4 - Updated global offsets and new dump zip file.
- 17/05/2024: Minor update v.2.2.1.
- 24/04/2024: Major game update v.2.2.o. Updated global offsets and new dump zip file.
- 08/02/2024: Minor game update v.2.0.1. Updated global offsets and new dump zip file.
- 26/01/2024: Major game Update to v2.0.0.Updated global offsets and new dump zip file.
- 29/12/2023: Update new season. v15.1.9 update.
- 02/12/2023: Update new season. v15.6.2 update.
- 10/11/2023: Major game Updated. v15.2.1 Updated global offsets and new dump zip file.
- 27/09/2023: New Season Game Update. v14.4.8. Updated global offsets and new dump zip file.
- 03/09/2023: Updated global offsets and new dump zip file.
- 01/09/2023: Updated global offsets and new dump zip file.
- 27/08/2023: Updated global offsets and new dump zip file. Included python IDA script "ida_funcs_python3.py" for IDA > v7.0 (python3) 
- 15/08/2023: Included python IDA script "ida_funcs.py" to import the script.json function symbols into IDA < v7.0 (python2)
- 27/7/2023: Major game update. Team information has been moved into a new class.
- 16/6/2023: A New Version for iOS is being pushed out with an Update to the Global Offsets
- 03/6/2023: Fixed the ida_funcs.py script. Confirmed working with "IDA - The Interactive Disassembler (Version 7.0.170914 macOSx86_64)"
