# MC Bedrock Addon Packer
Minecraft Bedrock Addon Packer to easily make or test a template or production addon.
Created by Adr-hyng

# Why is this created?

It's not the most useful thing in the world. It packs your production or template folder addon into a `.mcpack` or `.mcaddon` format, so you can use it inside the minecraft bedrock or pocket edition for development or production. Example of this repo is a template addon.

![image](https://user-images.githubusercontent.com/95139246/183453113-c6f3e990-578e-43c1-8c19-18abe03729b3.png)



# How to use

![image](https://user-images.githubusercontent.com/95139246/183453235-fa4ad69a-27b1-462b-a252-4b4e8d0b7890.png)

Example:

![image](https://user-images.githubusercontent.com/95139246/183454060-d4cf5ea4-2000-4680-8558-eddbe70581bd.png)

![image](https://user-images.githubusercontent.com/95139246/183454175-7bfa2e1f-145f-4fd7-a538-2f8691cb1e4e.png)


To use, you need Python, required packages are already built-in inside python. 
To start, download or clone this repo, then, run the `main.py` python file on this directory you've downloaded or cloned by using your Python IDE or Compiler. After running, there will be a `.mcaddon` which was compiled by this program. Namely `Test Addon.mcaddon`. There you can put your behavior pack folder or resource pack folder to that directory to automatically pack stuffs for you.

# Things to Do

- use fuzzy string matching (fuzzywuzzy) or NLP to accurately check your precise behavior and resource pack folder name.
- have CLI for beginner-friendly users, and to not use any IDE or Compiler for other user or me.
