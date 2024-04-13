![](https://github.com/JerryBerry12/futurehacks-2024-trashomatic/blob/main/images/PNGs/logo-500x500.png)
# futurehacks-2024-trashomatic
My project for futurehacks-2024. Ai model that can detect whether an object is compost, bottles/cans, paper, trash, plastic.
# Get Started
`pip install -r requirements.txt`
`python3 main_gui.py`
# To Train
`python3 train_gui.py`
# To Mass Import Training data
<details>
<summary><b>CSV Formatting</b></summary>
  
__CSV must be formatted as follows: (No header data)__
```
nameoftrash,numberofcategory
nameoftrash,numberofcategory
nameoftrash,numberofcategory
etc...
```
Categories:
| Number | 1    | 2    | 3   | 4   | 5   |
| :---:   | :---: | :---: | :---: | :---: | :---: |
| Category | compost   | bottles/cans   | paper | trash | plastic |
</details>

`python csv_reader_gui.py`
<br>

Tell it the full path to your csv file, and it should auto import everything.
It'll let you know if the file is misformatted.
You may have to delete the `ai_data.sqlite3` file if it gets corrupt or with the wrong data.
