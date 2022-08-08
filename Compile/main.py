from Compiler import MinecraftAddonCompiler

"""
!Warning:
- Must provide exact word to match, in order to pack the addon.
 
Example:
- Addon Name: "Forest Axe"
- Behavior Pack Name: "ForestAxe BP"
- returns -> None 

MUST:
- Addon Name: "ForestAxe"
- Behavior Pack Name: "ForestAxe BP"
- Resource Pack Name: "ForestAxe RP"
- returns -> compressed mcpacked addon (.mcaddon).
"""

if __name__ == "__main__":
    addon = MinecraftAddonCompiler("Test ")
    addon.compileMCADDON()