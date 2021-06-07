# Tech Challenge for Team 2 :

## Fix CSV Encoding

### Solution :

- User uploads the corrupted CSV file (sample corrupted csv added in the repository 'testCSV-corrupted.csv')
- Reading the corrupted (improper emoji encryption) CSV file.
- Fixing the encoding of the CSV file to allow the emojis to be inerpreted correctly.
- The encoding which supports the new unicode emojis was found to be 'utf-8-sig' and the same encryption was applied to the CSV file and displayed on the UI.
- User can now download the fixed CSV file and view the emojis correctly even inside MS Excel.

### Steps to run the code :

- Run `pip install streamlit`
- Move to the working directory
- Run `streamlit run app.py`
- The UI opens up in the browser
- Follow the steps in the solution
