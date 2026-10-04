import pandas as pd
import glob

path = "../csv/"

# sold data

sold_files = sorted(glob.glob(path + "CRMLSSold*.csv"))
sold_dfs = [pd.read_csv(file) for file in sold_files]

# Before concatenation: 615,707 rows
sold_rows_before = sum(len(df) for df in sold_dfs)
print("Sold rows before concatenation:", sold_rows_before)

sold = pd.concat(sold_dfs, ignore_index=True)

# After concatenation: 615,707 rows
print("Sold rows after concatenation:", len(sold))

# Before Residential filter: 615,707 rows
print("Sold rows before Residential filter:", len(sold))

sold = sold[sold["PropertyType"] == "Residential"]

# After Residential filter: 414,054 rows
print("Sold rows after Residential filter:", len(sold))

sold.to_csv(path + "combined_sold.csv", index=False)


# listing data

listing_files = sorted(glob.glob(path + "CRMLSListing*.csv"))
listing_dfs = [pd.read_csv(file) for file in listing_files]

# Before concatenation: 860,898 rows
listing_rows_before = sum(len(df) for df in listing_dfs)
print("Listing rows before concatenation:", listing_rows_before)

listings = pd.concat(listing_dfs, ignore_index=True)

# After concatenation: 860,898 rows
print("Listing rows after concatenation:", len(listings))

# Before Residential filter: 860,898 rows
print("Listing rows before Residential filter:", len(listings))

listings = listings[listings["PropertyType"] == "Residential"]

# After Residential filter: 547,162 rows
print("Listing rows after Residential filter:", len(listings))

listings.to_csv(path + "combined_listings.csv", index=False)