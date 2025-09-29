def create_project_dict():
  html = ''
  with open('./fixtures/kickstarter.html') as file:
        html = file.read()

  kickstarter = BeautifulSoup(html, 'html.parser')
  projects = {}
  
  # Iterate through the projects
  for project in kickstarter.select("li.project.grid_4"):
    # CORRECTED LINE 1: Use [0] to get the first element
    title = project.select("h2.bbcard_name strong a")[0].text 
    
    projects[title] = {
      # CORRECTED LINE 2: Use [0]['attribute_name'] to access the attribute
      'image_link': project.select("div.project-thumbnail a img")[0]['src'], 
      'description': project.select("p.bbcard_blurb")[0].text,
      'location': project.select("ul.project-meta span.location-name")[0].text,
      'percent_funded': project.select("ul.project-stats li.first.funded strong")[0].text.replace("%","")
    }
    
  # return the projects dictionary
  return projects