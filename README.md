# Vendor Performance Analysis

This repository offers an end-to-end solution for evaluating vendor performance using purchase, sales, and inventory data. It automates data ingestion into a SQLite database, computes essential vendor metrics, and generates clear visual reports, enabling data-driven decisions on supplier efficiency, profitability, and inventory management. With features like profitability analysis, inventory turnover, and vendor ranking, the system answers key business questions for comprehensive vendor evaluation.

---

## Project Structure

- **`ingestion_db.py`**: Automates loading CSV files into a SQLite database with logging support.
- **`get_vendor_summary.py`**: Generates vendor performance metrics by merging purchase, sales, and invoice data.
- **`vendor_performance_analysis.ipynb`**: Main analysis notebook for vendor rankings and visualizations.
- **`Exploratory_Data_Analysis.ipynb`**: Validates data schemas and performs initial profiling.
- **`ingestion_logging.ipynb`**: Tests and demonstrates the data ingestion pipeline.
- **`logs/`**: Stores runtime logs (auto-generated during execution).
- **`log_samples/`**: Contains example log files for reference.
- **`.gitignore`**: Excludes logs, databases, and non-source files from version control.

---

## Dataset

**Data Files:**

- **`begin_inventory.csv`**, **`end_inventory.csv`**: Store-level inventory snapshots  
- **`purchase_prices.csv`**: Vendor product pricing and volume information  
- **`vendor_invoice.csv`**: Invoice details including freight costs  
- **`purchases_sample.csv`** / **`purchases.csv`**: Purchase transaction records  
- **`sales_sample.csv`** / **`sales.csv`**: Sales transaction records  

*Due to large file sizes, only sample purchase and sales files are included in the repository.*

To use the complete dataset:

- Download **`purchases.csv`** and **`sales.csv`** from:  
  **[Insert your dataset download link here]**
- Place these files in the **`data/`** directory, replacing the sample files.

All other required data files are already provided.

---

## Setup Instructions

1. **Clone the repository:**
   
 ```bash
git clone https://github.com/yourusername/vendor-performance-analysis.git
cd vendor-performance-analysis
   ```

2. **Install dependencies:**
 ```bash
pip install pandas numpy matplotlib seaborn sqlalchemy scipy jupyter
   ```
3. **Add the full dataset:**  
Download **`purchases.csv`** and **`sales.csv`** as described above, and place them in the **`data/`** directory, replacing the sample files.

4. **Ingest data into the database:**

 ```bash
ingestion_db.py
   ```

5. **Generate the vendor summary:**
   
 ```bash
   get_vendor_summary.py

   ```
6. **Explore and analyze results:**  
Use the Jupyter notebooks for validation and analysis:
- **`Exploratory_Data_Analysis.ipynb`** for initial validation.
- **`vendor_performance_analysis.ipynb`** for detailed analysis and visualizations.

---

## Logging

- **logs/**: This folder is created automatically when running scripts. It stores all runtime logs (e.g., `ingestion_db.log`, `get_vendor_summary.log`).
- **log_samples/**: Contains sample log files for reference.

*Note: The main `logs/` folder will be populated only when running the code locally.*

---

## Analysis and Results

The analysis generated key vendor metrics such as *gross profit*, *profit margin*, *stock turnover*, and *sales-to-purchase ratio*, enabling clear comparisons across suppliers. Visualizations highlighted top-performing vendors, inventory efficiency, and the concentration of sales among a few major suppliers. New columns were engineered for deeper insights, supporting data-driven decisions to optimize procurement and inventory management.

---

## License

This repository is licensed under the MIT License.


