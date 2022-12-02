import PyPDF2
import glob
import datetime

merger = PyPDF2.PdfFileMerger()

files = sorted(glob.glob("combine/*.pdf"))
for file in files:
    merger.append(file)

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)

merger.write('combine/combine_' + now.strftime('%Y%m%d%H%M%S') + '.pdf')
merger.close()
