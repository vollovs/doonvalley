import os, calendar
class ProjectParser:
     
    def __init__(self):
        self.local_psf_path = '..\sql.txt'
         
         
    def load(self, file_path):
        print '#### 2015 basketball game schedule ####'
        self.file_buffer = []
        contents = []
        try:
            with open(file_path, "r") as file_handler:
                lines = file_handler.readlines()
                i = 1
                #j = 1
                for line in lines:
                    
                    contents.append(line.rstrip())
                    #print '[{0}]'.format(i)
                    if i % 8 == 0:
                        #print contents
                        self.file_buffer.append(contents)
                        contents = []
                    i += 1
                    
        except IOError:
            print 'File ' + self.config_file_path\
                   + ' does not exist, please create one.'
                    
    def parse_line(self, x, line):
        print 'parse line {0} -> {1}'.format(x, line)
         
    def print_all(self):
        #result = []
        i=1
        for content in self.file_buffer:
            #result.append('[{0:2d}] : {1} - {2} -{3:2s} ({4})\t {5}\n'.format(i, content[3], content[2],content[1], content[0], content[4]))
            print '[{0:2d}] : {1} - {2} -{3:2s} ({4})\t {5}'.format(i, content[3], content[2],content[1], content[0], content[4])
            i+=1
        #return result
    
    ## use the (Y-m-d) '20120101' or '2012-01-01' format.
    def print_sql(self):
        enum_month = dict((v.upper(),k) for k,v in enumerate(calendar.month_abbr))
        sql = 'INSERT INTO page_event(event_date,weekday, time_range) VALUES '
        
#         for k,v in enum_month.iteritems():
#             print k,v
        for content in self.file_buffer:
            sql += "('{0}-{1:02}-{2:02}', '{3}', '{4}'),\n".format(content[3], int(enum_month[content[2]]), int(content[1]), content[0], len(content[4]))
            
        return sql
    
    def write_file(self):
        #remove the old file before generate the new one
        if os.path.isfile(self.local_psf_path):
            os.remove(self.local_psf_path)
        try:
            with open(self.local_psf_path, "a") as file_handler:
                file_handler.writelines(self.print_all())
        except IOError:
            print 'File ' + self.config_file_path\
                   + ' does not exist, please create one.'
         
def run(file_name):
    parser = ProjectParser()
    parser.load(file_name)
    print parser.print_sql() 
    #parser.write_file()
    
     
if __name__=='__main__':
    #file_name = sys.argv[1]
    run('..\data.txt')