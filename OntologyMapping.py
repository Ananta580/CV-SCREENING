import Extraction as extraction
import pdftotext as pdftotext
import os
import math
import glob
def list_intersection(l1,l2):
    ul1=[x.upper() for x in l1]
    ul2=[x.upper() for x in l2]
    
    s=0
    
    for i in ul1:
        for j in ul2:
            if len(i)>2:
                if i in j:
                    s+=1
            else:
                if i==j:
                    s+=1
                
    return s

def sim(i1,i2):
    if type(i1) is int or type(i1) is float and type(i2) is int or type(i2) is float:
        if i1>=0 and i2>=0:
            return (1-math.exp(-(i2/(i1+0.001)*1.61)))
        else:
            return 0
        
    elif type(i1) is list and type(i2) is list:
        s=list_intersection(i1,i2)
        t=len(i1)
        
        if s>t:
            return 1
        
        else:
            return s/t
        
    else:
        return -1

def OntologyMapping(jobdescription):
    pdfList=glob.glob("./Upload_Folder/*")
    textList=[]
    pdfs=[]
    #Extracting Ontology from All Pdf's
    for pdf in pdfList:
        pdfs.append(pdf.split('\\')[1])
        textList.append(pdftotext.pdf2txt(pdf))

    ontology=extraction.generate_ontology(textList)
    #Setting Job Description Ontology
    job_criteria=[[jobdescription['skills'],jobdescription['skillsWeight']],[jobdescription['degree'],jobdescription['degreeWeight']],[jobdescription['designation'],jobdescription['designationWeight']],[jobdescription['experienceYear'],jobdescription['experienceYearWeight']]]
    #Finding Weight from Mapping
    M=[]
    n=0
    returnList=[]
    for i in range(len(job_criteria)):
        n+=job_criteria[i][1]
        
    for i in ontology:
        m=0
        
        for j in range(len(job_criteria)):
            m+=sim(job_criteria[j][0],i[j+1])*job_criteria[j][1]
            
        M.append(round(m/n,2))
    
    #Returning Candidate Name , Pdf Name and Weight of each Pdf
    i=0
    for ont in ontology:
        j=0
        for pdf in pdfs:
            k=0
            for m in M:
                if(i==j==k):
                    returnList.append({'name':ont[0],'pdfname':pdf,'weight':m})
                k=k+1
            j=j+1
        i=i+1
    return returnList


# ##### OLD OLD OLD
# import Extraction as extraction
# import pdftotext as pdftotext
# import os
# import math
# import glob
# def list_intersection(l1,l2):
#     ul1=[x.upper() for x in l1]
#     ul2=[x.upper() for x in l2]
#     s=0
#     for i in ul1:
#         for j in ul2:
#             i_split=i.split()
#             j_split=j.split()
#             for k in i_split:
#                 if k in j_split:
#                     s+=1
#                     break
#                 for l in j_split:
#                     if l in i_split:
#                         s+=1
#     return s

# def sim(i1,i2,t=1):
#     if type(i1) is int or type(i1) is float and type(i2) is int or type(i2) is float:
#         if i1>=0 and i2>=0:
#             return (1-math.exp(-(i2/(i1+0.001)*1.61)))
#         else:
#             return 0
        
#     elif type(i1) is list and type(i2) is list:
#         s=list_intersection(i1,i2)
        
#         if s>t:
#             return 1
        
#         else:
#             return s/t
        
#     else:
#         return -1

# def OntologyMapping(jobdescription):
#     pdfList=glob.glob("./Upload_Folder/*")
#     textList=[]
#     pdfs=[]
#     #Extracting Ontology from All Pdf's
#     for pdf in pdfList:
#         pdfs.append(pdf.split('\\')[1])
#         textList.append(pdftotext.pdf2txt(pdf))

#     ontology=extraction.generate_ontology(textList)
#     #Setting Job Description Ontology
#     job_criteria=[[jobdescription['skills'],jobdescription['skillsWeight']],[jobdescription['degree'],jobdescription['degreeWeight']],[jobdescription['designation'],jobdescription['designationWeight']],[jobdescription['experienceYear'],jobdescription['experienceYearWeight']]]
#     #Finding Weight from Mapping
#     M=[]
#     n=0
#     returnList=[]
#     for i in range(len(job_criteria)):
#         n+=job_criteria[i][1]
    
#     for i in ontology:
#         m=0
    
#         for j in range(len(job_criteria)):
#             if j==0:
#                 t=2
                
#             else:
#                 t=1
#             m+=sim(job_criteria[j][0],i[j+1],t)*job_criteria[j][1]
#         if n==0:
#             n=0.00001
#         M.append(round(m/n,2))
    
#     #Returning Candidate Name , Pdf Name and Weight of each Pdf
#     i=0
#     for ont in ontology:
#         j=0
#         for pdf in pdfs:
#             k=0
#             for m in M:
#                 if(i==j==k):
#                     returnList.append({'name':ont[0],'pdfname':pdf,'weight':m})
#                 k=k+1
#             j=j+1
#         i=i+1
#     return returnList

