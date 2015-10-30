import csv
from py2neo import authenticate,Graph
from py2neo import neo4j,Node,Relationship
 
authenticate("localhost:7474", "neo4j", "neo4j1")

# connect to authenticated graph database
sgraph = Graph("http://localhost:7474/db/data/")

with open('C:\\Users\\brsingh\\Documents\\character_relations2.csv','r') as csvfile:
	filereader = csv.DictReader(csvfile,delimiter=',')
	for row in filereader:
		'''char1 = Node("Person",characterId=row['relation1'])
		char2 = Node("Person",characterId=row['relation2'])
		char1_knows_char2 = Relationship(char1,row['relation'].upper(),char2)
 		sgraph.create(char1_knows_char2)'''
		'''cursor.execute('MATCH (Person1:Person {characterId:"' + row['relation1']+'"}) MATCH (character2:Character {characterId:"' + row['relation2'] + '"}) MERGE (character1.Name)-[:'+ row['relation'].upper() +']->(character2.Name)')
		connection.commit()'''

		txtCommand = "CREATE (" + row['relation1'].replace(' ','_') + ")-[:"+ row['relation'].upper() +"]->("+  row['relation2'].replace(' ','_') +")"
		'''sgraph.cypher.execute(txtCommand)'''
		print txtCommand

		'''print 'relationship made'''