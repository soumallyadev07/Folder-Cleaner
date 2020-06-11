from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil
from datetime import datetime
from time import gmtime, strftime


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'Sorted':
                # try:
                new_name = filename
                extension = 'noname'
                try:
                    extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                    path = extensions_folders[extension]
                except Exception:
                    extension = 'noname'

                now = datetime.now()
                year = now.strftime("%Y")
                month = now.strftime("%m")

                folder_destination_path = extensions_folders[extension]

                year_exists = False
                month_exists = False
                for folder_name in os.listdir(extensions_folders[extension]):
                    if folder_name == year:
                        folder_destination_path = extensions_folders[extension] + "/" + year
                        year_exists = True
                        for folder_month in os.listdir(folder_destination_path):
                            if month == folder_month:
                                folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                month_exists = True
                if not year_exists:
                    os.mkdir(extensions_folders[extension] + "/" + year)
                    folder_destination_path = extensions_folders[extension] + "/" + year
                if not month_exists:
                    os.mkdir(folder_destination_path + "/" + month)
                    folder_destination_path = folder_destination_path + "/" + month

                file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                while file_exists:
                    i += 1
                    new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + \
                               os.path.splitext(folder_to_track + '/' + filename)[1]
                    new_name = new_name.split("/")[4]
                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                src = folder_to_track + "/" + filename

                new_name = folder_destination_path + "/" + new_name
                os.rename(src, new_name)
            # except Exception:
            #     print(filename)
            # Add the folder path & also create all the folders


extensions_folders = {
    # No name
    'noname': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Uncategorized",
    # Audio
    '.aif': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Audio",
    '.cda': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Audio",
    '.mid': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Audio",
    '.midi': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Audio",
    '.mp3': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Audio",
    '.mpa': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Audio",
    '.ogg': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Audio",
    '.wav': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Audio",
    '.wma': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Audio",
    '.wpl': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Audio",
    '.m3u': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Audio",
    # Text
    '.txt': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/TextFiles",
    '.doc': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/Microsoft/Word",
    '.docx': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/Microsoft/Word",
    '.odt ': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/TextFiles",
    '.pdf': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/PDF",
    '.rtf': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/TextFiles",
    '.tex': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/TextFiles",
    '.wks ': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/TextFiles",
    '.wps': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/TextFiles",
    '.wpd': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/TextFiles",
    # Video
    '.3g2': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Video",
    '.3gp': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Video",
    '.avi': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Video",
    '.flv': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Video",
    '.h264': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Video",
    '.m4v': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Video",
    '.mkv': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Video",
    '.mov': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Video",
    '.mp4': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Video",
    '.mpg': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Video",
    '.mpeg': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Video",
    '.rm': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Video",
    '.swf': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Video",
    '.vob': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Video",
    '.wmv': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Video",
    # Images
    '.ai': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Images",
    '.bmp': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Images",
    '.gif': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Images",
    '.ico': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Images",
    '.jpg': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Images",
    '.jpeg': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Images",
    '.png': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Images",
    '.ps': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Images",
    '.psd': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Images",
    '.svg': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Images",
    '.tif': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Images",
    '.tiff': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Images",
    '.CR2': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Images",
    # Internet
    '.asp': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Internet",
    '.aspx': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Internet",
    '.cer': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Internet",
    '.cfm': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Internet",
    '.cgi': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Internet",
    '.pl': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Internet",
    '.css': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Internet",
    '.htm': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Internet",
    '.js': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Internet",
    '.jsp': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Internet",
    '.part': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Internet",
    '.php': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Internet",
    '.rss': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Internet",
    '.xhtml': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Internet",
    # Compressed
    '.7z': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Compressed",
    '.arj': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Compressed",
    '.deb': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Compressed",
    '.pkg': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Compressed",
    '.rar': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Compressed",
    '.rpm': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Compressed",
    '.tar.gz': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Compressed",
    '.z': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Compressed",
    '.zip': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Compressed",
    # Disc
    '.bin': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Disc",
    '.dmg': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Disc",
    '.iso': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Disc",
    '.toast': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Disc",
    '.vcd': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Disc",
    # Data
    '.csv': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Database",
    '.dat': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Database",
    '.db': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Database",
    '.dbf': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Database",
    '.log': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Database",
    '.mdb': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Database",
    '.sav': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Database",
    '.sql': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Database",
    '.tar': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Database",
    '.xml': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Database",
    '.json': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Database",
    # Executables
    '.apk': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Executables",
    '.bat': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Executables",
    '.com': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Executables",
    '.exe': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Executables",
    '.gadget': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Executables",
    '.jar': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Executables",
    '.wsf': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Executables",
    # Fonts
    '.fnt': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Fonts",
    '.fon': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Fonts",
    '.otf': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Fonts",
    '.ttf': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Other/Fonts",
    # Presentations
    '.key': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/Presentations",
    '.odp': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/Presentations",
    '.pps': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/Presentations",
    '.ppt': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/Presentations",
    '.pptx': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/Presentations",
    # Programming
    '.c': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/C&C++",
    '.class': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Java",
    '.dart': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Dart",
    '.py': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Python",
    '.sh': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Shell",
    '.swift': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/Swift",
    '.html': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/C&C++",
    '.h': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Programming/C&C++",
    # Spreadsheets
    '.ods': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/Microsoft/Excel",
    '.xlr': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/Microsoft/Excel",
    '.xls': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/Microsoft/Excel",
    '.xlsx': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/Text/Microsoft/Excel",
    # System
    '.bak': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/System",
    '.cab': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/System",
    '.cfg': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/System",
    '.cpl': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/System",
    '.cur': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/System",
    '.dll': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/System",
    '.dmp': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/System",
    '.drv': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/System",
    '.icns': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/System",
    '.ico': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/System",
    '.ini': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/System",
    '.lnk': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/System",
    '.msi': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/System",
    '.sys': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/System",
    '.tmp': "C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted/System",
}

folder_to_track = 'C:/Users/ashis dev/Desktop/DOWNLOADS_Copy'
folder_destination = 'C:/Users/ashis dev/Desktop/DOWNLOADS_Copy/Sorted'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()