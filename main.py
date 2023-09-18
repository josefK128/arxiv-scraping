# main.py
# arxiv-scraping - scrape arxiv categories - save as json-file with form:
#
#               {
#                  'title': title,
#                  'url': result.pdf_url,
#                  'entry_id': result.entry_id, 
#                  'published': result.published.strftime('%m/%d/%y'),
#                  'text': result.summary
#               }


import arxiv
import csv
import os
import datetime
import json
import remove_nonprintables


# category
category = "physics.hist-ph"
_category = input("Enter the arxiv category (or d for default physics.hist-ph : ")
if _category != 'd':
  category = _category
print(f'category = {category}')

# max scraped articles
max = 10
_max = input("Enter the maximum number of articles to summarize (or d for default of 10 : ")
if _max != 'd':
  max = int(_max)
print(f'max = {max}')


search = arxiv.Search(
  query = category,
  max_results = max,
  sort_by = arxiv.SortCriterion.SubmittedDate,
  sort_order = arxiv.SortOrder.Descending
)


filepaths = []
for result in search.results():

  filtered_summary = remove_nonprintables.action(result.summary)

  title = result.title
  title = title.replace('/', '-')
  title = title.replace(':', '-')
  title = title.replace('?', '')
  title = title.replace('"', '')
  data = {
    'title': title,
    'url': result.pdf_url,
    'entry_id': result.entry_id, 
    'published': result.published.strftime('%m/%d/%y'),
    'text': filtered_summary
  }
  print(f'\n\ndata["title"] = {data["title"]}')
  print(f'data["text"] = {data["text"]}')

  # create path with all permissions if it does not already exist
  path = f'./corpus/{category}'
  isExist = os.path.exists(path)
  if not isExist:
    os.makedirs(path)
    os.chmod(path, 0x777) 

  # open the file in the write mode - write JSON
  filepath = f'{path}/{title}.txt'
  filepaths.append(filepath)
  with open(filepath, 'w') as fw:
    json.dump(data, fw)
  fw.close()


  # test the file write
  with open(filepath, 'r') as fr:
    try:
       data_read = json.load(fr)
       fr.close()
    except:
      print(f'{data["title"]} is empty! Deleting file!')
      fr.close()
      os.remove(filepath)




# diagnostics
print('\n\n****************************************************')
for fp in filepaths:
  file = open(fp, "r") 
  size = os.path.getsize(fp)
  print(f'{size} bytes in {fp}')
  if size == 0:
    print(f'File {filepath} is empty! - removing!')
    os.remove(fp)
