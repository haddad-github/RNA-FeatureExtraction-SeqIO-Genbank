from Bio import SeqIO

with open("mRNAs.fasta", "w") as f: #commencer a ecrire nouveau fichier fasta ou l'on...

     record = SeqIO.read("sequence.gb", format = "genbank") #lit la sequence du fichier genbank
     
     for feature in record.features: #on extrait les features
           
           if feature.type == "mRNA": #de type mRNA
           
               ARNm = feature
               
               ARNm_join = ARNm.location.extract(record) #pour acceder a id et description
               
               ARNm_join.id = "".join(ARNm.qualifiers["transcript_id"]) #id remplacee par qualifier transcript_id
               ARNm_join.description = "".join(ARNm.qualifiers["product"]) #description remplacee par qualifier product
               
               SeqIO.write(ARNm_join, f, format = "fasta") #ecrire tous les ARNm's modifiee dans le fichier fasta
