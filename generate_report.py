import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def analyze_data(file_path):
    """Reads CSV file and returns basic statistics"""
    data = pd.read_csv(file_path)
    stats = data.describe(include="all")
    return data, stats

def generate_pdf_report(data, stats, output_file="sample_report.pdf"):
    """Generates a PDF report with data insights"""
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 50, "Automated Data Report")

    # Dataset Preview
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, "📊 Dataset Preview (first 5 rows):")
    preview_text = data.head().to_string(index=False)
    text_object = c.beginText(50, height - 120)
    text_object.textLines(preview_text)
    c.drawText(text_object)

    # Statistics
    c.drawString(50, height - 250, "📈 Summary Statistics:")
    stats_text = stats.to_string()
    text_object = c.beginText(50, height - 270)
    text_object.textLines(stats_text)
    c.drawText(text_object)

    c.save()
    print(f"Report saved as {output_file}")

if __name__ == "__main__":
    # Input file
    file_path = "data_sample.csv"

    # Read & analyze
    data, stats = analyze_data(file_path)

    # Generate report
    generate_pdf_report(data, stats)
