import pandas as pd

brown_dwarf_data = pd.read_csv('brown_dwarf_stars.csv')

brown_dwarf_data.dropna(inplace=True)

brown_dwarf_data['Mass'] = brown_dwarf_data['Mass'].astype(float)
brown_dwarf_data['Radius'] = brown_dwarf_data['Radius'].astype(float)

brown_dwarf_data['Radius'] = brown_dwarf_data['Radius'] * 0.102763

brown_dwarf_data['Mass'] = brown_dwarf_data['Mass'] * 0.000954588

brown_dwarf_data.to_csv('cleaned_brown_dwarf_stars.csv', index=False)

brightest_stars_data = pd.read_csv('brightest_stars.csv')

merged_data = pd.merge(brown_dwarf_data, brightest_stars_data, how='inner')

merged_data.to_csv('merged_stars.csv', index=False)
