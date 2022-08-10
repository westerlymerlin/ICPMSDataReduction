import os
import csv
import numpy
import zipfile
import time
from io import StringIO


def a_mean(x):
    return numpy.mean(x, axis=0).tolist()


def a_sterr(x):
    return (numpy.std(x, axis=0, ddof=1) / numpy.sqrt(numpy.size(x, axis=0))).tolist()


def getbatchfilelist(batchlogfile):
    print("Reading batch log: %s" %batchlogfile)
    with open(batchlogfile) as csvfile:
        filepath = os.path.dirname(batchlogfile)
        csv_data = csv.DictReader(csvfile, delimiter=',')
        batchfiles = []
        for row in csv_data:
            parsename = row['File Name'].split('\\')[len(row['File Name'].split('\\')) - 1]
            datafile = filepath + '\\' + parsename + '\\' + parsename[:-1] + 'csv'
            batchfiles.append([row['Sample Name'], datafile])
    csvfile.close()
    count_index = 0
    for filename in batchfiles:
        if [item[0] for item in batchfiles].count(filename[0]) > 1:
            batchfiles[count_index][0] = batchfiles[count_index][0] + '_1'
            print('Duplicate sample name in batchlog.csv - file name set to: %s' % filename[0])
        count_index += 1
    return batchfiles


def get_icpms_data(batchfile):
    icpms_files = getbatchfilelist(batchfile)
    print('Calculating mean and StdErr')
    arithmetic_means = []
    arithmetic_sterr = []
    filecounter = 0
    zipfilename = os.path.dirname(batchfile) + '\\he_reduction.zip'
    with zipfile.ZipFile(zipfilename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.close()
    for icpms_file in icpms_files:
        with open(icpms_file[1]) as csvfile:
            destfile = icpms_file[0] + '.csv'
            print('Writing: %s' % destfile)
            csvdata = csv.reader(csvfile, delimiter=',')
            icpms_data = []
            rowcounter = 0
            for row in csvdata:
                rowcounter += 1
                if rowcounter > 3:
                    icpms_data.append(row)
        csvfile.close()
        with zipfile.ZipFile(zipfilename, 'a', zipfile.ZIP_DEFLATED) as zip_file:
            string_buffer = StringIO()
            writer = csv.writer(string_buffer)
            writer.writerows(icpms_data[:-3])
            zip_file.writestr(destfile, string_buffer.getvalue())
        if filecounter == 0:
            arithmetic_means.append(icpms_data[0])
            arithmetic_means[0][0] = 'SampleID'
            arithmetic_sterr.append(icpms_data[0])
            arithmetic_sterr[0][0] = 'SampleID'
        am_row = a_mean(numpy.asarray(icpms_data[1:-3], dtype=float))
        as_row = a_sterr(numpy.asarray(icpms_data[1:-3], dtype=float))
        am_row[0] = icpms_file[0]
        as_row[0] = icpms_file[0]
        arithmetic_means.append(am_row)
        arithmetic_sterr.append(as_row)
        filecounter += 1
    with zipfile.ZipFile(zipfilename, 'a', zipfile.ZIP_DEFLATED) as zip_file:
        string_buffer = StringIO()
        writer = csv.writer(string_buffer)
        writer.writerows(arithmetic_means)
        print('Writing: arithmetic_means.csv')
        zip_file.writestr('arithmetic_means.csv', string_buffer.getvalue())
        string_buffer = StringIO()
        writer = csv.writer(string_buffer)
        writer.writerows(arithmetic_sterr)
        print('Writing: arithmetic_stderr.csv')
        zip_file.writestr('arithmetic_stderr.csv', string_buffer.getvalue())
        zip_file.close()
    print('\n\nICPMS Data Reduction Finished')
    print('%s files processed' %filecounter)
    print ('Zip file is located at: %s' % zipfilename)
    print('Processing time = %s seconds' % time.process_time())
    print('**** Script Finished ****')


if __name__ == '__main__':
    get_icpms_data('..\\..\\..\\..\\GTFiles\\Scratch Area\\20220713_Soln.b\\batchlog.csv')
