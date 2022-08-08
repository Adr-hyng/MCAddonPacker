from os import listdir as getDir, walk as iterFile, remove as deleteFile, path
from zipfile import ZipFile
from pathlib import Path

class MinecraftAddonCompiler:
    
    """MinecraftAddonCompiler
    Description:
        - This automates the compressing of behavior pack or resource pack, or both by just running the main.py.
        
    Example: Both Behavior Pack and Resource Pack.
    ```py
    from Compiler import MinecraftAddonCompiler

    if __name__ == "__main__":
        addon = MinecraftAddonCompiler("Dev")
        addon.compileMCADDON()
    ```
    
    Example: Only Behavior Pack or Resource Pack.
    ```py
    from Compiler import MinecraftAddonCompiler

    if __name__ == "__main__":
        addon = MinecraftAddonCompiler("Dev")
    ```
"""
    
    def __init__(self, addonPack: str):
        self.addonPack = addonPack
        self.mcPacks = []
        self.compilePacks()
        
    def zipPacks(self, addonPack: str) -> str:
        zf = ZipFile(f"{addonPack}.zip", "w")
        for dirname, subdirs, files in iterFile(f"./{addonPack}"):
            zf.write(dirname)
            for filename in files:
                zf.write(path.join(dirname, filename))
        zf.close()
        p = Path(f"{addonPack}.zip")
        output = p.rename(p.with_suffix('.mcpack'))
        return output.__str__()


    # Packs the folders into mcpacks.
    def compilePacks(self) -> list[str]:
        for test in getDir("./"):
            for packName in ("BP", "RP"):
                if test.startswith(f"{self.addonPack}{packName}"):
                    addonPack = f"{self.addonPack}{packName}"
                    self.mcPacks.append(self.zipPacks(addonPack))
                    del addonPack

    # Compress the mcpacks into mcaddon.
    # Optional if user wants to compile BP and RP
    def compileMCADDON(self) -> None:
        if len(self.mcPacks) < 2: return
        zf = ZipFile(f"{self.addonPack} Addon.zip", "w")
        for dirname, subdirs, files in iterFile(f"./"):
            for mcpack in files:
                if mcpack in self.mcPacks:
                    zf.write(mcpack)
                    deleteFile(mcpack)
        zf.close()
        p = Path(f"{self.addonPack} Addon.zip")
        output = p.rename(p.with_suffix('.mcaddon'))
        print(f"{output.__str__()} is done compiling")
    
