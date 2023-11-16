<div align="center">

# Fleet Fingers - A simple tool to help you practice difficult key combinations for faster typing.

#### 🔧 Made with:
![](https://img.shields.io/badge/-Python-informational?style=flat&logo=Python&logoColor=white)


[Motivation](#motivation) 
•
[Explanation](#explanation)
•
[Installation and Usage](#installationandusage)

</div>

## Motivation

Touch typing is a method of typing without the need to look at the keyboard. This skill involves memorizing the keyboard layout and using muscle memory to type quickly and accurately. In touch typing, each finger is generally responsible for a specific group of keys, allowing for efficient and speedy typing. The main benefits of touch typing include increased typing speed, improved accuracy, and the ability to maintain focus on the screen or on the content being typed, rather than on finding keys on the keyboard. This method is particularly useful for tasks that involve a lot of typing, such as writing, programming, and data entry.

However, there are no websites that allow for this flexibility in terms of personalized learning. Because of that, this small project attempts to do just that: personalize your typing practice based on the key combinations that you find hardest to type correctly.

Many beginners who are new to touch typing will find themselves struggling to use the correct fingers to press the right keys. This is probably most obvious with the `b` key located in the center of the keyboard. Most people will type the letter `b` using the right hand, as it is intuitively much easier, especially for right-handed typists. However, in touch typing, the letter `b` should be pressed with the left index finger to maximize efficiency. 

There is also the case of key combinations. A personal example of mine would be the letters 'nu' or 'be'. Such combinations can be tricky to learn, especially after years of typing them with the wrong fingers. This is because your brain must get used to learning these new combinations while suppressing the old ones that were stuck in your head for years.

## Explanation

By default, Fleet Fingers loops over all the top 10,000 English words and retrieves the ones with a given key combination from the user. For example, if you struggle to type the letters 'be' after each other with the right fingers, you can input this to Fleet Fingers, which will then find all words containing 'be' in the top 10,000 English words (e.g., Belgium, because, etc.). Fleet Fingers accepts any text file as input, so if you would like to practice another language or have more words at your disposal, you are able to upload your own text file!

Optionally, you can also add special characters at the end of the words in case you would like to practice these keys as well. 

I used this tool in conjunction with 10fastfingers.com and Keybr, to achieve close to 110 wpm.

## Installation and Usage

Run `weak_combinations.py` and enter all the weak combinations that you would like to practice, separated by a `space`. The script will then generate a new text file in the `files` directory, containing all the words in the top 10,000 English words that contain the letter combination that you specified. Now, you can copy all these words and paste them in online tools such as Keybr, Monkeytype, etc. to practice typing them and retrieve stats about your performance.


