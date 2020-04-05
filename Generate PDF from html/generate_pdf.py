#importing  library
import pdfkit

#path set (windows OS)
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

#using pdfkit configuration
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

#html to pdf conversion
pdfkit.from_url("invoice.html", "invoice.pdf", configuration=config)