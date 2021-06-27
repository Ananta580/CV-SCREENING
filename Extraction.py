import spacy
import dateProcessing as date
import re
# Loading Our Trained Model
trainedModel = spacy.load("model")

def generate_ontology(textlists):
    ontology=[]
    for text in textlists:
        ontology.append(concept_extraction(text))
    return ontology

def concept_extraction(text):
    backupUserName=text.split('\n', 1)[0]
    extractedText = trainedModel(text) # Passing text to Trained Model
    username='A'
    skillList=[]
    experienceYear=0
    degreeList=[]
    designationList=[]
    ontology=[]
    d={}
    experienceList=[]
    # If Saving To File
    f=open("resume"+".txt","w",encoding="utf-8")

    # If Saving To File
    for ent in extractedText.ents:
        d[ent.label_]=[]
    for ent in extractedText.ents:
        d[ent.label_].append(ent.text)
    for i in set(d.keys()):
        f.write("\n\n")
        f.write(i +":"+"\n")
        for j in set(d[i]):
            if i=="name":
                username=j
            f.write(j.replace('\n','')+"\n")
    if username=='A':
        f.write("\n\n")
        f.write('name' +":"+"\n")
        f.write(backupUserName.replace('\n','')+"\n")

    for ent in extractedText.ents:
        d[ent.label_]=[]
    for ent in extractedText.ents:
        d[ent.label_].append(ent.text)
    for i in set(d.keys()):
        for j in set(d[i]):
            if i=="name":
                username=j
            elif i=="degree":
                degreeList.append(j)
            elif i=="designation":
                designationList.append(j)
            elif i=="skill":
                skillList.append(j)
            elif i=="experience":
                experienceList.append(j)
    if username == 'A':
        username=backupUserName
        username = username.replace(u'\xa0', u'')
    for j in experienceList:
        j.strip().replace('\n', '')
        experienceYear=experienceYear+date.ExperienceCalculator(j)
    ontology.append(username)
    ontology.append(skillList)
    ontology.append(degreeList)
    ontology.append(designationList)
    ontology.append(experienceYear)
    #Ontology Format=[['Name', ['Degree1','Degree2'], ['Designation'], ['Skill1, Skill2, Skill3,skill4,skill5'],experienceYear]]
    return ontology

def concept_extraction_single():
    text=''
    with open('Demo_Upload/processing.txt',encoding="utf-8") as f:
        text = f.read()
    backupUserName=text.split('\n', 1)[0]
    extractedConcept=[]
    linkedConcept=''
    extractedText = trainedModel(text) # Passing text to Trained Model
    username='A'
    skillList=[]
    experienceYear=0
    degreeList=[]
    designationList=[]
    ontoloyGenerated=[]
    d={}
    experienceList=[]
    # If Saving To File
    f=open("Demo_Upload/processing"+".txt","w",encoding="utf-8")

    # If Saving To File

    for ent in extractedText.ents:
        d[ent.label_]=[]
    for ent in extractedText.ents:
        d[ent.label_].append(ent.text)
        extractedConcept.append(ent.text)
    for i in set(d.keys()):
        f.write("\n\n")
        f.write(i.upper()+":"+"\n")
        for j in set(d[i]):
            if i=="name":
                username=j
            f.write(j.replace('\n','')+"\n")
    if username=='A':
        extractedConcept.append(backupUserName)
        f.write("\n\n")
        f.write('NAME' +":"+"\n")
        f.write(backupUserName.replace('\n','')+"\n")

    with open('Demo_Upload/processing.txt',encoding="utf-8") as f:
        txt = f.read()
        linkedConcept=re.sub(r"^\s+", "", txt)

    for ent in extractedText.ents:
        d[ent.label_]=[]
    for ent in extractedText.ents:
        d[ent.label_].append(ent.text)
    for i in set(d.keys()):
        for j in set(d[i]):
            if i=="name":
                username=j
            elif i=="degree":
                degreeList.append(j)
            elif i=="designation":
                designationList.append(j)
            elif i=="skill":
                skillList.append(j)
            elif i=="experience":
                experienceList.append(j)
    if username == 'A':
        username=backupUserName
        username = username.replace(u'\xa0', u'')
    for j in experienceList:
        j.strip().replace('\n', '')
        experienceYear=experienceYear+date.ExperienceCalculator(j)
    ontoloyGenerated.append(username)
    ontoloyGenerated.append(skillList)
    ontoloyGenerated.append(degreeList)
    ontoloyGenerated.append(designationList)
    ontoloyGenerated.append(experienceYear)
    conceptExt_conceptLink_ontologyGeneration={'extractedConcept':extractedConcept,'linkedConcept':linkedConcept,'ontoloyGenerated':ontoloyGenerated}
    return conceptExt_conceptLink_ontologyGeneration
concept_extraction_single()
