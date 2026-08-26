# Data Schema - vgsales

## Overview
This project uses the `vgsales.xlsx` dataset as the source file and `vgsalesclean.xlsx` as the cleaned output file.

The cleaning workflow does the following:
- removes rows with missing values
- converts `Year` to an integer type
- normalizes sales-related numeric values
- sorts the dataset by `Global_Sales` in descending order

## Data Schema

### Before and After Comparison

| Column | vgsales.xlsx (Original) | vgsalesclean.xlsx (Cleaned) | Notes |
|---|---|---|---|
| `Rank` | Numeric-like value | Numeric value | Kept as rank information |
| `Name` | Text | Text | Game title |
| `Platform` | Text | Text | Platform name |
| `Year` | Numeric-like value, sometimes shown with decimal formatting | Integer | Converted to `int` |
| `Genre` | Text | Text | Game genre |
| `Publisher` | Text | Text | Publisher name |
| `NA_Sales` | Numeric-like value | Numeric value | North America sales |
| `EU_Sales` | Numeric-like value | Numeric value | Europe sales |
| `JP_Sales` | Numeric-like value | Numeric value | Japan sales |
| `Other_Sales` | Numeric-like value | Numeric value | Other region sales |
| `Global_Sales` | Numeric-like value | Numeric value | Used for sorting in descending order |

### Schema Summary
- Original file: `vgsales.xlsx`
- Cleaned file: `vgsalesclean.xlsx`
- Main structural change: `Year` is converted to integer and sales values are normalized for consistent numeric handling
- Row order in the cleaned file: sorted by `Global_Sales` from highest to lowest

## Cleaning Details

The cleaned file was prepared with the following steps:
- load the original dataset from `vgsales.xlsx`
- remove empty rows
- convert `Year` to integer
- normalize the sales columns so they are treated as numeric data
- sort the dataset by `Global_Sales` in descending order
- export the result to `vgsalesclean.xlsx`

## Clean File Statistics

| Metric | Value |
|---|---|
| Data rows | 16,327 |
| Columns | 11 |
| Year range | 1980 to 2020 |
| Missing values | 0 |
| Sort order | `Global_Sales` descending |

## Distribution Review

### Top Platforms

| Platform | Count |
|---|---:|
| DS | 2,133 |
| PS2 | 2,127 |
| PS3 | 1,304 |
| Wii | 1,290 |
| X360 | 1,235 |

### Top Genres

| Genre | Count |
|---|---:|
| Action | 3,253 |
| Sports | 2,304 |
| Misc | 1,710 |
| Role-Playing | 1,471 |
| Shooter | 1,282 |

### Top Publishers

| Publisher | Count |
|---|---:|
| Electronic Arts | 1,339 |
| Activision | 966 |
| Namco Bandai Games | 928 |
| Ubisoft | 918 |
| Konami Digital Entertainment | 823 |

## Sample Preview

The first rows in the cleaned file can be used as a quick review of the stored content:

| Rank | Name | Platform | Year | Genre | Publisher |
|---|---|---|---:|---|---|
| 196 | Guitar Hero II | PS2 | 2006 | Misc | RedOctane |
| 195 | Microsoft Flight Simulator | PC | 1996 | Simulation | Microsoft Game Studios |
| 282 | Half-Life | PC | 1997 | Shooter | Vivendi Games |
| 283 | Super Mario World 2: Yoshi's Island | SNES | 1995 | Platform | Nintendo |
| 447 | Dragon Warrior IV | NES | 1990 | Role-Playing | Enix Corporation |

## Usage

To reproduce the cleaned dataset:
1. Place `vgsales.xlsx` in the same folder as `Weebforce.ipynb`.
2. Run the notebook cell that loads and cleans the data.
3. The notebook will create `vgsalesclean.xlsx` in the same directory.
4. Open the output file to review the cleaned and sorted dataset.

## Processing Pipeline

| Step | Action | Result |
|---|---|---|
| 1 | Read the original file | Load `vgsales.xlsx` into pandas |
| 2 | Normalize numeric columns | Convert sales columns to numeric values |
| 3 | Clean the year field | Convert `Year` to integer |
| 4 | Remove invalid rows | Drop rows with missing data |
| 5 | Sort the dataset | Order rows by `Global_Sales` descending |
| 6 | Export the result | Write the cleaned data to `vgsalesclean.xlsx` |

## Notes

- `vgsales.xlsx` is the original source dataset.
- `vgsalesclean.xlsx` is the cleaned version after processing.
- The notebook displays numeric columns aligned to the right and text columns aligned to the left.
- The cleaned file keeps the same column structure as the original file.
- The main visible change is consistent numeric handling and sorted row order.
