import csv
from keboola import docker


class SampleApplication:
    def run(self):
        # initialize the application and read parameter 'multiplier'
        cfg = docker.Config()
        multiplier = cfg.get_parameters()['multiplier']

        # open the input and output files
        with open('in/tables/source.csv', mode='rt', encoding='utf-8') as in_file, open('out/tables/destination.csv', mode='wt', encoding='utf-8') as out_file:
            # write output file header
            writer = csv.DictWriter(out_file, fieldnames=['number', 'someText', 'double_number'], dialect='kbc')
            writer.writeheader()

            # read input file line-by-line
            lazy_lines = (line.replace('\0', '') for line in in_file)
            csv_reader = csv.DictReader(lazy_lines, dialect='kbc')
            for row in csv_reader:
                # do something and write row
                writer.writerow({'number': row['number'], 'someText': row['someText'], 'double_number': int(row['number']) * multiplier})
