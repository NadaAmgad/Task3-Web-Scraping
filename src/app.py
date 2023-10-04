import subprocess

# Run the other script
subprocess.run(["python", "../Moviemeter_Scraping/scrap_moviemeter.py"])
subprocess.run(["python", "../IMDB_Scraping/scrap_imdb.py"])
subprocess.run(["python", "../Combined_Data/combined_data_analysis.py"])
subprocess.run(["python", "../Data_Analysis/app_analysis.py"])