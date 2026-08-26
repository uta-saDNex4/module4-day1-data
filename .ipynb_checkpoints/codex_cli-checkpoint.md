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
